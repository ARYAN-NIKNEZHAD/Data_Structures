# we use OOP for make Queue in python


class Queue:

    def __init__(self, lenght) -> None:
        self.lenght = lenght
        self.queue = [None] * lenght
        self.front = -1 
        self.rear = -1

    def display(self):
        if (self.front == -1):
            print("The Queue is empty")

        for i in range(self.front, self.rear + 1):
            print(self.queue[i], end=" ")

    def insert_queue(self, data):
        if ((self.rear + 1) == self.lenght):
            print("The Queue is Full!!")
        
        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear += 1
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
            self.front += 1
            return deleted_element



queue_first = Queue(4)
queue_first.insert_queue(5)
queue_first.insert_queue(5)
queue_first.insert_queue(5)
queue_first.delete_queue()
queue_first.delete_queue()
queue_first.display()


