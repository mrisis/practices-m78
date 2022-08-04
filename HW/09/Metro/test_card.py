import unittest
from cards import *
from datetime import datetime


class TestCards(unittest.TestCase):

    def setUp(self):
        self.single = SingleTicket()
        self.single.payment()
        self.credit = CreditCard(7000)
        self.credit.payment(1000)

        self.card_ed = Card_expiration_date(8000, datetime(2022, 8, 29))
        self.card_ed.payment(3000)

        self.credit2 = CreditCard(9000)
        self.credit2.recharge(1000)

        self.card_ed2 = Card_expiration_date(11000, datetime(2022, 8, 17))
        self.card_ed2.recharge(1000)



    def testcreateSingleTicket(self):
        self.assertEqual(self.single.balance, 0)

    def testcreateCreditCard(self):
        self.assertEqual(self.credit.balance, 6000)

    def testcreatCard_expiration_date(self):
        self.assertEqual(self.card_ed.balance, 5000)
        self.assertEqual(self.card_ed.end_of_date, datetime(2022, 8, 29))

    def testpaymentSingleTicket(self):
        self.assertEqual(self.single.balance, 0)
        # self.assertRaises(ValueError, self.single.balance < 0)

    def testPaymentCreditCard(self):
        self.assertEqual(self.credit.balance, 6000)

    def testRechrgeCreditCard(self):
        self.assertEqual(self.credit2.balance, 10000)

    def testPaymentCard_expiration_date(self):
        self.assertEqual(self.card_ed.balance, 5000)

    def testRechrgeCard_expiration_date(self):
        self.assertEqual(self.card_ed2.balance, 12000)


if __name__ == "__main__":
    unittest.main()
