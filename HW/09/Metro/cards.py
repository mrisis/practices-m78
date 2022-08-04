from datetime import datetime
import pickle
from log import logger


class SingleTicket:
    tmp = []

    def __init__(self):
        self.name = "SingleTicket"
        self.balance = 2000
        logger.name = __name__
        logger.info(f"singleticket was created with name= {self.name}")
        self.add_to_file(self)
        self.__class__.tmp.append(self)


    def __repr__(self):
        return f"{self.name}"

    def payment(self):
        if self.balance <= 0:
            raise ValueError("your ticket has been used")
        else:
            self.balance -= self.balance

    def add_to_file(self, value):
        with open("cards.pickle", "ab") as f:
            pickle.dump(value, f)
            f.write(b"\n")


class CreditCard:

    def __init__(self, balance=0):
        self.name = "Creditcard"
        self.balance = balance
        logger.name = __name__
        logger.info(f"credit card was created with name= {self.name}")

    def __repr__(self):
        return f"{self.name}"

    def recharge(self, value):
        if value > 0:
            self.balance = self.balance + value
            return self.balance
        else:
            raise ValueError("Invalid value")

    def payment(self, value):
        if self.balance != 0:
            if value > 0 and value < self.balance:
                self.balance = self.balance - value
                return self.balance
            else:
                raise ValueError("Invalid value")
        else:
            raise ValueError("Insufficient inventory")

    def add_to_file(self, value):
        with open("cards.pickle", "ab") as f:
            pickle.dump(value, f)
            f.write(b"\n")

class Card_expiration_date():
    def __init__(self, balance, end_of_date: datetime):
        self.name = "Card_expiration_date"
        self.balance = balance
        self.end_of_date = end_of_date
        logger.name = __name__
        logger.info(f"card_with_expiration_date was created with name= {self.name}")

    def __repr__(self):
        return f"{self.name}"

    @property
    def end_of_date(self):
        return self._end_of_date

    @end_of_date.setter
    def end_of_date(self, value: datetime):
        if value <= datetime.today():
            raise ValueError("The card has expired")
        else:
            self._end_of_date = value

    def recharge(self, value):
        if value > 0:
            self.balance = self.balance + value
            return self.balance
        else:
            raise ValueError("Invalid value")



    def payment(self, value):
        if self.balance != 0:
            if value > 0 and value < self.balance:
                self.balance = self.balance - value
                return self.balance
            else:
                raise ValueError("Invalid value")
        else:
            raise ValueError("Insufficient inventory")




    def add_to_file(self, value):
        with open("cards.pickle", "ab") as f:
            pickle.dump(value, f)
            f.write(b"\n")

# single = SingleTicket()

# single2 = SingleTicket()
# single3 = SingleTicket()
# print(SingleTicket.tmp)
# # print(single)
# single.payment()
# single2.payment()


# with open("cards.pickle", "rb") as f:
#     result = f.readlines()
#     for i in result:
#         print(pickle.loads(i))


# c1 = CreditCard(0)
# print(c.Recharge(12))
# print(c.Decrease(45))
# c2 = Card_expiration_date(10, datetime(2022, 8, 20))
# print(datetime.date.today())
# print(datetime.today())
