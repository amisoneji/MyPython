#Author :: AMISONEJI
#Sample Programs for set different methods.

#Python program to create an intersection of sets

my_set1={1,2,3,4}
my_set2={2,3,4,5}
print(my_set1.intersection(my_set2))
         
  
#or

my_set1={1,2,3,4}
my_set2={2,3,4,5}
a=set()
for i in my_set1:
    if i in my_set2:
        a.add(i)
print(a)
 
#Python program to create a union of sets

my_set1={1,2,3,4}
my_set2={2,3,4,5}
print(my_set1.union(my_set2))


#Python program to create set difference.

my_set1={1,2,3,4}
my_set2={2,3,4,5}
re_set=set()
for i in my_set1:
    if i not in my_set2:
        re_set.add(i)
print(re_set)
 
#or

my_set1={1,2,3,4}
my_set2={2,3,4,5}
print(my_set1.difference(my_set2))

#Python program to create a symmetric difference.
A={1,2,3,4,5}
B={3,4,5,6,7}
C=set()
for i in A:
    if i not in B:
        C.add(i)
for i in B:
    if i not in A:
        C.add(i)
print(C)
 
#or
  
A={1,2,3,4,5}
B={3,4,5,6,7}
print(A.symmetric_difference(B))



