import unittest
from user import *
from bank import *
from cards import *


class TestUser(unittest.TestCase):
    def setUp(self):
        self.bu1 = BaseUser("ali", "ahmadi")
        self.bank1 = BankAccount("tejarat", 5000)
        self.u2 = User('sara', 'mohamadi', self.bank1)

        self.single = SingleTicket()
        self.credit = CreditCard(8000)

    def testCreateBaseUser(self):
        self.assertEqual(self.bu1.name, "ali")
        self.assertEqual(self.bu1.family, "ahmadi")

    def testCreateUser(self):
        self.assertEqual(self.u2.name, "sara")
        self.assertEqual(self.u2.family, "mohamadi")
        self.assertEqual(self.u2.bank_account, self.bank1)

    def testAdToCart(self):
        self.assertEqual(self.u2.add_to_cards(self.single), [self.single])

        # self.assertEqual(self.u2.add_to_cards(self.credit), self.)


if __name__ == "__main__":
    unittest.main()
