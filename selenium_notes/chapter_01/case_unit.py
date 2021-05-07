"""
unttext父类
"""

import unittest

class TestUint(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._Driver = open_bro()
        cls._driver = SecondaryPackaging(cls._Driver)
        cls.driver = login(cls._driver)

    @classmethod
    def tearDownClass(cls):
        pass
        # cls._driver.close()


if __name__ == '__main__':
    unittest.main()
