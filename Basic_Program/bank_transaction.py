#Author :: AMISONEJI
#Sample Program for basic bank transaction calculations.

"""
program that has following menu:

Enter code w for withdraw.
Enter code d for deposit.
Enter code c for checking balance.

Note: You can withdraw an amount only if balance is greater than or equal to 500 and withdrawing amount should be less than balance.
"""

balance=10000

x=input("please enter w for withdraw \nd for deposite \nc for checking balance: ")

if x=="w":
    amount=int(input("enter amount:"))
    
    if balance>amount and balance>=500 :
        print("collect your money:")
        print("available balance:",balance-amount)
    else:
        print("withdraw")

elif x=="d":
    amount1=int(input("enter amount:"))
    balance=balance+amount1
    print("now abailable balance:",balance)

else:
    print ("balance is: ",balance)
