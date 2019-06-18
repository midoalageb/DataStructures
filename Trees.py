from Queue import Queue


class BreakError(Exception):
    pass


class TreeNode:
    def __init__(self, val):
        self.right = None
        self.left = None
        self.value = val

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


class BinaryTree:
    def __init__(self):
        self.root = None

    def preOrderTraversal(self, root):
        if root is None:
            # print("Empty Tree")
            return

        print(root)
        self.preOrderTraversal(root.left)
        self.preOrderTraversal(root.right)

    def inOrderTraversal(self, root):
        if root is None:
            # print("Empty Tree")
            return

        self.inOrderTraversal(root.left)
        print(root)
        self.inOrderTraversal(root.right)

    def postOrderTraversal(self, root):
        if root is None:
            # print("Empty Tree")
            return

        self.postOrderTraversal(root.left)
        self.postOrderTraversal(root.right)
        print(root)

    def levelOrderTraversal(self, root):
        self.__levelOrderTraversalFunction__(root, print)

    def __levelOrderTraversalFunction__(self, root, f):
        q = Queue()
        q.createQueue()
        q.enqueque(root)
        while not q.isEmpty():
            if q.peek().left:
                q.enqueque(q.peek().left)
            if q.peek().right:
                q.enqueque(q.peek().right)
            try:
                f(q.dequeue())
            except ValueError:
                continue
            except BreakError:
                return True
        return False

    def search(self, value):
        if self.root is None:
            print("Empty Tree")
            return

        if value == self.root.value:
            print("Found "+str(value))
            return

        def checkVal(mVal):
            val = mVal
            if val.value == value:
                print("Found " + str(value))
                raise BreakError

        found = self.__levelOrderTraversalFunction__(self.root, checkVal)
        if not found:
            print(str(value)+" not found!")

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
            return True
        else:
            def leftInsert(node):
                if node.left is None:
                    node.left = TreeNode(value)
                    raise BreakError
                elif node.right is None:
                    node.right = TreeNode(value)
                    raise BreakError

            return self.__levelOrderTraversalFunction__(self.root, leftInsert)
