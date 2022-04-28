#Bank application 
accountnumber = 0
CustumerName = ""
pin = 0
mobilenumber = 0
bal = 0
def account():
    global accountnumbers
    global CustumerName
    global pin
    global mobilenumber
    accountnumbers = int(input("Enter account number: "))
    CustumerName = input("Enter your name: ")
    pin = int(input("Enter your pin: "))
    mobilenumber = int(input("Enter your mobile number: "))
    global bal 
    bal = int(input("Enter the balance: "))


def showaccountdetail ():
    print(f"Account number: {accountnumber}\nCustomer Name: {CustumerName}\nPin: {pin}\nMobile Number: {mobilenumber}")


def deposite(amount):
    global bal
    bal = bal + amount
    checkbalance()

def withdraw(amount):
    global bal
    bal = bal - amount

def checkbalance():
    print(f"Your current balance is: {bal}")

#_Mai_#
ch1 = "yes"
while ch1 == "yes":
    print("Welcome to the bank application\n1.Create account\n2.Withdraw\n3.Deposite\n4.Check balance")
    opcion = int(input("Select the option that you need: "))
    if opcion == 1:
        account()
    elif opcion == 2:
        amount = int(input("Enter the amount withdraw: "))
        withdraw(amount)
    elif opcion == 3:
        amount = int(input("Enter the amount withdraw: "))
        deposite(amount)
    elif opcion == 4:
        checkbalance()
    else:
        print("Invalid, please enter the only 4 valid options: ")
    print("Do you want to continue .. write yes: ")
    ch1 = input()



