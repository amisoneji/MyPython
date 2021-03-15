#Author :: AMISONEJI
#Sample Program for counting vowels.

str=input("enter a string")
str1="aeiouAEIOU"
count=0
list=[] #create empty list

for i in str:
    if i in str1:
        count=count+1
        list.append(i) #append that element in empty list
print(list) 	
print(count)

