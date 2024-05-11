customer ={
    "PIN" : 1234,
    "name" : "Derrick Clerkson",
    "balance" :15000,
    "status" : "active",
    "phone" : "+2547XXXXXXX",
    "fuliza status":"paid",
    "fuliza limit": 400
}

def  fuliza(cash,pin):
    if customer["status"] =="active":
        if pin ==customer["PIN"]:
            if customer["fuliza status"]=="paid":
                 if cash<=customer["fuliza limit"]:
                                         customer["fuliza limit"]= customer["fuliza limit"]+ (40/100*cash)
                                         print(f"Success. You have Beeen Awarded Fuliza of amount  {cash} .Your fuliza limit is now {customer['fuliza limit']}.")

                 else:
                      print(f"Your Request for fuliza of {cash} Has Been Denied as Your Limit {customer['fuliza limit']} is low")
               
                 
            else:
                 print("Please repay your fuliza loan before you can apply for another one")
        else:
            print("Wrong PIN!")
    else:
        print("Please Activate Your Account: ")

def  menu():
    print("SIMPLE MPESA USSD APP")
    print("======WELCOME========")
    print("\n")
    print("6.Fuliza Mpesa")

    while True:
        option = int(input("Please enter your choice: "))
        if  option ==6:
                fuliza(
                     int(input("Please Enter Your Fuliza Amount : ")),
                     int(input("Please Enter Your PIN: "))
                )
        else:
             print("We are still working on development")
menu ()