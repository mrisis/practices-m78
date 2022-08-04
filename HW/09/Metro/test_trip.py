import unittest
from tripe import *
from user import User
from bank import BankAccount


class testtrip(unittest.TestCase):
    def setUp(self):
        self.b11 = BankAccount("tejarat", 20000)
        self.u11 = User("reza", "ahmadi", self.b11)
        self.t1 = Tripe('kermanshah', 'tehran', 2000, self.u11, "SingleTicket")

    def testCreate(self):
        self.assertEqual(self.t1.origin, "kermanshah")
        self.assertEqual(self.t1.destination, "tehran")
        self.assertEqual(self.t1.cost, 2000)
        self.assertEqual(self.t1.traveller, self.u11)
        self.assertEqual(self.t1.ticket, "SingleTicket")





if __name__ == "__main__":
    unittest.main()
