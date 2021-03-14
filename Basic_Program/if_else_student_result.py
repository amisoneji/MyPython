#Author :: AMISONEJI
#Sample Program for calculating student result using if-else conditions.

#Admission to professional course in a college according to following conditions:
"""
Marks in Mathematics are greater than or equal to 60 and marks in physics is greater than or equal to 50 and marks in chemistry is greater than or equal to 40
OR
Total marks in mathematics, physics and chemistry is greater than or equal to 200.
OR
Total marks in mathematics and physics are greater than or equal to 150.
Marks of all three subjects will be entered through the keyboard. WAP to tell whether a student is qualifying for admission or not.
"""


## Use Input 
sub1=int(input("Enter 1st subject marks out of 100:"))
sub2=int(input("Enter 2nd subject marks out of 100:"))
sub3=int(input("Enter 3rd subject marks out of 100:"))
sub4=int(input("Enter 4th subject marks out of 100:"))
sub5=int(input("Enter 5th subject marks out of 100:"))


# Marks sum
obtained_marks=sub1+sub2+sub3+sub4+sub5

total_marks=500

#Percentage Formula
per=(obtained_marks*100)/total_marks

# If-elae Conditions 
if (per>=60):
    print("first divison")

elif (per>50 and per<60):
    print("secound divison")

elif (per>40 and per<50):
    print("third divison")

else:
    print("fail")
