class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Error")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Error")

    def get_balance(self):
        return self.__balance


acc = BankAccount("Viktor", 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.get_balance())

