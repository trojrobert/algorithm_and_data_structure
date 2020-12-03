class Node:

    def __init__(self, value):

        self.left = None 
        self.right = None 
        self.value = value 



class BinarySearchTree:


    def __init__(self):

        self.root = None 


    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return

        else:

            current_node = self.root

            while True:

                if  (value < current_node.value):
                    #left 
                           
                    if current_node.left == None:
                        current_node.left = new_node

                        return

                    else:

                        current_node = current_node.left

                else:
                    #right 

                    if current_node.right == None:
                        current_node.right = new_node

                        return
                    else:

                        current_node = current_node.right  

    def lookup(self, value):
        if self.root == None: 
            return None

        else:

            current_node = self.root

            while current_node:

                if value < current_node.value:

                    #check left node
                    current_node = current_node.left

                elif ( value > current_node.value):
                    current_node = current_node.right

                elif (value == current_node.value):
                    return "found"

            return "Not found"

    def remove(self, value):

        if self.root == None:
            return "The Tree is empty"

        current_node = self.root
        parent_node = None 
        while(current_node):
            if (value < current_node.value):
                parent_node = current_node
                current_node = current_node.left

            elif (value > current_node.value):

                parent_node = current_node
                current_node = current_node.right

            elif(value == current_node.value):

                # No right child 

                if current_node.right == None:
                    
                    #leave node
                    if (parent_node == None):
                        self.root = current_node.left

                    else:

                        if (current_node.value < parent_node.value):

                            parent_node.left = current_node.left 

                        elif (current_node.value > parent_node.value):
                            parent_node.right = current_node.left
                # Option 2: Right child which doesnot have a left child 
                elif (current_node.right.left == null):

                    if(parent_node == None):
                        self.root = current_node.left

                    else:

                        current_node.right.left = current_node.left 

                        #if parent > current, make right child of the left the parent 

                        if( current_node.value < parent_node.value):

                            parent_node.left = current_node.right 

                        #if paarent > current, make right child a right child of the parent 

                        elif( current_node.value > parent_node.value):

                            parent_node.right = current_node.right 


                # Option 3 Right child that has a left child

                else:

                    leftmost = currentNode.right,left 
                    leftmostParent = current_node.right

                    while(leftmost.left != None ):

                        leftmostParent = leftmost
                        leftmost = leftmost.left 

                #Parent left subtree is now the leftmost right subtree

                    leftmostParent.left = leftmost.right
                    leftmost.left = current_node.left
                    leftmost.right = current_node.right 


                    if parent_node == None:
                        self.root = leftmost

                    else:
                        if(currentNode.value < parentNode.value):
                            parent_node.left = leftmost 

                        elif(current_node > parent_node.value):
                            parent_node.right = leftmost 
            return True




    def print_tree(self):
        if self.root != None:
            self.printl(self.root)


    def printl(self, current_node):

        if current_node != None:
            self.printl(current_node.left)
            print(str(current_node.value))
            self.printl(current_node.right)

         

            

if __name__ == "__main__":

    my_binary_tree = BinarySearchTree()
    my_binary_tree.insert(9)
    my_binary_tree.insert(4)
    my_binary_tree.insert(20)
    my_binary_tree.insert(170)
    my_binary_tree.insert(15)

    print(my_binary_tree.remove(170))


    my_binary_tree.print_tree()