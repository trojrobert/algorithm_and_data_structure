
class Node():

    def __init__(self, value):
        self.value = value
        self.next = None



class Queue:

    def __init__(self):
        self.first = None 
        self.last = None 
        self.length = 0 

    def __str__(self):
        return str(self.__dict__)


    def peek(self):

        return self.first.value

    def enqueue(self, value):

        new_node = Node(value)

        if self.length == 0:
            self.first = new_node
            self.last = new_node

        else:

            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):

        if self.length == 0:
            return None 

        temp = self.first 

        self.first = self.first.next 

        self.length -= 1

    def printl(self):

        temp = self.first

        while temp != None:
            print(f"{temp.value} ", end = " -> ")
            temp = temp.next 

        print()



if __name__ == "__main__":
    my_queue = Queue()
    my_queue.enqueue('google')
    my_queue.enqueue('microsoft')
    my_queue.enqueue('facebook')
    my_queue.enqueue('apple')

    my_queue.printl()

    my_queue.dequeue()

    my_queue.printl()

    x = my_queue.peek()
    print(x)



