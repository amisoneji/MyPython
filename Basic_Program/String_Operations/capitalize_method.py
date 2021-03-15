#Author :: AMISONEJI
#Sample Program for capitalize letters.



#Python program to capitalize first and last letters of each word of a given string. 

str=input("enter a string")
str1=str.split(" ")
li_st=[]
for word in str1:
    li_st.append(word[0].upper()+word[1:-1]+word[-1].upper())
print(" ".join(li_st))
