class Account:
    def __init__(self, id=0, b=100, air=0):
        self.__id = id
        self.__balance = b
        self.__annualInterestRate = air

    def get_id(self):
        return self.__id

    def get_balance(self):
        return self.__balance

    def get_annualInterestRate(self):
        return self.__annualInterestRate

    def set_id(self, id=float()):
        self.__id = id

    def set_balance(self, b=float()):
        self.__balance = b

    def set_annualInterestRate(self, air=int()):
        self.__annualInterestRate = air

    def get_MonthlyInterestRate(self):
        return (self.__annualInterestRate / 100) / 12

    def get_MonthlyInterest(self):
        return self.__balance * self.get_annualInterestRate()

    def withdraw(self):
        w = eval(input("Withdraw amount: "))
        self.__balance -= w

    def deposit(self):
        d = eval(input("Deposit amount: "))
        self.__balance -= d


Nate = Account(1122, 20000, 4.5)

Nate.withdraw()
Nate.deposit()

print(F"ID: {Nate.get_id()}\nBalance: {Nate.get_balance()}"
      + F"\nMounthly Interest Rate: {Nate.get_MonthlyInterestRate()}"
      + F"\nMounthly Interest {Nate.get_MonthlyInterest()}"
      )
