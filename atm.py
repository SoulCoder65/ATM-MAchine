print("Welcome to Our Banking Services:")
print("Enter Your Pin:")
status='Yes'
pin=1234
chance=0
balance=50000.00
while chance<3:
    pin_input=int(input())
    if pin_input==pin:
        while status not in ('No','no','n','N'):
            print(end="")
            print("You have entered correct Pin!!")
            print("Entered 1 for checking Balance:")
            print("Entered 2 for Withdrawl:")
            print("Entered 3 for Deposit:")
            print("Entered 4 for Pin Change:")
            print("Entered 5 for Exit:")
            option=int(input("Enter choice??"))
            if option==1:
                print("Balance is ",balance)
                op=input("Would do like to go back")
                if op in ('No','no','n','N'):
                    print("Thank You")
                    break
            elif option==2:
                with_amount=float(input("Enter Amount to be Withdrawl:"))
                if with_amount>balance:
                    print("Don't Have Enough Money!!")
                else:
                    balance=balance-with_amount
                    print("Updated Balance: ",balance)
                    op = input("Would do like to go back")
                    if op in ('No','no','n','N'):
                        print("Thank You")
                        break
            elif option==3:
                add_amount=float(input("Enter Amount to be Added:"))
                balance=balance+add_amount
                print("Updated Balance is ",balance)
                op = input("Would do like to go back")
                if op in ('No','no','n','N'):
                    print("Thank You")
                    break
            elif option==4:
                new_pin=int(input("Enter New Pin:"))
                pin=new_pin
                op = input("Would do like to go back")
                if op in ('No','no','n','N'):
                    print("Thank You")
                    break
            elif option==5:
                status='No'
                print("Thanks For Banking Services!!")
            else:
                print("Invalid Option!!")
    else:
        print("Enter Valid Pin!!")
        chance=chance+1
        if chance==3:
            print("No more Chances!!")
            break