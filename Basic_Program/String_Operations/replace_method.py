#Author :: AMISONEJI
#Sample Program for replace method
"""
Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. 
Sample String : 'restart'
Expected Result : 'resta$t'
"""
#string declaration
s="emrgency"

for i in s:
    if i==s[0]:
        s=s.replace(i,"$")
        s1=i+s[1:]
print(s1)

