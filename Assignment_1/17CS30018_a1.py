### ROLLNO:         17CS30018
### Name:           Kanishk Singh
### Assignment N0.: 1
### Compilation:    python2 17CS30018_a1.py
### Note:           The input file (data1_19.csv) must be in the same directory



import sys
import math

class Node(object):
    
    def __init__(self,attribute=None,index=None):
        self.attribute=attribute
        self.index=index
        self.children=[]
        
    def _get_index(self):
        return self.index
    
    def _get_attribute(self):
        return self.attribute
    
    def _add_child(self,child):
        self.children.append(child)
        
    def _get_children(self):
        return self.children
    
    def _get_child(self,index):
        try:
            return self.children[index]
        except IndexError:
            print("index_out_of_bounds")
    
    def _print_tree(self,level=0):
        
        print '\t'*level+'+'*(level+1)+(self.attribute)
        
        for child in self.children:
            child._print_tree(level+1)


def entropy(data,target_id):
    
    ### This function returns the entropy from the bifurcation due to the target variable.
    negdict={}
    posdict={}
    n=len(data)
    for i in range(n):
        key=data[i][target_id]
        if key not in posdict.keys():
            posdict[key]=0
        if key not in negdict.keys():
            negdict[key]=0
    for i in range(n):
        key=data[i][target_id]
        if data[i][len(data[0])-1]=="yes":
            posdict[key]+=1
        else:
            negdict[key]+=1
    calculated_entropy=0
    for key in posdict.keys():
        if posdict[key]==0:
            calculated_entropy-=(((negdict[key]*1.0)/(n))*math.log((negdict[key]*1.0)/(negdict[key]+posdict[key]),2))
        elif negdict[key]==0:
            calculated_entropy-=(posdict[key]*1.0/(n)*math.log(posdict[key]*1.0/(negdict[key]+posdict[key]),2))
        else:
            calculated_entropy-=((posdict[key]*1.0/(n)*math.log(posdict[key]*1.0/(negdict[key]+posdict[key]),2)+((negdict[key]*1.0)/(n))*math.log((negdict[key]*1.0)/(negdict[key]+posdict[key]),2)))
    return calculated_entropy

def information_gain(data,target_id):
    
    pos_count=0
    for i in range(len(data)):
        if data[i][len(data[0])-1]=="yes":
            pos_count+=1
    neg_count=len(data)-pos_count
    if neg_count==0:
        entropy_before_split=-((pos_count*1.0/len(data))*math.log((pos_count*1.0/len(data)),2))
    elif pos_count==0:
        entropy_before_split=-((neg_count*1.0/len(data))*math.log((neg_count*1.0/len(data)),2))
    else:
        entropy_before_split=-((pos_count*1.0/len(data))*math.log((pos_count*1.0/len(data)),2)+(neg_count*1.0/len(data))*math.log((neg_count*1.0/len(data)),2))

    entropy_after_split=entropy(data,target_id)
    return entropy_before_split-entropy_after_split


def best_attribute_for_bifurcation(data,attributes):
    
    maximum=-1
    for key in attributes.keys():
        if(maximum<information_gain(data,attributes[key])):
            maximum=information_gain(data,attributes[key])
            key_attribute=key
    dict={}
    n=len(data)
    for i in range(n):
        key=data[i][attributes[key_attribute]]
        if key not in dict.keys():
            dict[key]=[[]]
    for i in range(n):
        key=data[i][attributes[key_attribute]]
        dict[key].append(data[i])
        
    for key in dict.keys():
        dict[key].remove([])
        
    return(key_attribute,attributes,dict)


def Make_Tree(data,attribute_dict):
    
        if(len(attribute_dict)>0):
            (a,b,c)=best_attribute_for_bifurcation(data,attribute_dict)
            new_dict_attribute=b.copy()
            del new_dict_attribute[a]
            Tree=Node(attribute=a,index=b[a])
            for key in c.keys():
                Tree._add_child(Make_Tree_class(key,c[key],new_dict_attribute,b[a]))
            return Tree
        
        else:
            pos_count=0
            for example in data:
                if example[len(example)-1]=="yes":
                    pos_count+=1
            neg_count=len(data)-pos_count
            if(pos_count>=neg_count):
                return Node(attribute="yes")
            else:
                return Node(attribute="no")
        
def Make_Tree_class(key,data,attribute_dict,index):
    Tree=Node(attribute=key,index=index)
    Tree._add_child(Make_Tree(data,attribute_dict))
    return Tree

def percent_accuracy(Tree,data):
    correct_prediction=0
    wrong_prediction=0
    
    for example in data:
        #print(tree_traversal(Tree,example))
        if example[len(data[0])-1]==tree_traversal(Tree,example):
            correct_prediction+=1
        else:
            wrong_prediction+=1
    accuracy=(correct_prediction*100.0)/len(data)        
    print("Percentage accuracy on the givven training_set itself is="+ str(accuracy))
    print("Total number of Wrong predictions ="+str(wrong_prediction))
        


def tree_traversal(Tree,example):
    index=Tree._get_index()
    attribute=Tree._get_attribute()
    
    if attribute=="yes":
        return "yes"
    elif attribute=="no":
        return "no"
    
    elif example[index]==attribute:
        child=Tree._get_child(0)
        return tree_traversal(child,example)

    else:
        children=Tree._get_children()
        for child in children:
            if child._get_attribute()==example[index]:
                return tree_traversal(child,example)
        
def main():
    
    ### This is used for reading the data from the csv file.
    file = open('winequality-red.csv')
    data = [[]]
    for line in file:
        line = line.strip("\r\n")
        data.append(line.split(','))
    data.remove([])
    attributes=data[0];
    
    attribute_dict={}
    
    for i in range(len(attributes)-1):
        attribute_dict[attributes[i]]=i
    
    data.remove(attributes)
    Tree=Make_Tree(data,attribute_dict)
    Tree._print_tree()
    percent_accuracy(Tree,data)

main()



