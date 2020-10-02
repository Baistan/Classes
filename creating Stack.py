class Stack:
    """Custom class for python Stack"""
    def __init__(self):
        self.items = []


    def isEmpty(self):
        return self.items == 0

    def push(self,x):
        self.items.append(x)

    def delete(self):
        self.items.pop()

    def size(self):
        return len(self.items)
    # take берет первый элемент сверху
    def take(self):
        return self.items[-1]

stack = Stack()
for i in range(8):
    stack.push(i)

stack.delete()
print(stack.size())
print(stack.take())
print(stack.items)