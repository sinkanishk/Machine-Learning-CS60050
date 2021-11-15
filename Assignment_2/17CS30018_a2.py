### ROLLNO:         17CS30018
### Name:           Kanishk Singh
### Assignment N0.: 2
### Compilation:    python2 17CS30018_a2.py
### Note:           The input file (data2_19.csv) and test file (test2_19.csv)  must be in the same directory

file = open('data2_19.csv')
data = [[]]
for line in file:
    line = line.strip("\r\n")
    data.append(line.split(','))
data.remove([])

#print data

for i in range(1,len(data)):
    data[i][0]=data[i][0][1]
    data[i][len(data[i])-1]=data[i][len(data[i])-1][0]

freq=[[],[]]
for i in range(len(data[1])-1):
    freq[0].append([0,0,0,0,0])
    freq[1].append([0,0,0,0,0])
for i in range(1,len(data)):
    for j in range(1,7):
        freq[int(data[i][0])][j-1][int(data[i][j])-1]+=1
        
class_array=[0,0]
for i in range(1,len(data)):
    class_array[int(data[i][0])]+=1;

#accuracy(freq,class_array)


file = open('test2_19.csv')
data = [[]]
for line in file:
    line = line.strip("\r\n")
    data.append(line.split(','))
data.remove([])

for i in range(1,len(data)):
    data[i][0]=data[i][0][1]
    data[i][len(data[i])-1]=data[i][len(data[i])-1][0]
    
correct_predictions=0
for i in range(1,len(data)):
    neg_prob=(1.0*class_array[0])/(class_array[0]+class_array[1])
    pos_prob=(1.0*class_array[1])/(class_array[0]+class_array[1])
    for j in range(1,7):
        neg_prob*=((freq[0][j-1][int(data[i][j])-1]+1)*1.0)/(class_array[0]+5)
        pos_prob*=((freq[1][j-1][int(data[i][j])-1]+1)*1.0)/(class_array[1]+5)
    #print(str(pos_prob)+" "+str(neg_prob)+" "+data[i][0])
    if pos_prob>=neg_prob and data[i][0]=='1':
        correct_predictions+=1
    if neg_prob>=pos_prob and data[i][0]=='0':
        correct_predictions+=1

#print freq

percentage=(correct_predictions*1.0/(len(data)-1)*100)
print("Percentage accuracy is "+str(percentage))
print("Total number of correct predictions are "+str(correct_predictions)+" out of "+str(len(data)-1)+" cases")
    


