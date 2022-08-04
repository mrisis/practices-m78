import unittest
from admin import *


class testadmin(unittest.TestCase):
    def setUp(self):
        self.admin1 = Admin("ali", "ahmadi", "ali789", "aliali")
        self.admin1.show_password()

    def testCreate(self):
        self.assertEqual(self.admin1.name, "ali")
        self.assertEqual(self.admin1.family, "ahmadi")
        self.assertEqual(self.admin1.username, "ali789")
        self.assertEqual(self.admin1.show_password(), "aliali")

    def testrepr(self):
        self.assertEqual(self.admin1.__repr__(),"Family : ahmadi your Username is : ali789")


if __name__ == "__main__" :
    unittest.main()

