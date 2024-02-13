# Creating an empty queue

# A structure to represent a queue


class Queue:
    # constructor
    def __init__(self, cap):
        self.cap = cap
        self.front = 0
        self.size = 0
        self.rear = cap - 1
        self.arr = [0] * cap

    # Function to create a queue of given capacity
    # It initializes size of queue as 0
    def createQueue(self):
        return Queue(self.cap)


que = Queue(10)

print(que.size)

que.arr(10)
print(que.size)
