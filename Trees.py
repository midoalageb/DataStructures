from Queue import Queue


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
        q = Queue()
        q.createQueue()
        q.enqueque(root)
        while not q.isEmpty():
            if q.peek().left:
                q.enqueque(q.peek().left)
            if q.peek().right:
                q.enqueque(q.peek().right)
            try:
                print(q.dequeue())
            except ValueError:
                continue

    def search(self, value):
        if self.root is None:
            print("Empty Tree")
            return

        if value == self.root.value:
            print("Found "+str(value))
            return

        q = Queue()
        q.createQueue()
        q.enqueque(self.root)
        while not q.isEmpty():
            if q.peek().left:
                q.enqueque(q.peek().left)
            if q.peek().right:
                q.enqueque(q.peek().right)
            try:
                val = q.dequeue()
                if val.value == value:
                    print("Found " + str(value))
                    return
            except ValueError:
                continue
        print(str(value)+" not found!")
