#Author :: AMISONEJI
#Sample Program for basic use cases for string.

#.upper() & .lower() method

#Python script that takes input from the user and displays that input back in upper and lower cases.

#user input
str=input("enter a string:")
print ("input in lower:",str.lower()) #convert string into lower case
print ("input in upper:",str.upper()) #convert string into upper case

#Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.  

str=input("enter a string:")
str1=str[0:4] #string slicing (index 0:inclusive,index 1:exclusive)
count=0

for i in str1:
    if i==i.upper():
       count=count+1
       
if count>=2:
    print (str.upper())
else:
    print(str + " because condition not matched")


#Python program to get the last part of a string before a specified character.

str=input("enter email address:")
word=str.split("@") #split string by "@"
li_st=list(word)
print(li_st[1])

#Python program to split a string on the last occurrence of the delimiter.

str=input("enter a string with comma sepration")
print(str.rsplit(",",1))

#Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).

#user inpur
str=input("enter comma seprated list:")

word=str.split(",") #split the string by comma

#convert it in set for unique values 
li_st=list(set(word))

#sorted alphabatically
list=sorted(li_st)
print(list)

#.COUNT() METHOD
#Python program to count occurrences of a substring in a string

str=input("enter a string")
str1=input("enter a sub string")
occ=str.count(str1)
print(occ)


