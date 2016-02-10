class Queue(object):
    def __init__(self):
        self.myQueue = []

    def enqueue(self, element):
        self.myQueue.append(element)

    def dequeue(self):
        return self.myQueue.pop(0)

    def isEmpty(self):
        if len(self.myQueue) == 0:
            return True
        else:
            return False

myQueue = Queue()
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)

print ("1st dequeued number: ", myQueue.dequeue())
print ("2nd dequeued number: ", myQueue.dequeue())
print ("3rd dequeued number: ", myQueue.dequeue())