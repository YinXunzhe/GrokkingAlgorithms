import unittest
from merge_sort import merge,merge_sort


class MyTestCase(unittest.TestCase):
    def test_merge_singleElemtents(self):
        list1=[1]
        list2=[3]
        merged_list=merge(list1,list2)
        self.assertEqual([1,3],merged_list)
    def test_merge_doubleElemtents(self):
        list1=[6]
        list2=[3,8]
        merged_list=merge(list1,list2)
        self.assertEqual([3,6,8],merged_list)
    def test_merge_sort_Double(self):
        list=[2,1]
        sorted_list=merge_sort(list)
        self.assertEqual([1,2],sorted_list)
    def test_merge_sort_Multi_Odd(self):
        list=[2,1,6,3,8]
        sorted_list=merge_sort(list)
        self.assertEqual([1,2,3,6,8],sorted_list)
    def test_merge_sort_Multi_Even(self):
        list=[2,1,6,3]
        sorted_list=merge_sort(list)
        self.assertEqual([1,2,3,6],sorted_list)

if __name__ == '__main__':
    unittest.main()
