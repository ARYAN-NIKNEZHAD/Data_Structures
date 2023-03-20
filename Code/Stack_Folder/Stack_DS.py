

class Stack:

    def __init__(self, limit) -> None:
        self.stack = []
        self.limit = limit

    def top(self):
        if len(self.stack) <= 0:
            return -1
        else:
            return self.stack[len(self.stack) - 1]
        
    def push(self, data):
        if len(self.stack) >= self.limit:
            return -1
        else:
            self.stack.append(data)
    
    def pop(self):
        if len(self.stack) <= 0:
            return -1 
        else:
            return self.stack.pop()


stack = Stack(5)
