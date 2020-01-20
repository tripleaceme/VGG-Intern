"""
A command line banking application with the following:
- Create account
- Perform transactions when user is authenticated
    - Check balance
    - Deposit funds
    - Withdraw funds
    - Transfer funds
"""

# dict of users to be used
registered_users =[
    {'email_add':'mario@vgg.com','password':'mario', 'balance':5000},
    {'email_add':'prosper@vgg.com', 'password':'prosper', 'balance':4500},
    {'email_add':'theo@vgg.com', 'password':'theo', 'balance':4000}]

# function creates a new user
def create_account():
    email = input('please enter an email address: ').lower()
    while True:            
        if ("@" in email) and ("." in email):
            # The loop checks if the user with the given email  already exist
            while True:
                if not duplicate_account('email_add',email):
                    break
                else:
                    print('An account with the email  already exist.')
                    email = input('please enter an email address: ').lower()
            break
        else:
            print("enter a correct email address e.g myself@yourwebsite.com")
            email = input('please enter an email address: ').lower()
    password = input('please choose a password: ')
    # loop makes sure user chooses a character at least 4 character long
    while True:
        if (len(password) > 4):
            break
        else:
            print('password must be at least four characters')
            password = input('please choose a password: ')
    # add the new user to users database
    new_user = {'email_add':email, 'password':password, 'balance': 0}
    registered_users.append(new_user)
    print('{} successfully created'.format(email))


# This function checks if user already exist
# checker represents the value we are trying to see if it has already exist in the DB
# value is the new user input that is been compared against what we have in the DB

def duplicate_account(checker, value):
    for user in registered_users:
        if user[checker] == value:
            return user
    return False


# This function checks if user already exist
# checker represents the value we are trying to see if it has already exist in the DB
# value is the new user input that is been compared against what we have in the DB

def authenticate_user(checker, value):
    for user in registered_users:
        if user[checker] == value:
            return user
    return False

def check_balance(user):
    print('Your account balance is {}'.format(user['balance']))


def deposit(user):
    deposit_money = int(input("Enter an amount to be deposited"))
    while True:
        try:
            if deposit_money > 0:
                break
            else:
                print("Invalid amount, only figures are allowed")
                deposit_money = int(input("Enter an amount to be deposited"))
        except ValueError:
            print("Invalid amount, please enter figures only")
            deposit_money = int(input("Enter an amount to be deposited"))
    old_bal = registered_users[user]["balance"]
    new_bal = old_bal + deposit_money
    registered_users[user]["balance"] = new_bal
    print("You have deposited {}, Your new balance is {}".format(deposit_money,new_bal))
    print("Thank you for banking with us")

def withdraw(user):
    withdrawal = int(input("How much do you want to widthraw: "))
    balance = registered_users[user]["balance"]
    if (withdrawal > balance):
        print("Insufficient amount. Kindly fund your account")
        deposit(user)
    else:
        avail_bal = balance - withdrawal
        print("Withdrawal successful. Available balance is {}".format(avail_bal))
        print("Thank you for banking with us")



        
def App():
    print("""
          Welcome to VGG Bank Ltd
      We hope to serve you better today.
              """)



    user_input = input('''
                            Enter 1: Create Account
                            Enter 2: Transaction
                            Enter 0: Exit ''')

    # loop ensures that the user input is 1 or 2
    while True:
        if user_input == '1' or user_input == '2' or user_input == '0':
            break
        else:
            print('Incorrect Input, Enter either 1 or 2 or 0')    
            user_input = input('''
                            Enter 1: create account
                            Enter 2: transaction
                            Enter 0: Exit ''')
        
    # Creating Account
    if (user_input == '1'):
        create_account()
    else:
        #ask user for their password
        password = input('please enter your password: ')
        # check if password is correct
        user_pass = authenticate_user('password', password)
        # if password is not correct return back to the set of options
        if not user_pass:
            print('password incorrect, you are not authorized')
            App()
        # if password is correct
        # makes sure user chooses from available options
        else:
            print('Choose an option')
            operation_options = input('''
                                    Enter 1: check balance
                                    Enter 2: deposit
                                    Enter 3: withdraw
                                    Enter 4: transfer
                                    Enter 0: exit
                            ''')
        while True:
            if operation_options == '0' or operation_options == '1' or operation_options == '2' or operation_options == '3' or operation_options == '4' or operation_options == '0':
                break
            else:
                print('Choose the correct option')
                operation_options = input('''
                                        Enter 1: check balance
                                        Enter 2: deposit
                                        Enter 3: withdraw
                                        Enter 4: transfer
                                        Enter 5: Start Program All Over
                                        Enter 0: exit
                                ''')
        if operation_options == '5':
            App()
        elif operation_options == '1':
            check_balance(user)
        elif operation_options == '2':
            deposit(user)
        elif operation_options == '3':
            withdraw(user)
        elif operation_options == '4':
            transfer(user)
        else:
            exit()
App()