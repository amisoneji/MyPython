#Author :: AMISONEJI
#Sample Program for remove and add element in set.

#Python program to remove item(s) from set

my_set={1,2,3,4,5,6}
my_set.remove(5)
print(my_set)

#Python program to remove an item from a set if it is present in the set

my_set={1,14,5,6,15,7,9}

item=int(input("Enter a item you want to remove:"))
if item in my_set:
    my_set.remove(item)
print(my_set)

#Python program to add member(s) in a set

my_set={1,2,3,4,5}
my_set.add(6)
print(my_set)

