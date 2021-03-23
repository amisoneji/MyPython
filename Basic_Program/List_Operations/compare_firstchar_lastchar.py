#Author :: AMISONEJI
#Sample Program for comparing first and last character in list.

#Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

list=['abc', 'xyz', 'aba', '1221','jmj']

count=0

for str in list:
    if str[0]==str[-1] and len(str)>1:
        count=count+1
print(count)



