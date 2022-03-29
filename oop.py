class BankAccount:
    intr_rate=0.04
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        self.transactions=[]

    def deposit(self,amount):
        self.balance=self.balance+amount
        self.transactions.append("amount deposited:{amount}")

c1=BankAccount("steve",1000)
print(c1.name,c1.balance)