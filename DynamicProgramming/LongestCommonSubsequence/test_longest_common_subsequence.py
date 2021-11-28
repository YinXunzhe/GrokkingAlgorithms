import unittest
from longest_common_subsequence import longest_common_subsequence


class MyTestCase(unittest.TestCase):
    def test_ordinary(self):
        str1 = "fosh"
        str2 = "fish"
        ans = longest_common_subsequence(str1, str2)
        self.assertEqual(ans, 3)  # add assertion here

    def test_empty_string(self):
        str1 = ""
        str2 = "fish"
        ans = longest_common_subsequence(str1, str2)
        self.assertEqual(ans, 0)  # add assertion here

    def test_single_char(self):
        str1 = "i"
        str2 = "fish"
        ans = longest_common_subsequence(str1, str2)
        self.assertEqual(ans, 1)  # add assertion here


if __name__ == '__main__':
    unittest.main()
