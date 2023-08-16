# Bank ATM program using try / except for the purposes of unit testing 
# Requirements = 5 tests, therefore 5 functions. 

bank_customer = {'pin': 1996,  # pin can be changed
                 'balance': 100}  # balance can be changed

banks = {'A': ['BARCLAYS'],
         'B': ['MONZO'],  # dict 'choose bank' outcome = bank choice dependent on user input
         'C': ['CO-OP'],
         }

# Function 1 - simple welcome ATM print function
def welcome_atm():  
    print("** Welcome to ATM **")

welcome_atm()  # calling function - so it executes before other code

# Function 2 - choose bank function
def choose_bank():
    bank = input("CHOOSE BANK: A, B, C :  ")  
    print(banks[bank])  


choose_bank()  # calling function. - so it executes before other code


# Function 3 - invalid withdraw function 
def invalid_withdraw():  
    print("Sorry you cannot withdraw below £10")
    print("RESTART PROGRAM")


# Function 4 - withdraw money 
def withdraw_money():  
    amount = int(input("Enter withdrawal amount £ : "))  # user input (withdrawal amount)
    while True: 
        
        if amount in range(10, 100):  # if in range of 10 to 100 for invalid_withdraw to work / reflect balance
            try:  
                if amount <= bank_customer['balance']:
                    # if statement that checks if amount entered is less than or = to balance
                    bank_customer['balance'] = bank_customer['balance'] - amount
                    # subtraction using dict key's
                    print(f"£{amount}  WITHDRAWN = £ BALANCE IS NOW £{bank_customer['balance']}")
                    # formatted print statement
            finally:  # finally key word for try clause 'this is final thing executed in try'
                print('THANK YOU FOR USING CASH ATM')

        # insufficient funds 
        if amount >= 100:  # if statement checking if amount entered is more than 100 = balance
            try:  
                if amount >= bank_customer['balance']:  # if statement to check if amount is more than ba
                    raise ValueError  # ValueError exception added
            except ValueError:
                print("!*! SORRY YOU HAVE INSUFFICIENT £££ !*!")
                # contents of except block ran if error i.e. not enough money
            finally:
                print("RESTART PROGRAM")
        #   break

        # invalid withdraw 
        try:
            if amount <= 9:  # if statement for if user amount entered less than £10 = invalid withdraw
                raise ValueError
        except ValueError:  
                invalid_withdraw()  # the exception calls the invalid_withdraw function.

        return True  


# Function 5 - pin check maximum 3 times

def pin_check():
    count = 0   
    for count in range(3):  
        try:
            pin = int(input('PLEASE ENTER PIN : **** '))     # input created and defined as int for pin
        except ValueError:     # these do not seem to be in the correct order
            raise ValueError    
            
        else:    
            if pin != bank_customer['pin']:
                # if statement to check whether the pin entered is equal to the user pin 
                print("!*! INCORRECT PIN - TRY AGAIN !*!")
                count += 1  
            else:
                withdraw_money()     
                break    # I have added the break keyword otherwise program continues to run.
            if count == 2:
                print('!*! WARNING LAST PIN ATTEMPT !*!')
    if count == 3:
        print('** 3 UNSUCCESSFUL PIN ATTEMPTS **')
        print('!*! YOUR CARD HAS BEEN LOCKED !*!')






pin_check()   # calling the function