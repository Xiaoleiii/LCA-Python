import unittest
from LCA import LCA

class TestLCA(unittest.TestCase):
 

    def test_bst_constructor(self):
        tree = LCA.BST()
        self.assertEqual(None, tree.root)

    def test_get_node_none(self):
        tree = LCA.BST()
        self.assertEqual(None, tree.get_node(1))

    def test_lca_none(self):
        tree = LCA.BST()
        self.assertEqual(None, tree.LCA(1, 2))

    def test1(self):
        tree = LCA.BST()
        self.assertEqual(tree.get_node(3), tree.LCA(1, 2))

    def test2(self):
        tree = LCA.BST()
        self.assertEqual(tree.get_node(5), tree.LCA(8, 9))

    

if __name__ == '__main__': 
    unittest.main()
