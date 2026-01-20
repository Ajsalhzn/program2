class BankAccount:
    def __init__(self):
        self.__balance = 5000

    def get_balance(slef):
        return slef.__balance
    
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficent balance")

#Object creation
acc = BankAccount()

print("Initial Balance:", acc.get_balance())

acc.deposit(2000)
print("After Deposit:", acc.get_balance())

acc.withdraw(1000)
print("After Withdrawal:", acc.get_balance())