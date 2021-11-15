### ROLLNO:         17CS30018
### Name:           Kanishk Singh
### Assignment N0.: 4
### Compilation:    python 17CS30018_a4.py
### Note:           The input file (data4_19.csv) must be in the same directory

import random


def main():
	file = open('data4_19.csv')
	data = [[]]
	for line in file:
		line = line.strip("\r\n")
		data.append(line.split(','))
	data.remove([])
	n=len(data)-1
	mean={}
	count={}
	Jacquard={}
	output={}
	connection={}
	Iris_survey={}
	clusters=0
	for i in range(n):
		key=data[i][len(data[i])-1]
		if key not in Iris_survey.keys():
			clusters=clusters+1
			Iris_survey[key]=0.0
			Jacquard[key]=0.0
			connection[key]=0

	for i in range(clusters):
		key=i
		if key not in mean.keys():
			mean[key]=data[random.randrange(0, len(data)-1, 1)][0:len(data[i])-1]
			count[key]=0
			output[key]=0


	for i in range(10):
		(updated_mean,classified)=iteration(data,mean,n)
		old_mean=mean
		mean=updated_mean
	
	for i in range(n):
		output[classified[i]]+=1

	

	for i in range(n):
		for key in Iris_survey.keys():
			if data[i][len(data[i])-1]==key:
				Iris_survey[key]+=1

	for i in range(clusters):
		for key in Iris_survey.keys():
			x=0
			for j in range(n):
				if classified[j]==i and data[j][len(data[0])-1]==key:
					x=x+1
			if x>count[i]:
				count[i]=x
				Jacquard[key]=1-(x*1.0/(Iris_survey[key]+output[i]-x))
				connection[key]=i

	key_set=set()
	for key in Jacquard.keys():
			key_set.add(connection[key])

	if len(key_set)<clusters:  	#This has been done to avoid ill classification when two classes correspond to the same cluster
		main()
		return

	if 1:
		for i in range(clusters):
			print("Mean of class "+str(i)+"="+str(mean[i]))
		for key in Jacquard.keys():
			print("class("+str(connection[key])+")"+str(key)+"->"+str(Jacquard[key]))


def euclidean(x,y,dim):
	sum=0.0
	for i in range(dim):
		a=float(x[i])
		b=float(y[i])
		sum=sum+(a-b)*(a-b)
	return((sum))

def iteration(data,mean,n):
	classified=[]
	for i in range(n):
		minima=1000000000
		for key in mean.keys():
			dist=euclidean(mean[key],data[i],len(data[i])-1)
			if dist<minima:
				minima=dist
				key_classified=key
		classified.append(key_classified)
	updated_mean=update_mean(data,mean,classified,n)
	return(updated_mean,classified)

def update_mean(data,mean,classified,n):
	count={}
	for key in mean.keys():
		count[key]=0
	for key in mean.keys():
		for j in range(len(mean[key])):
			mean[key][j]=0.0
	for i in range(n):
		key=classified[i]
		count[key]+=1
		for j in range(len(mean[key])):
			mean[key][j]+=float(data[i][j])
	for key in mean.keys():
		for j in range(len(mean[key])):
			if(count[key]):
				mean[key][j]/=count[key]
	return(mean)

main()


