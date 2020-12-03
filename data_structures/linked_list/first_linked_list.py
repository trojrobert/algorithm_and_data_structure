class Node:

    def __init__(self, data):

        self.data = data
        self.next = None 

class LinkedList:
    def __init__(self):

        self.head = None 
        self.tail = None


    def append(self, data):
        next_node = Node(data)


        if self.head == None:

            self.head = next_node
            self.tail = self.head

            self.length = 1

        else:

            self.tail.next = next_node
            self.tail = next_node

            self.length += 1



    def prepend(self, data):
        next_node = Node(data)

        next_node.next = self.head
        self.head = next_node
        
        self.length += 1

    def insert(self, index, data):
        next_node = Node(data)
        
        i = 0

        temp = self.head 
       

        if index  >= self.length:
            self.append(data)

            return

        if index == 0:
            self.prepend(data)
            return

        while i < self.length:

            if i == index -1 :
                temp.next , next_node.next = next_node , temp.next

                self.length += 1

                break

            
            temp = temp.next
            i += 1

    def printl(self):

        temp = self.head 

        while temp != None:

            print(f"{temp.data} ", end = " ")

            temp = temp.next 

        print()
        print(f"length = {self.length}")



if __name__ == "__main__":
    my_linked_list = LinkedList()

    my_linked_list.append(10)
    my_linked_list.append(5)
    my_linked_list.append(16)
    my_linked_list.prepend(1)
    my_linked_list.prepend(24)
    my_linked_list.insert(2, 45)
    my_linked_list.printl()
   