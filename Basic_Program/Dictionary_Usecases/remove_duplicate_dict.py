#Author :: AMISONEJI
#Sample Program for remove duplicates. 

#Python program to remove duplicates (based on values) from Dictionary.

D={"A":1,"B":2,"C":3,"A":1,"D":4,"E":9,"C":3}
li=list()
Di=dict()
for key,value in D.items():
    if value not in li:
        li.append(value)
        Di[key]=value
print(Di)
