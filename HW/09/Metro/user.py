from cards import SingleTicket, CreditCard, Card_expiration_date
from bank import BankAccount
from uuid import uuid4
from datetime import datetime
from log import logger


class BaseUser:
    def __init__(self, name, family):
        self.name = name
        self.family = family


class User(BaseUser):
    list_of_user = []
    def __init__(self, name, family, bank_account, wallet=[]):
        super().__init__(name, family)
        self.bank_account = bank_account
        self.wallet = wallet
        self.__id = uuid4().int % 10000
        logger.name = __name__
        logger.info(f"user was created with name= {self.name}")

    def add_to_cards(self, card):
        if isinstance(card, SingleTicket):
            if card.balance < self.bank_account.balance:
                self.bank_account.balance -= card.balance
                self.wallet.append(card)
        elif isinstance(card, CreditCard):
            if card.balance < self.bank_account.balance:
                self.bank_account.balance -= card.balance
                self.wallet.append(card)
        elif isinstance(card, Card_expiration_date):
            if card.balance < self.bank_account.balance:
                self.bank_account.balance -= card.balance
                self.wallet.append(card)
        return self.wallet



# bank1 = BankAccount("tejarat", 5000)

# single = SingleTicket()
# credit = CreditCard(5000)
# card_ed = Card_expiration_date(7000,datetime(2022,8,28))

# u1 = User('ali','ahmadi',bank1)
#
# u1.add_to_cards(single)
# u1.add_to_cards(credit)
# u1.add_to_cards(card_ed)

