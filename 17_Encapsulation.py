     # Encapsulations in python programing
class Bank:
    
    def __init__(self):
        self.__balance = 1000;
        
    def deposit(self,amount):
        self.__balance +=amount;
        
    def get_balance(self):
        return self.__balance;
    
    def withdraw(self, amount):
        self.__balance -= amount;
        
    
account = Bank();
account.deposit(500);
print("Deposit : ",account.get_balance());
account.withdraw(200);
print("Withdraw :",account.get_balance());