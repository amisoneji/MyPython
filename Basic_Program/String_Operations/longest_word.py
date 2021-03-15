#Author :: AMISONEJI
#Sample Program for longest word from the list.


#Python function that takes a list of words and returns the length of the longest one.

#list comprehension
x=[input("enter words:") for i in range(5)]

longest=0

for word in x:
    if len(word)>longest:
        longest=len(word)
print(word)
