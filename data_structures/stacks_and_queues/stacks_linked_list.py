

class Node():
    def __init__(self, value):
        self.value = value 
        self.next = None


class Stack:

    def __init__(self):
        self.top = None 
        self.bottom = None 
        self.length = 0 


    def peek(self):
        return self.top.value

    def push(self, value):

        new_node = Node(value)

        #if the stack is empty
        if self.length == 0:
            self.top = new_node 
            self.bottom = new_node 
        
        else:

            temp = self.top
            self.top = new_node
            self.top.next = temp

        self.length += 1

    def pop(self):


        if self.length == 0:
            return None


        self.top = self.top.next
        self.length -= 1 

    def printl(self):

        temp = self.top

        while temp != None:
            print(f"{temp.value} ", end = " -> ")
            temp = temp.next 

        print()





if __name__ == "__main__":

    my_stack = Stack()

    my_stack.push("John")
    my_stack.push("Robert")
    my_stack.pop()
    #my_stack.peek()

    my_stack.printl()