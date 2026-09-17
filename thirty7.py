class bank_account():
    def __init__(self,name,account_number,balance):
        self.name=name
        self.balance=balance
        self.account_number=account_number
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"${amount} deposited successfully")
        else :
            print("Invalid amount")
    def withdraw(self,amount):
        if amount<= 0:
            print("Invalid amount")
        elif amount>self.balance:
            print("insufficient balance")
        else :
            self.balance-=amount
            print(f"${amount} withdred successfully")
    def check_balance(self):
        print(f'Your current balance is {self.balance}')
    def display_balance(self):
        print("\n Account details:")
        print(f"Name: {self.name}")
        print(f"Account number: {self.account_number}")
        print(f"Balance:$ {self.balance}")
        
acc1=bank_account('zeenath',20000,50000)
print(acc1.name)
print(acc1.account_number)
print(acc1.balance)
acc1.deposit(10000)
acc1.withdraw(30000)
print(acc1.balance)