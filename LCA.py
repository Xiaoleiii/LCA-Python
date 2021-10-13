class LCA(object):
    class Node(object):
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    class BST:
        def __init__(self):
            self.root = None

        def get_node(self, key):
            return self.get_node1(self.root, key)

       
        def get_node1(self, node, key):
           
            if node is None or node.key == key:
                return node

            
            if key > node.key:
                return self.get_node1(node.right, key)

            return self.get_node1(node.left, key)

        def LCA(self, p, q):
            return self.LCA1(self.root, p, q)

        def LCA1(self, root, p, q):

            if root in (None, p, q):
                return root

            left = self.LCA(root.left, p, q)
            right = self.LCA(root.right, p, q)

            if not left:
                return right

            if not right:
                return left

            if left and right:
                return root