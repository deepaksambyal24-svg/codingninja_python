# It follows First In First Out (FIFO)
# Insert -> ENQUEUE
# Remove -> DEQUEUE

class Queue:
    def __init__(self):
        self.arr = []

    def is_empty(self):
        return len(self.arr) == 0

    def enqueue(self, data):
        self.arr.append(data)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.arr.pop(0)

    def front(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.arr[0]


# Driver Code
qu = Queue()

qu.enqueue(10)
qu.enqueue(20)
qu.enqueue(30)

print("Front:", qu.front())      # 10
print("Dequeued:", qu.dequeue()) # 10
print("Front:", qu.front())      # 20