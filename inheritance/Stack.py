class Stack(object):
    def __init__(self):
        self.myStack = []

    def push(self, element):
        self.myStack.append(element)

    def pop(self):
        return self.myStack.pop()

    def isEmpty(self):
        if len(self.myStack) == 0:
            return True
        else:
            return False

myStack = Stack()
myStack.push(1)
myStack.push(2)
myStack.push(3)

print ("1st Popped number: ", myStack.pop())
print ("2nd Popped number: ", myStack.pop())
print ("3rd Popped number: ", myStack.pop())



