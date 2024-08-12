chances = 3
Balance = 1000  # Assuming a starting balance
restart = 'y'

while chances >= 0:
    pin = int(input("Please enter your 4-digit pin: "))
    if pin == 1234:
        # Options for user to choose from
        while restart not in ('n', 'NO', 'no', 'N'):
            print("Please Press 1 for your Balance\n")
            print("Please Press 2 to make a withdrawal\n")
            print("Please Press 3 to make payment\n")
            print("Please Press 4 to return card\n")
            option = int(input("Choose an option: "))
            
            # When user choice is option 1
            if option == 1:
                print(f"Your account balance is ${Balance}\n")  # Displaying user account balance
                restart = input('Would you like to go back? ')
                if restart in ('n', 'NO', 'no', 'N'):
                    print('Thank You')
                    break
                
            # When user choice is option 2
            elif option == 2:
                option2 = 'y'
                # Input to take what the user wants to withdraw & range of amount for user to choose from
                withdrawal = float(input('How much do you want to withdraw? \n- $10/$20/$40/$60/$80/$100: '))
                # Loop to check if amount to withdraw is in the range
                if withdrawal in [10, 20, 40, 60, 80, 100]:
                    # Calculating the balance that will be left
                    Balance = Balance - withdrawal
                    # Displaying available balance
                    print("Your outstanding balance is: $", Balance)
                # When user input is not in the range
                elif withdrawal not in [10, 20, 40, 60, 80, 100]:
                    print("Invalid amount, please re-try \n")
                    restart = 'y'
                # When user choice is not in the amount range 
                elif withdrawal == 1:
                    withdrawal = float(input('Please enter desired amount to withdraw: '))
                    
            # When user wants to top up account balance 
            elif option == 3:
                pay_in = float(input("Please enter amount to pay in: "))
                Balance = Balance + pay_in
                print("Your current balance is: $", Balance)    
                restart = input('Would you like to go back? ')
                if restart in ('n', 'NO', 'no', 'N'):
                    print('Thank You')
                    break  
                
            elif option == 4:
                print("Please wait while your card is being returned... \n")
                print("Thank you for your service")
                break
            
            else:
                print("Please enter the correct number. \n")
                restart = 'y'
                
    else:
        print("Incorrect pin")
        chances -= 1
        if chances == 0:
            print("No more tries")
            break
        