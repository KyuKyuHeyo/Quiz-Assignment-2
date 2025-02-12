flag = False

account_number_list = {} #empty dictionary

#checking account
def account_balance(account_number):
    account_balance_flag = False
    balance = account_number_list[account_number]["balance"]

    while not account_balance_flag:
        print("-----Check Account["+ str(account_number)+"]-----")
        print("1. Check Balance\n2. Deposit\n3. Withdraw\n4. Logout")
        choice_account = int(input("Enter choice: "))

        match choice_account:
            case 1:
                print("Current balance: $" + str(balance))
            case 2: #To depoist
                amount = float(input("Enter amount to deposit: "))
                print("$" + str(amount) + " deposited successfully.")
                balance += amount
            case 3: #To withdraw
                amount = float(input("Enter amount to withdraw: "))
                if amount > balance:
                    print("Insufficient balance.")
                else:
                    print("$" + str(amount) + " withdrawn successfully.")
                    balance -= amount
            case 4:
                #Save new balance from logged in account
                account_number_list[account_number]["balance"] = balance
                print("Logged out!")
                account_balance_flag = True
            case _:
                print("Invalid choice!\nTry again.")
        print()

#Register Validation
def choice1():
    print("-----REGISTER FORM-----")
    account_number = int(input("Enter Account Number: ")) #create new dict

    if account_number in account_number_list:
        print(str(account_number) + " is already exist!")
    else:
        pin = int(input("Enter Account PIN: "))
        account_number_list[account_number] = {"pin":pin, "balance":0.0} #add an item
        print("Registered account!")

#Login Validation
def choice2():
    print("-----LOGIN FORM-----")
    account_number = int(input("Enter Account Number: "))
    pin = int(input("Enter Account PIN: "))

    if account_number in account_number_list and account_number_list[account_number]["pin"] == pin:
        account_balance(account_number)
    elif account_number in account_number_list and account_number_list != pin:
        print("Invalid password!\nPlease try again.")
    else:
        print("Invalid account!\nPlease register an account.")

while not flag:
    print("-----Menu-----")
    print("1. Register\n2. Login\n3. Exit")

    choice = int(input("Enter choice: "))
    print()

    match choice:
        case 1:
            choice1()
        case 2:
            choice2()
        case 3:
            print("Program closed!")
            flag = True
        case _:
            print("Invalid choice!")

    print()
