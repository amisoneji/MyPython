#Author :: AMISONEJI
#Sample Program for removing duplicates from list.

list=[1,2,3,4,2,3,5,6,7]

no_dup=set()
count=0

for i in list:
    if i  not in no_dup:
        no_dup.add(i)
print(no_dup)


