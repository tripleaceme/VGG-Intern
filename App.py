registered_users = { 
            'Abel' : { 'password' : 'tripleace', 'balance' : 1200 },
            'mario':{'password':'mario', 'balance':5000},
            'prosper': {'password':'prosper', 'balance':4500},
            'theo': {'password':'theo', 'balance':4000} 
            }




#Initialize balance to 0
balance = 0

#Cretating a new user account
def create_account() :

    email = input("please enter an email address: ").lower()
    # The loop checks if the user with the given email  already exist
    if email in registered_users.keys() :

        print("Sorry! Account already exists")
        # Go back to the account creation page
        App()
    else :    
        # Take password for the new account.
        password = input("please choose a password: ")
        # loop makes sure user chooses a character at least 4 character long
        while True:
            if (len(password) > 4):
                break
            else:
                print("password must be at least five characters")
                password = input("please choose a password: ")
    # add the new user to users database
    registered_users[email] = { 'password' : password, 'balance' : balance }
    print("{} successfully created.".format(email))
    # Go home
    App()

def transaction() :
    # Take an account name for account login
    email = input("Enter email associated with your account: ").lower()
    # Check if account name exists in the data base.
    if email in registered_users.keys() :
        # Take password for the new account.
        password = input("Enter password here: ")
        # Authenticate login
        if password == registered_users[email]['password'] :
            print("""
                Select an option below.
                Press 1 to check balance.
                Press 2 to deposit.
                Press 3 to withdraw cash.
                Press 4 to transfer funds.
                """)
            # Take choice of transaction selection
            choice = int(input("Enter your preferred selection here: "))
            if choice == 1:
                check_balance(email)
            elif choice == 2 :
                deposit_cash(email)
            elif choice == 3 :
                withdraw_cash(email)
            elif choice == 4 :
                transfer_cash(email)
            else :
                print("Not a valid key. Try again!")
                # Go home
                App()
        else :
            print("password incorrect, you are not authorized")
            # Go home
            App()
    else :
        print("Account Name not found. Kindly Register")
        # Go home
        App()


def check_balance(email) :

    print("Your balance is {}".fotmat(registered_users[email]['balance']))
    # Go home
    App()

def deposit_cash(email) :
    balance = registered_users[email]['balance']
    amount = int( input("Enter the amount you want to deposit here: ") )
    balance += amount
    # Update Account balance
    registered_users[email]['balance'] = balance
    print("Your balance is {}".fotmat(registered_users[email]['balance']))
    # Go home
    App()

def withdraw_cash(email) :
    balance = registered_users[email]['balance']
    amount = int( input("\nEnter the amount you want to withdraw here: ") )
    balance -= amount
    # Update balance
    registered_users[email]['balance'] = balance
    print("Your balance is {}".fotmat(registered_users[email]['balance']))
    # Go home
    App()

def transfer_cash(email) :
    current_balance = registered_users[email]['balance']
    beneficiary = input("Enter beneficiary account name here: ").lower()
    # Check if beneficiary exists in the data store
    if beneficiary in registered_users.keys() :
        # Take beneficiary's balance
        beneficiary_balance = registered_users[beneficiary]['balance']
        # Take the amount to be transferred
        amount = int(input("Enter the amount you want to transfer here: ") )
        # Check if benefactor has enough in his balance
        if (current_balance < amount) :
            print("Sorry! Not enough balance for this transaction.")
            # Go home
            App()
        else :
            beneficiary_balance += amount
            current_balance -= amount
            # Update the balance of beneficiary and the depositor
            registered_users[beneficiary]['balance'] = beneficiary_balance
            registered_users[email]['balance'] = current_balance
        print("Your current balance is {}".format(registered_users[email]['balance']))
        # Go home
        App()
    else :
        print("Error! Beneficiary not found.\nTry again.")
        # Go home
        App()


def App():

    print("""
            You are welcome to VGG Bank Ltd. 
            Make a selection below for your desire choice of service.
            Press 1 to create an account.
            Press 2 to conduct a transaction.
            Press 0 to close app.""")
    choice_selection = int(input("Enter your preferred selection here: "))
    # Choose action based on choice selection
    if choice_selection == 1 :
        create_account()
    elif choice_selection == 2 :
        transaction()
    elif choice_selection == 0 : 
        print("\nThanks for using this app. Goodbye!")
        exit()


App()