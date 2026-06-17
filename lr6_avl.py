import random
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
class AVLTree:
    def __init__(self):
        self.root = None
    def height(self, node):
        return node.height if node else 0
    def balance(self, node):
        return self.height(node.left) - self.height(node.right) if node else 0
    def update(self, node):
        node.height = 1 + max(self.height(node.left), self.height(node.right))
    def rotate_right(self, y):
        x = y.left
        t = x.right
        x.right = y
        y.left = t
        self.update(y)
        self.update(x)
        return x
    def rotate_left(self, x):
        y = x.right
        t = y.left
        y.left = x
        x.right = t
        self.update(x)
        self.update(y)
        return y
    def rebalance(self, node):
        self.update(node)
        b = self.balance(node)
        if b > 1:
            if self.balance(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if b < -1:
            if self.balance(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node
    def insert(self, key):
        self.root = self.insert_node(self.root, key)
    def insert_node(self, node, key):
        if node is None:
            return AVLNode(key)
        if key < node.key:
            node.left = self.insert_node(node.left, key)
        elif key > node.key:
            node.right = self.insert_node(node.right, key)
        else:
            return node
        return self.rebalance(node)
    def delete(self, key):
        self.root = self.delete_node(self.root, key)
    def delete_node(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self.delete_node(node.left, key)
        elif key > node.key:
            node.right = self.delete_node(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            succ = node.right
            while succ.left:
                succ = succ.left
            node.key = succ.key
            node.right = self.delete_node(node.right, succ.key)
        return self.rebalance(node)
    def search(self, key):
        node = self.root
        while node:
            if key == node.key:
                return True
            node = node.left if key < node.key else node.right
        return False
    def inorder(self):
        result = []
        self.inorder_walk(self.root, result)
        return result
    def inorder_walk(self, node, result):
        if node:
            self.inorder_walk(node.left, result)
            result.append(node.key)
            self.inorder_walk(node.right, result)
def avl_balanced(tree, node):
    if node is None:
        return True
    if abs(tree.balance(node)) > 1:
        return False
    return avl_balanced(tree, node.left) and avl_balanced(tree, node.right)
def main():
    try:
        tree = AVLTree()
        values = random.sample(range(1, 5000), 500)
        for v in values:
            tree.insert(v)
        for v in values[:50]:
            tree.insert(v)
        assert tree.inorder() == sorted(values)
        for v in values:
            assert tree.search(v)
        assert not tree.search(-1)
        assert avl_balanced(tree, tree.root)
        remove = values[:250]
        for v in remove:
            tree.delete(v)
        assert tree.inorder() == sorted(values[250:])
        for v in remove:
            assert not tree.search(v)
        assert avl_balanced(tree, tree.root)
        print("Работает")
    except Exception:
        print("Не работает")
def main_broken():
    try:
        tree = AVLTree()
        tree.root = AVLNode(1)
        tree.root.right = AVLNode(2)
        tree.root.right.right = AVLNode(3)
        tree.update(tree.root.right)
        assert avl_balanced(tree, tree.root)
        print("Работает")
    except Exception:
        print("Не работает")
if __name__ == "__main__":
    main()
    main_broken()