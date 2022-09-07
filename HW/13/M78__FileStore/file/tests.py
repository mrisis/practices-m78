import unittest
from file.models import *
from file.utils import Validator
from core.managers import db1, DBManager


class test_file(unittest.TestCase):
    def setUp(self):
        self.file = File("film1", "drive1")

    def test_create(self):
        self.assertEqual(self.file.filename, 'film1')
        self.assertEqual(Validator.path_validation(self.file.path), self.file.path)
        self.assertTrue(isinstance(self.file.filename, str))
        self.assertEqual(self.file.path, "drive1")


# # class test_create_file():
# #     def test_create_file(self):
# #         self.filename = "q69"
# #         self.path = "fadaidrive"
# #         file1 = File(self.filename, self.path)
# #         res = db1.create(File, file1)
# #         self.assertIsInstance(res, int)
#
#
# class test_crate_file(unittest.TestCase):
#     def setUp(self):
#         self.db1 = DBManager('file_shop')
#         self.file1 = File('rezafile', 'desktop')
#         self.res = self.file1.register_file(self.db1)
#
#     def test_create_success(self):
#         self.assertIsInstance(self.res, int)
#         self.assertEqual(self.file1.id, self.res)
# #
# #
# # class test_show(unittest.TestCase):
# #     # def setUp(self):
# #     #     self.db1 = DBManager('file_shop')
# #     #     self.files1 = db1.read_all(File)
# #
# #     def test_showing(self):
# #         self.assertIsInstance(self.,list)


if __name__ == "__main__":
    unittest.main()
