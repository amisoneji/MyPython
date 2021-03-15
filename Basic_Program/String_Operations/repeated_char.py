#Author :: AMISONEJI
#Sample Program for repeated chars.

#Python program to count repeated characters in a string

str=input("enter a string:")
str1="abcdefghijklmnopqrstuvwxyz"
for i in str1:
    count=str.count(i)
    if count>1:
        print (i,count)

