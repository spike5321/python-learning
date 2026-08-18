import unittest
from main1 import Student

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.chen = Student("张三", "001", 90, 80, 75)
        self.li = Student("李四", "002", 90, 50, 75)
    def test_average(self):
        self.assertEqual(self.chen.get_average(), 81.66666666666667)
        self.assertEqual(self.li.get_average(), 71.66666666666667)
        print("✓ test_average passed")

    def test_is_pass(self):
        self.assertTrue(self.chen.pass_all())
        self.assertFalse(self.li.pass_all())
        print("✓ test_is_pass passed")

if __name__ == "__main__":
    unittest.main()









