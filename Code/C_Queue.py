class CQueue:

    def __init__(self, lenght) -> None:
        self.lenght = lenght
        self.queue = [None] * lenght
        self.front = -1 
        self.rear = -1

    def display(self):
        if (self.front == -1):
            print("The Queue is empty")
        elif (self.front <= self.rear):
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
        else:
            for i in range(self.front, self.lenght):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear+1):
                print(self.queue[i], end=" ")

    def insert_queue(self, data):
        if (((self.rear + 1) % self.lenght) == self.front):
            print("The Queue is Full!!")
        
        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % self.lenght
            self.queue[self.rear] = data

    def delete_queue(self):
        if (self.front == -1):
            print("The Queue is empty")
        
        elif (self.front == self.rear):
            deleted_element = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return deleted_element
        else:
            deleted_element = self.queue[self.front]
            self.front = (self.front + 1) % self.lenght
            return deleted_element
        

c_queue = CQueue(4)

c_queue.insert_queue("a")
c_queue.insert_queue("b")
c_queue.insert_queue("c")
c_queue.insert_queue("d")
c_queue.delete_queue()
c_queue.delete_queue()
c_queue.display()
