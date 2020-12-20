try: 
    import os
    import sys


except Exception as e:
    print("Some Modules are missing {}".format(e))

sys.path.append('/home/trojrobert/Documents/algorithm_and_data_structure/')

from data_structures.trees.binary_search_tree import (Node, BinarySearchTree)
                
array = [1, 2,3]

class TraversalSearch(BinarySearchTree):

    def __init__(self):
        super(BinarySearchTree).__init__()
        self.root = None

        
    def breadth_first_search(self):
        current_node = self.root

        list_ = []
        queue = []
        queue.append(current_node)

        while(len(queue) > 0):
            current_node = queue[0]
            del queue[0]
            list_.append(current_node.value)

            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)

        return list_

    
    def depth_first_search(self, queue, list_):
        if len(queue) == 0:
            return list_

        current_node = queue[0]
        del queue[0]

        list_.append(current_node.value)

        if current_node.left:
            queue.append(current_node.left)

        if current_node.right:
            queue.append(current_node.right)

        return self.depth_first_search(queue, list_)

if __name__ == "__main__":
    tree  = TraversalSearch()
    tree.insert(9)
    tree.insert(4)
    tree.insert(6)
    tree.insert(20)
    tree.insert(170)
    tree.insert(15)
    tree.insert(1)

    x = tree.lookup(170)

    print(x)

    print(tree.breadth_first_search())
    print(tree.depth_first_search([tree.root], []))


