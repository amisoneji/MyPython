#Author :: AMISONEJI
#Sample Program for remove duplicates

#program to remove duplicate characters of a given string.

str=input("enter a string:")
str1="abcdefghijklmnopqrstuvwxyz"

list=[]
s=set() #set only allow unique values
count=0

for i in str1:
    if i in str:
        count=count+1
        if count==1:
            list.append(i)
        else:
            s.add(i) 
print(set)
