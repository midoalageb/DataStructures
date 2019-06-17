from LinkedList import SingleLinkedList


class Queue:
    def __init__(self):
        self.lst = None

    def createQueue(self):
        self.lst = []

    def enqueque(self, value):
        if self.lst is not None:
            self.lst.append(value)
        else:
            print("Queue not created")

    def dequeue(self):
        if not self.isEmpty():
            tmp = self.lst[0]
            del self.lst[0]
            return tmp
        raise ValueError("Empty list")

    def peek(self):
        if not self.isEmpty():
            return self.lst[0]
        raise ValueError("Empty list")

    def isEmpty(self):
        return not (self.lst is not None and len(self.lst) > 0)

    def deleteQueue(self):
        self.lst = None


class QueueLinkedList:
    def __init__(self):
        self.lst = None

    def createQueue(self):
        self.lst = SingleLinkedList()

    def enqueque(self, value):
        if self.lst is not None:
            self.lst.insert(value)
        else:
            print("Queue not created")

    def dequeue(self):
        if not self.isEmpty():
            tmp = self.lst.head
            self.lst.head = self.lst.head.next
            return tmp
        raise ValueError("Empty list")

    def peek(self):
        if not self.isEmpty():
            return self.lst.head.value
        raise ValueError("Empty list")

    def isEmpty(self):
        return self.lst is None or self.lst.head is None

    def deleteQueue(self):
        self.lst = None
