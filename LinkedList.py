class Node:
    def __init__(self, val):
        self.next = None
        self.previous = None
        self.value = val

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


class SingleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value):
        if value is None:
            return
        mNode = Node(value)

        if self.head is None:
            self.head = mNode

        if self.tail is None:
            self.tail = mNode
        else:
            self.tail.next = mNode
            self.tail = mNode

    def traverse(self):
        node = self.head

        while node:
            print(node.value)
            node = node.next

    def search(self, val):
        node = self.head

        while node:
            if node.value == val:
                print("Found " + str(val))
                return
            node = node.next

        print(str(val)+" not found")

    def delete(self, val):
        if self.head is None:
            print(str(val) + " not found")
            return

        node = self.head
        if node.value == val:
            self.head = node.next
            if node == self.tail:
                self.tail = None
            return

        while node.next:
            if node.next.value == val:
                if self.tail == node.next:
                    self.tail = node
                node.next = node.next.next
                return
            node = node.next

        print(str(val) + " not found")

    def destroy(self):
        self.head = None
        self.tail = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value):
        if value is None:
            return
        mNode = Node(value)

        if self.head is None:
            self.head = mNode

        if self.tail is None:
            self.tail = mNode
        else:
            mNode.previous = self.tail
            self.tail.next = mNode
            self.tail = mNode

    def leftTraverse(self):
        node = self.head

        while node:
            print(node.value)
            node = node.next

    def rightTraverse(self):
        node = self.tail

        while node:
            print(node.value)
            node = node.previous

    def search(self, val):
        node = self.head

        while node:
            if node.value == val:
                print("Found " + str(val))
                return
            node = node.next

        print(str(val)+" not found")

    def delete(self, val):
        if self.head is None:
            print(str(val) + " not found")
            return

        node = self.head
        if self.head == self.tail == node and node.value == val:
            self.tail = self.head = None
            return

        if node == self.head and node.value == val:
            node.next.previous = None
            self.head = node.next
            return

        if node == self.tail and node.value == val:
            self.tail = node.previous
            node.previous.next = None
            return

        while node.next:
            if node.next.value == val:
                if node.next == self.tail:
                    self.tail = node
                if node.next.next:
                    node.next.next.previous = node
                node.next = node.next.next
                return
            node = node.next

        print(str(val) + " not found")

    def destroy(self):
        self.head = None
        self.tail = None

        node = self.head

        while node:
            node.previous = None
            node = node.next


class CircularSingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value):
        if value is None:
            return
        mNode = Node(value)

        if self.head is None:
            self.head = mNode

        if self.tail is None:
            self.tail = mNode
        else:
            self.tail.next = mNode
            self.tail = mNode

        mNode.next = self.head

    def traverse(self):
        node = self.head
        if node is None:
            print("Empty list")
            return
        while True:
            print(node.value)
            node = node.next
            if node == self.head:
                return

    def search(self, val):
        node = self.head

        while True:
            if node.value == val:
                print("Found " + str(val))
                return
            node = node.next
            if node == self.head:
                break

        print(str(val)+" not found")

    def delete(self, val):
        if self.head is None:
            print(str(val) + " not found")
            return

        node = self.head
        if self.head == self.tail == node and node.value == val:
            node.next = None
            self.tail = self.head = None
            return

        if node == self.head and node.value == val:
            self.head = node.next
            self.tail.next = self.head
            return

        while True:
            if node.next.value == val:
                if node.next == self.tail:
                    self.tail = node
                node.next = node.next.next
                return
            node = node.next
            if node == self.head:
                break

        print(str(val) + " not found")

    def destroy(self):
        self.head = None
        self.tail.next = None
        self.tail = None


class CircularDoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, value):
        if value is None:
            return
        mNode = Node(value)

        if self.head is None:
            self.head = mNode
            mNode.next = self.head
            mNode.previous = self.tail

        if self.tail is None:
            self.tail = mNode
        else:
            mNode.previous = self.tail
            mNode.next = self.head
            self.tail.next = mNode
            self.tail = mNode
            self.head.previous = self.tail

    def leftTraverse(self):
        node = self.head
        if node is None:
            print("Empty list")
            return
        while True:
            print(node.value)
            node = node.next
            if node == self.head:
                return

    def rightTraverse(self):
        node = self.tail
        if node is None:
            print("Empty list")
            return
        while True:
            print(node.value)
            node = node.previous
            if node == self.tail:
                return

    def search(self, val):
        node = self.head
        if node is None:
            print("Empty list")
            return
        while True:
            if node.value == val:
                print("Found " + str(val))
                return
            node = node.next
            if node == self.head:
                break

        print(str(val)+" not found")

    def delete(self, val):
        if self.head is None:
            print(str(val) + " not found")
            return

        node = self.head

        # Only 1 item
        if self.head == self.tail == node and node.value == val:
            self.tail = self.head = node.next = node.previous = None
            return

        # Delete 1st item
        if node == self.head and node.value == val:
            node.next.previous = self.tail
            self.head = node.next
            self.tail.next = self.head
            return

        # if node == self.tail and node.value == val:
        #     self.tail = node.previous
        #     node.previous.next = None
        #     return

        while True:
            if node.next.value == val:
                if node.next == self.tail:
                    self.tail = node
                node.next.next.previous = node
                node.next = node.next.next
                return

            node = node.next
            if node == self.head:
                break

        print(str(val) + " not found")

    def destroy(self):
        node = self.head

        while True:
            node.previous = None
            node = node.next
            if node == self.head:
                break

        self.head = None
        self.tail = None
