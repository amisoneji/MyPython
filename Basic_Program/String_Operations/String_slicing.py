#Author :: AMISONEJI
#Sample Program for string slicing.

#Python program to reverse a string.

str=input("enter a string:")
print ("reverse string:",str[::-1])


#Python program to reverse words in a string.

str=input("enter a string:")
word=str.split(" ")
list=list(word)
final_list=list[::-1]
print(" ".join(final_list)) # join the list elements by " "(space)

