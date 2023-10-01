username="shyamkumar"
password="shyamkumar@123"
u_username=input("Enter your name:")
p_password=input("Enter the password:")
if u_username==username and p_password==password:
    print("You are successfully login into your account!")
    print("*-----------------------*-------------------------*")
    print("Please select your option from given below:")
    print('''   
             1.Deposite
             2.Withdraw
             3.check Bank Balance
             4.Exit''')
    amount=20000
    option=int(input("Enter your option:"))
    if option==1:
        deposite_amount=int(input("Enter your deposite amount:"))
        amount+=deposite_amount
        print("Your total bank balance is:",amount)
        print("-----------Thank you for visiting------------")
    elif option==2:
        withdraw_amount=int(input("Enter your withdrawal amount:"))
        if withdraw_amount<=(amount-2000):
            amount-=withdraw_amount
            print("your Remaining bank balance is:",amount)
        elif withdraw_amount>amount:
            print("Please enter sufficient balance!")
        else:
                print("Please maintain minimum of 2000/-Rs balance in your account")
                print("-----------Thank you for visiting------------")
    elif option==3:
        print("Your total balance is:",amount)
        print("-----------Thank you for visiting------------")
    elif option==4:
        print("Thank you for visiting,you are successfully exit!")



    
else:

      print("Please entered valid username or password")
    


