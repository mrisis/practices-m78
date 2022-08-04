from log import logger


class BankAccount:
    def __init__(self, bank_name, balance=0):
        self.bank_name = bank_name
        self.balance = balance
        logger.name = __name__
        logger.info(f"Bank was created with name= {self.bank_name}")

    def deposit(self, value):
        if value > 5000:
            self.balance += value
        else:
            raise ValueError("Minimum balance to deposit")

    def withdraw(self, value):
        if self.balance > value:
            if value > 0:
                self.balance -= value
            else:
                raise ValueError("Value must be positive")
        else:
            raise ValueError("Not enough balance")


# b1 = BankAccount("tejarat", 10000)
