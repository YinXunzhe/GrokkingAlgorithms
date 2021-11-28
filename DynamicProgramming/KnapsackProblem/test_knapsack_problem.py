import unittest
from zero_one_knapsack import steal_samrtly


class MyTestCase(unittest.TestCase):
    def test_something(self):
        capacity = 4
        goods = {"Guitar": [1500, 1], "Speaker": [3000, 4], "Laptop": [2000, 3]}
        ans = steal_samrtly(capacity, goods)
        self.assertEqual({3500: {"Guitar", "Laptop"}}, ans)  # add assertion here
    def test_add_iPhone(self):
        capacity = 4
        goods = {"Guitar": [1500, 1], "Speaker": [3000, 4], "Laptop": [2000, 3],"iPhone":[2000,1]}
        ans = steal_samrtly(capacity, goods)
        self.assertEqual({4000: {"iPhone", "Laptop"}}, ans)  # add assertion here


if __name__ == '__main__':
    unittest.main()
