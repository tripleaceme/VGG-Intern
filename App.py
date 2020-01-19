print("""
        Welcome to VGG Bank Ltd
       Thank you for banking with us.
            """)

option = int(input("""
                Please choose your prefered operation
                1. Create Account
                2. Perform Transaction
                : """))
user_id = []
password = []
amount = []
if (option == 1):
    username = input("Enter your user ID: ")
    #user_id.append(username)
    while True:
        found_user_id = False
        for user in user_id:
            if (username == user):
                found_user_id = True
                print("Username not available")
            else:
                user_id.append(username)
    
    login = input("Choose a password between 5 - 8 characters: ")
    password.append(login)
    deposit = int(input("How Much do you want to open your account with: "))
    if (len(deposit) < 3):
        print("Enter real value")
        deposit = int(input("How Much do you want to open your account with: "))
    else:
        amount.append(deposit)
        print("Your account with the USER ID {} has been Successsfully created.".format(user_id))
        print("Press 2 to perform your first transaction")
        print("Press 3 to exit")

elif (option == 2):

    username = input("Enter your user ID: ")
    user_id.append(username)
    if(user_id == username):
        print("User ID already exist. Please choose a new one")
        username = input("Enter your user ID: ")
        user_id.append(username)
    else:
        login = input("Choose a password between 5 - 8 characters: ")
        password.append(login)
        deposit = int(input("How Much do you want to open your account with: "))
        if (len(deposit) < 3):
            print("Enter real value")
            deposit = int(input("How Much do you want to open your account with: "))
        else:
            amount.append(deposit)
            print("Your account with the USER ID {} has been Successsfully created.".format(user_id))
            print("Press 2 to perform your first transaction")
            print("Press 3 to exit")
else:
    print("Thank you for Banking with us.")
    exit()