class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
        
    #debit method
    def debit(self,amount):
        self.balance-=amount
        print("Rs",amount,"was debited")  
        print("Total balance was=",self.get_balance())
    def credit(self,amount):
        self.balance+=amount
        print("Rs",amount,"was credited")  
        print("Total balance was=",self.get_balance())
    def get_balance(self):
        return self.balance         
        



a1=Account(12000,39599507)
a1.debit(1000)
a1.credit(500)
print(a1.balance)        