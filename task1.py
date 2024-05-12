# System that uses ussd.
import random
import string

class  Account:
    def __init__(self,accname,pin,amount,accno,branch,status,limit,f_status) :
     
        if amount<= 100:
            print("Your Account balance is Less than the Minimum Amount Accepted for Deposit")
        elif len(accno) != 6:
            print("Your Account Does not exist")
        elif status != "active":
            print('Activate Your Account')
        elif len(pin) != 4:
            print("Please input the right PIN")
        else:
            self.accname =accname
            self.pin =pin
            self.amount =amount
            self.accno =accno
            self.branch=branch
            self.status = status
            self.limit=limit
            self.f_status=f_status




    #Account Creation
    def create_acc(self):
        print("\n \n")
        print("====WELCOME TO ACCOUNT DETAILS====\n")
        self.accno= self.generate_random_string(6)
        acc_number = self.accno
        print(f"Your Account Number is {acc_number}")
        print(f"Your Account name is {self.accname}. Your PIN is  {self.pin}. \nYour Account balance is {self.amount}")
        print(f"Your Account status has now been set to {self.status}")

    def generate_random_string(self,length):
        random.seed(1)
        characters = string.ascii_letters + string.digits  # includes both uppercase and lowercase letters, as well as digits
        random_string = ''.join(random.choice(characters) for i in range(length))
        return random_string
    
    def withdraw(self):
            print("\n\n")
            print("=======WELCOME TO WITHDRAWALS=====\n")
            pin = input("Please Input Your Pin: ")
            if pin ==self.pin:
                    print("=====Access Granted=====\n")
                    am_ount = int(input("Please Enter the Amount You Would like to Withdraw: "))
                    if  am_ount<= self.amount:
                            self.amount-=am_ount
                            print(f"Success! You have successfully withdrawn $ {am_ount}.\n Your Account Balance is Now $ {self.amount}")
                    else:
                            print(f"Insufficient Funds in Your Account to Withdraw Amount $ {am_ount}.\n Your current Acount Balance is {self.amount}")
            else:
                    print("Wrong PIN")

    def deposit(self):
            print("\n\n")
            print("======WELCOME TO DEPOSIT========\n")
            pin=input("Please Input Your PIN: ")
            if pin==self.pin:
                    deposit=int(input("Please Enter the Amount You Would like to Deposit: "))
                    self.amount+=deposit
                    print(f"Success. You have successully Deposited $ {deposit}\n Your Account Balance is Now ${self.amount}")
            else:
                    print("Wrong PIN. \nPlease Input the right PIN")

    def check_balance(self):
            print("\n\n")
            print("======WELCOME TO BALANCES======")
            pin = input("Please Enter Your PIN: ")
            if pin ==self.pin:
                    print(f"Your Account Balance is ${self.amount}")
            else:
                    print("Wrong PIN. \nPlease Input the right PIN")

    def change_pin(self):
            print("\n\n")      
            print("=======WELCOME TO PIN CHANGE=======")  
            pin =input("Please Enter Your PIN: ")
            if pin == self.pin:
                    new = input("Please Enter Your New PIN: ")
                    self.pin = new
                    print(f"Success. PIN successfully updated.\n Your New PIN is {self.pin}")
            else:
                    print("Wrong PIN. Please Enter the Right PIN.")

    def loans(self):
            print("\n\n")
            print("======LOANS======")
            pin = input("Please Enter Your PIN: ")
            if pin == self.pin:
                    loan=int(input("Please Enter the Loan Amount : "))
                    if loan <= self.amount * 70/100:
                            self.amount+=loan
                            print(f"Success. Loan  of $ {loan} Successfully Approved.\n Your Account Balance is Now ${self.amount} ")
                    else:
                            print(f"You Are not Elligable to the Loan Amount of $ {loan}")
            else:
                    print("Wrong PIN. Please Enter the Correct PIN")

    def   savings(self):
            print("\n\n")
            print("======SAVINGS=====")
            pin = input("Please Enter the Your PIN: ")
            if pin == self.pin:
                    saving=int(input("Please Enter the Amount You Want to Save: "))
                    self.amount+=saving
                    print(f"Success. You have Successfully Saved $ {saving}\n Your Account Balance is now ${self.amount}")
            else:
                    print("Wrong PIN. Please Enter the Correct PIN")

    def  choice(self):
            print("\n \n")
            print("Please Choose an Option")
            print("1. Savings")
            print("2. Loan Request")

    def fuliza(self):
            print("\n\n")
            print("====WELCOME TO FULIZA====")
            pin = input("Enter Your PIN: ")
            if pin == self.pin:
                    if self.f_status=="paid":
                        _fuliza= int(input("Enter the Amount You Want to Fuliza: "))
                        if _fuliza <=  self.limit:
                                self.limit+= 5/100* self.limit
                                self.amount+=_fuliza
                                print(f"Success. You have received fuliza of amount $ {_fuliza}. \nYour Account Balance is now $ {self.amount}.\n Your fuliza limit is now $ {self.limit}")
                        else:
                                print(f"Unable to Process Your Fuliza request of {_fuliza}. Your Fuliza limit is {self.limit}")
                    else:
                            print("Your Fuliza Loan is Unpaid. \n Please pay it before requesting for another Loan ")
            else:
                    print("Wrong PIN. Please Input the Right PIN")
    def lipa_na_mpesa(self):
            print("\n \n")
            print("====WELCOME TO LIPA NA MPESA====")
            print("1.Buy goods and services")
            print("2.Paybill")
            print("3.Pochi la biashara")
            option =  input("Input the option: ")

            if option == "1":
                    print("==Till number==")
                    till_number = input("till number: ")
                    print("\n")
                    print("==Amount==")
                    amount = int(input("amount: "))
                    print("\n")
                    print("==PIN==")
                    pin = input("pin: ")
                    if pin == self.pin:
                            if amount <= self.amount:
                                    self.amount-=amount
                                    print(f"Success. You have successfully paid $ {amount} to account number {till_number}.\n Your Account Balance is now $ {self.amount}")
                            else:
                                    print(f"Insufficient Funds in Your Account to send Amount $ {amount}.\n Your current Acount Balance is $ {self.amount}")
                    
            elif option == "2":
                    print("==Paybill==")
                    paybill = input("Enter paybill/business number: ")
                    print("\n")
                    print("==Account number==")
                    account_number = input("Enter account number: ")
                    print("\n")
                    print("==PIN==")
                    pin = input("Enter PIN number: ")
                    if pin==self.pin:
                            if amount <= self.amount:
                                    self.amount-=amount
                                    print(f"Success. You have successfully paid $ {amount} to paybill {paybill} account {account_number}.\n Your account Balance is now $ {self.amount}")
                            else:
                                    print(f"Insufficient Funds in your account to send amount $ {amount}.\n Your current account balance is $ {self.amount}")

            elif option == "3":
                    print("==Pochi la Biashara==")
                    number = int(input("Phone number: "))
                    print("\n")
                    print("==Amount==")
                    amount = input("Amount: ")
                    print("\n")
                    print("==PIN==")
                    pin = input("Enter PIN number: ")
                    if pin == self.pin:
                            if amount <=self.amount:
                                    self.amount -= amount
                                    print(f"Success. You have successfully paid $ {amount} to {number}.\n Your account Balance is now $ {self.amount}")
                            else:
                                    print(f"Insufficient Funds in your account to send amount $ {amount}.\n Your current account balance is $ {self.amount}")


                                    
    def send_money(self):
        print("==Send money==")
        while True:
                number = input("Phone number: ")
                if len(number) == 10 and number.isdigit():
                        break
                else:
                 print("Error: Phone number must be exactly 10 digits.")
        print("\n")
        print("==AMOUNT==")
        amount = int(input("Enter Amount: "))
        print("\n")
        print("==PIN==")
        pin = input("Enter PIN number: ")
        if pin==self.pin:
            if amount <= self.amount:
                    self.amount -=amount    
                    print(f"Success. You sent $ {amount} to {number}.\n Your balance is {self.amount}")
            else:
                    print(f"Insufficient Funds in your account to send amount $ {amount}.\n Your current balance is {self.amount}")



    def menu(self):
            print("\n \n")
            print("====SIMPLE MPESA USSD APP====")
            print("===========WELCOME===========\n")
            print("1. Account Details")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Check Balance")
            print("5. Change PIN")
            print("6. Loans & Savings")
            print("7. Fuliza Mpesa")
            print("8.lipa na mpesa")
            print("9.Send money")
            print("0. Exit")

    
            option =int(input("Please Enter an option: "))
            if option ==1:
                            self.create_acc()

            elif option ==2:
                        self.withdraw()
            elif option ==3:
                        self.deposit()
            elif option ==4:
                        self.check_balance()
            elif option ==5:
                        self.change_pin()
            elif option ==6:
                        self.choice()
                        cho_ice =int(input("Option: "))
                        if cho_ice == 1:
                                self.savings()
                        elif cho_ice ==2:
                                self.loans()
                        else:
                                print("Invalid Option")
                        
            elif option ==7:
                        self.fuliza()
            elif option == 8:
                    self.lipa_na_mpesa()
            elif option == 9:
                    self.send_money()
                    
            elif option == 0:
                    print("====You exit the system===")
                    
            else:
                        print("Still working on Development")
account1=Account(
              input("What is Your Account Name: "),
               input("What is Your Pin: "),
                int(input("Enter the Amount You Would like to Deposit: ")),
                "123456",
                "Westlands",
                "active",
                300,
                "paid"
    )
print("\nSuccess. Account Created Successfully. \n")
while True:
    account1.menu()
    
            