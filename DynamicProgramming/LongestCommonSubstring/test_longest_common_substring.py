import unittest
from longest_common_substring import longest_common_substring
from longest_common_substring_opt import longest_common_substring_opt


class MyTestCase(unittest.TestCase):
    def test_ordinary(self):
        str1 = "fosh"
        str2 = "fish"
        ans = longest_common_substring(str1, str2)
        self.assertEqual(2, ans)  # add assertion here

    def test_ordinary2(self):
        str1 = "hish"
        str2 = "fish"
        ans = longest_common_substring(str1, str2)
        self.assertEqual(3, ans)  # add assertion here

    def test_empty_string(self):
        str1 = ""
        str2 = "fish"
        ans = longest_common_substring(str1, str2)
        self.assertEqual(0, ans)  # add assertion here

    def test_single_char(self):
        str1 = "i"
        str2 = "fish"
        ans = longest_common_substring(str1, str2)
        self.assertEqual(1, ans)  # add assertion here


class MyTestCaseforOpt(unittest.TestCase):
    def test_ordinary(self):
        str1 = "fosh"
        str2 = "fish"
        ans = longest_common_substring_opt(str1, str2)
        self.assertEqual(2, ans)  # add assertion here

    def test_ordinary2(self):
        str1 = "hish"
        str2 = "fish"
        ans = longest_common_substring_opt(str1, str2)
        self.assertEqual(3, ans)  # add assertion here

    def test_empty_string(self):
        str1 = ""
        str2 = "fish"
        ans = longest_common_substring_opt(str1, str2)
        self.assertEqual(0, ans)  # add assertion here

    def test_single_char(self):
        str1 = "i"
        str2 = "fish"
        ans = longest_common_substring_opt(str1, str2)
        self.assertEqual(1, ans)  # add assertion here

if __name__ == '__main__':
    unittest.main()
