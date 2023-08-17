# Bank ATM program using try / except for the purposes of unit testing
# Requirements = 5 tests, therefore 5 functions.

bank_customer = {'pin': 1996, 'balance': 100}
banks = {'A': ['BARCLAYS'], 'B': ['MONZO'], 'C': ['CO-OP']}

def welcome_atm():
    print("** Welcome to ATM **")

def choose_bank():
    bank = input("CHOOSE BANK: A, B, C : ")
    print(banks.get(bank, "Invalid bank"))

def invalid_withdraw():
    print("Sorry you cannot withdraw below £10")
    print("RESTART PROGRAM")

def withdraw_money():
    amount = int(input("Enter withdrawal amount £: "))
    if 10 <= amount <= 99:
        try:
            if amount <= bank_customer['balance']:
                bank_customer['balance'] -= amount
                print(f"£{amount} WITHDRAWN = £ BALANCE IS NOW £{bank_customer['balance']}")
            else:
                raise ValueError("Insufficient funds")
        except ValueError:
            print("!*! SORRY YOU HAVE INSUFFICIENT £££ !*!")
        finally:
            print('THANK YOU FOR USING CASH ATM')
    elif amount >= 100:
        print("!*! SORRY YOU HAVE INSUFFICIENT £££ !*!")
        print("RESTART PROGRAM")
    elif amount <= 9:
        invalid_withdraw()

def pin_check():
    for count in range(3):
        try:
            pin = int(input('PLEASE ENTER PIN : **** '))
            if pin == bank_customer['pin']:
                withdraw_money()
                break
            else:
                print("!*! INCORRECT PIN - TRY AGAIN !*!")
        except ValueError:
            raise ValueError
        if count == 2:
            print('!*! WARNING LAST PIN ATTEMPT !*!')
    else:
        print('** 3 UNSUCCESSFUL PIN ATTEMPTS **')
        print('!*! YOUR CARD HAS BEEN LOCKED !*!')

welcome_atm()
choose_bank()
pin_check()
