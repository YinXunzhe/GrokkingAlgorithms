import unittest
from find_mango_seller import find_mango_seller


class MyTestCase(unittest.TestCase):
    def test_no_mango_seller(self):
        # 测试找不到的情况
        graph = {"you": ["alice", "bob", "claire"], "bob": ["anuj", "peggy"], "alice": ["peggy"],
                 "claire": ["jonny", "thon"], "anuj": [], "peggy": [], "jonny": [], "thon": []}
        mango_seller = find_mango_seller(graph)
        self.assertEqual(mango_seller, False)  # add assertion here

    def test_multi_seller(self):
        # 测试存在多个seller，且不同亲密度的情况
        graph = {"you": ["alice", "bobm", "claire"], "bobm": ["anuj", "peggy"], "alice": ["peggy"],
                 "claire": ["jonny", "thom"], "anuj": [], "peggy": [], "jonny": [], "thom": []}
        mango_seller = find_mango_seller(graph)
        self.assertEqual(mango_seller, "bobm is a mango seller!")  # add assertion here


if __name__ == '__main__':
    unittest.main()
