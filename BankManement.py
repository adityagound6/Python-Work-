print("Welcome to Yess Bank")
restart=('y')
chances=3
balance=152304745.632
while chances>=0:
    pin=int(input("Enter your four digit pin number"))
    if pin==(6441):
        print("Welcome Aditya\n")
        while restart not in ('n','no'):
            print("1. Balance Enquery\n")
            print("2. Balance deposit\n")
            print("3. Pay in\n")
            print("4. Return\n")
            option=int(input('choise one option'))
            if option==1:
                print("Your Balaance is",balance)
                restart=input('Whould You Like to Leave')
                if restart in ('no','n'):
                    print("Thank you Aditya")
                    break
            elif option==2:
                withdrawl=float(input("Enter your Amount\n"))
                if withdrawl in [100]:
                    balance=balance-withdrawl
                    print('your balance is',balance)
                    restart=input('Whould like to leave')
                    if restart in ('no','n'):
                        print(Thanku)
                        break
                elif withdrawl !=[100]:
                    print('invalid entery please try again')
                elif withrawl ==1:
                    withdrawl=float(input('Please enter your amount'))
            elif option==3:
                withdrawl=float(input("Enter your Amount\n"))
                if withdrawl in [100]:
                    balance=balance-withdrawl
                    print('your balance is',balance)
                    restart=input('Whould like to leave')
                    if restart in ('no','n'):
                        print(Thanku)
                        break
                elif withdrawl !=[100]:
                    print('invalid entery please try again')
                elif withrawl ==1:
                    withdrawl=float(input('Please enter your amount'))
            elif option==4:
                print('thanks you for visiting')
                break
            else:
                print('enter a correct number')
                restart=('y')
    elif pin !=(6441):
        print('Incorrect Password')
        chances=chances - 1
        if chances == 0:
            print('no more chance')
            break