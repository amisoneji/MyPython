#Author :: AMISONEJI
#Sample Program for Dictionary comprehension

#Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
n=int(input("enter a number till want to square"))
d={i:i*i for i in range(1,n+1)}
print(d)

 
#Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys. 

d={i:i*i for i in range(1,16)}
print(d)
