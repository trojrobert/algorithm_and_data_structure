

def find_first_recurring(array):


    #create a set to keep seen items 
    seen_items = {}

    for i in range(len(array)):

        if array[i] in seen_items:
            return array[i]

        else:

            seen_items[array[i]] = i

        print(seen_items)

    print(seen_items)

    return None 


if __name__ == "__main__":

    print(find_first_recurring([2, 5, 1, 2,3, 5, 1, 2, 4]))