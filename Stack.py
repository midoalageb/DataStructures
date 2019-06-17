class Stack:
    def __init__(self):
        self.lst = None
        
    def createStack(self):
        self.lst = []
    
    def push(self, value):
        if self.lst is not None:
            self.lst.append(value)
        else:
            print("Stack not created")
    
    def pop(self):
        if not self.isEmpty():
            return self.lst.pop()
        raise ValueError("Empty list")

    def peek(self):
        if not self.isEmpty():
            return self.lst[len(self.lst)-1]
        raise ValueError("Empty list")

    def isEmpty(self):
        return not (self.lst is not None and len(self.lst) > 0)

    def deleteStack(self):
        self.lst = None
