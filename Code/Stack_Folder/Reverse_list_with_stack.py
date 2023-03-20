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
        


def reverse_list_Stack(lst, limit):
    stack = Stack(limit)
    for e in lst:
        stack.push(e)

    for i in range(len(lst)):
        lst[i] = stack.pop()


x = [1, 2, 3]
reverse_list_Stack(x, 10)
print(x)
