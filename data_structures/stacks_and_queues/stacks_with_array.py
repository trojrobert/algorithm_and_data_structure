

class Stack:

    def __init__(self):
        self.array = []
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    def peek(self):

        return self.array[-1]

    def push(self, value):

        self.array.append(value)
        self.length += 1
        
    def pop(self):
        self.array.pop()
        self.length -= 1


if __name__ == "__main__":


    mystack = Stack()
    mystack.push('google')
    mystack.push('microsoft')
    mystack.push('facebook')
    mystack.push('apple')
    print(mystack)
    x = mystack.peek()
    print(x)
    mystack.pop()
    print(mystack)