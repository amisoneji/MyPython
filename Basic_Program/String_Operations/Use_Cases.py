#Author :: AMISONEJI
#Sample Program for basic use cases for string.

#.upper() & .lower() method

#Python script that takes input from the user and displays that input back in upper and lower cases.

#user input
str=input("enter a string:")
print ("input in lower:",str.lower()) #convert string into lower case
print ("input in upper:",str.upper()) #convert string into upper case

#Python program to get the last part of a string before a specified character.

str=input("enter email address:")
word=str.split("@") #split string by "@"
li_st=list(word)
print(li_st[1])


#Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).

#user inpur
str=input("enter comma seprated list:")

word=str.split(",") #split the string by comma

#convert it in set for unique values 
li_st=list(set(word))

#sorted alphabatically
list=sorted(li_st)
print(list)

