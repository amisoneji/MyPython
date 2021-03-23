#Author :: AMISONEJI
#Sample Program for removing particular elements.

#Python program to print a specified list after removing the 0th, 4th and 5th elements.

list=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

new_list=[]

for i,v in enumerate(list):
    if i not in [0,4,5]:
        new_list.append(v)
print(new_list)


#Python program to print the numbers of a specified list after removing even numbers from it. 

list=[2,4,5,7,6,9,10,23,12]
new_list=[]

for i in list:
    if i%2!=0:
        new_list.append(i)
print(new_list)


