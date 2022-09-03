class Atm:
    def __init__(self,cardNumber,pin):
        self.cardNumber= cardNumber
        self.pin= pin  

    def balanceInquiry(self):
        print("your balance is 1000$")

    def cashWithdrawal(self,amount):
        newAmount= 1000-amount
        print("You Withdrawed: " + str(amount) + " ,Your remaining balance is: " + str(newAmount))

def main():
    name= input("Hello, Welcome to the digital ATM, What is your username?")
    print("hello " + name)
    cardNumber = input("Insert your card number here: ")
    pin= input("Enter your pin here: ")
    user= Atm(cardNumber, pin)
    print("Choose your next activity:")
    print("1- Balance Inquiry")
    print("........OR........")
    print("2- Cash Withdrawal")
    activity= int(input("Enter Your next activity:  (Hint: write the number for the activity you want to procced with)"))
    if(activity==1):
        user.balanceInquiry()
    elif(activity==2):
        amount= int(input("Enter the amount: (Warning: Dont write any symbols before or after the amount)"))
        user.cashWithdrawal(amount)
    else:
        print("Enter a valid number: ")

if __name__=="__main__":
    main()