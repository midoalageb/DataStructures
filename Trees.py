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
                tmp = q.dequeue()
                f(tmp)
            except ValueError:
                continue
            except BreakError:
                if tmp:
                    return tmp
                return True
        return False

    def search(self, value):
        if self.root is None:
            print("Empty Tree")
            return

        if value == self.root.value:
            print("Found "+str(value))
            return self.root

        def checkVal(mVal):
            val = mVal
            if val.value == value:
                print("Found " + str(value))
                raise BreakError

        found = self.__levelOrderTraversalFunction__(self.root, checkVal)
        if not found:
            print(str(value)+" not found!")
        else:
            return found

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

    def findDeepestNode(self):
        q = Queue()
        q.createQueue()
        q.enqueque(self.root)
        while not q.isEmpty():
            if q.peek().left:
                q.enqueque(q.peek().left)
            if q.peek().right:
                q.enqueque(q.peek().right)
            try:
                tmp = q.dequeue()
            except ValueError:
                continue
        return tmp

    def delete(self, value):
        tmp = self.search(value)
        if not tmp:
            print(str(value) + " not found!")
            return

        moved = self.findDeepestNode()
        print(moved)

        moved.left = tmp.left
        moved.right = tmp.right

        def findFirstLeafParent(val):
            if val.left == moved:
                val.left = None
                raise BreakError
            elif val.right == moved:
                val.right = None
                raise BreakError

        def replaceDeleted(val):
            print(val)
            if val.left == tmp:
                val.left = moved
                raise BreakError
            elif val.right == tmp:
                val.right = moved
                raise BreakError

        if self.__levelOrderTraversalFunction__(self.root, findFirstLeafParent):
            if self.root == tmp:
                self.root = moved
                if self.__levelOrderTraversalFunction__(self.root, replaceDeleted):
                    return True
            else:
                return self.__levelOrderTraversalFunction__(self.root, replaceDeleted)
        return False
