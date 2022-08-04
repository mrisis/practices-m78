from uuid import uuid4
from random import randint
from user import *
from cards import *
from log import logger


class Tripe:
    list_of_trips = []

    def __init__(self, origin, destination, cost, traveller: User, ticket: str):
        self._id_trip = randint(1, 10)
        self.__class__.checker(self._id_trip)
        self.origin = origin
        self.destination = destination
        self.cost = cost
        self.traveller = traveller
        self.ticket = ticket
        logger.name = __name__
        logger.info(f"Trip was created with credit= {self._id_trip}")
        self.__class__.list_of_trips.append(self._id_trip)

    @classmethod
    def checker(cls, value):
        if value in cls.list_of_trips:
            raise ValueError("This id trips has already been used")

    def payment_trip(self, ticket):
        wallet_tmp = list(map(str, self.traveller.wallet))
        if ticket not in wallet_tmp:
            raise ValueError("ticket does not exist")
        else:
            temp = wallet_tmp.index(ticket)
            if ticket == "SingleTicket":
                self.traveller.wallet[temp].payment()
            else:
                self.traveller.wallet[temp].payment(self.cost)

#
# t1 = Tripe('kermanshah', 'tehran', 2000, u1, "SingleTicket")
# t1.payment_trip("SingleTicket")
