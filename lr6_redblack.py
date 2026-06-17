import random
class RBNode:
    def __init__(self, key, color, nil):
        self.key = key
        self.color = color
        self.left = nil
        self.right = nil
        self.parent = nil
class RBTree:
    def __init__(self):
        self.nil = RBNode(None, "black", None)
        self.nil.left = self.nil
        self.nil.right = self.nil
        self.nil.parent = self.nil
        self.root = self.nil
    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left is not self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is self.nil:
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
    def rotate_right(self, x):
        y = x.left
        x.left = y.right
        if y.right is not self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is self.nil:
            self.root = y
        elif x is x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
    def insert(self, key):
        node = RBNode(key, "red", self.nil)
        parent = self.nil
        current = self.root
        while current is not self.nil:
            parent = current
            if key == current.key:
                return
            current = current.left if key < current.key else current.right
        node.parent = parent
        if parent is self.nil:
            self.root = node
        elif key < parent.key:
            parent.left = node
        else:
            parent.right = node
        self.fix_insert(node)
    def fix_insert(self, node):
        while node.parent.color == "red":
            if node.parent is node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node is node.parent.right:
                        node = node.parent
                        self.rotate_left(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.rotate_right(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node is node.parent.left:
                        node = node.parent
                        self.rotate_right(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.rotate_left(node.parent.parent)
        self.root.color = "black"
    def search(self, key):
        node = self.root
        while node is not self.nil:
            if key == node.key:
                return True
            node = node.left if key < node.key else node.right
        return False
    def inorder(self):
        result = []
        self.inorder_walk(self.root, result)
        return result
    def inorder_walk(self, node, result):
        if node is not self.nil:
            self.inorder_walk(node.left, result)
            result.append(node.key)
            self.inorder_walk(node.right, result)
    def check(self, node):
        if node is self.nil:
            return 1
        if node.color == "red" and (node.left.color == "red" or node.right.color == "red"):
            return 0
        left = self.check(node.left)
        right = self.check(node.right)
        if left == 0 or right == 0 or left != right:
            return 0
        return left + (1 if node.color == "black" else 0)
    def is_valid(self):
        if self.root.color != "black":
            return False
        return self.check(self.root) != 0
def main():
    try:
        tree = RBTree()
        values = random.sample(range(1, 5000), 500)
        for v in values:
            tree.insert(v)
        for v in values[:50]:
            tree.insert(v)
        assert tree.inorder() == sorted(values)
        for v in values:
            assert tree.search(v)
        assert not tree.search(-1)
        assert tree.is_valid()
        print("Работает")
    except Exception:
        print("Не работает")
def main_broken():
    try:
        tree = RBTree()
        for v in [10, 20, 30, 40, 50]:
            tree.insert(v)
        tree.root.color = "red"
        assert tree.is_valid()
        print("Работает")
    except Exception:
        print("Не работает")
if __name__ == "__main__":
    main()
    main_broken()