#Author :: AMISONEJI
#Sample Programs for replace method
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


""""
a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string. 
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'
"""
s="The lyrics is not that poor!"

snot=s.find("not")
spoor=s.find("poor")

if spoor>snot:
    s=s.replace(s[snot:spoor+4],"good")
    print (s)
else:
    print (s)


