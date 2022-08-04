import unittest
from bank import *


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.bank_sina = BankAccount("sina", 10000)
        self.bank_mellat = BankAccount("mellat", 40000)
        self.bank_sina.deposit(6000)
        self.bank_mellat.withdraw(4000)

    def testcreate(self):
        self.assertEqual(self.bank_sina.bank_name, "sina")
        self.assertEqual(self.bank_sina.balance, 16000)

    def testdeposit(self):
        self.assertEqual(self.bank_sina.balance,16000)
        self.assertRaises(ValueError,self.bank_sina.deposit(2000))

    def testwithdraw(self):
        self.assertEqual(self.bank_mellat.balance,36000)
        self.assertRaises(ValueError,self.bank_mellat.withdraw(41000))

if __name__ == "__main__":
    unittest.main()
