#Author :: AMISONEJI
#Sample Program for calculator

"""
the simple calculator that has following menu:
Enter 1 to find the addition of two numbers.
Enter 2 to find the subtraction of two numbers.
Enter 3 to find the multiplication of two numbers.
Enter 4 to find the division of two numbers.
Enter 5 to find the inverse of a number.
Enter 6 to find the square of a number.
Enter 7 to find the cube of a number.

"""
#user input
x=int(input("Enter 1 for addition \nEnter 2 for substraction \nEnter 3 for multplication \nEnter 4 for divison: \nEnter 5 for inverse of num: \nEnter 6 for square of num \nEnter 7 for cube of num: "))

#conditions
if x in range(1,5):

  num1=int(input("Enter 1st number:"))
  num2=int(input("Enter 2nd number:"))
    
  if x==1:
       print (num1+num2)
  elif x==2:
       print (num1-num2)
  elif x==3:
       print (num1*num2)
  elif x==4:
       print (num1/num2)
else:
  num3=int(input("enter a number:"))
  if x==5:
        print(1/num3)
  elif x==6:
        print (num3*num3)
  else:
        print (num3*num3*num3)



