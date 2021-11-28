import unittest
from longest_common_subsequence import longest_common_subsequence


class MyTestCase(unittest.TestCase):
    def test_ordinary(self):
        str1="fosh"
        str2="fish"
        ans=longest_common_subsequence(str1,str2)
        self.assertEqual(ans, 3)  # add assertion here


if __name__ == '__main__':
    unittest.main()
