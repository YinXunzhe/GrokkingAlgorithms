import unittest
from quick_sort import quick_sort

class MyTestCase(unittest.TestCase):
    def test_quick_sort_Single(self):
        list=[1]
        sorted_list=quick_sort(list)
        self.assertEqual([1],sorted_list)
    def test_quick_sort_Double(self):
        list=[2,1]
        sorted_list=quick_sort(list)
        self.assertEqual([1,2],sorted_list)
    def test_quick_sort_Multi_Odd(self):
        list=[2,1,6,3,8]
        sorted_list=quick_sort(list)
        self.assertEqual([1,2,3,6,8],sorted_list)
    def test_quick_sort_Multi_Even(self):
        list=[2,1,6,3]
        sorted_list=quick_sort(list)
        self.assertEqual([1,2,3,6],sorted_list)


if __name__ == '__main__':
    unittest.main()
