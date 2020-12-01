array_1 = [1, 2, 3, 4, 5]
array_2 = [10, 8, 6, 7]

def contain_common_items(arr1 , arr2):

# loop through the first array and create object where properties == items in the array
    map = {}

    for i in range(len(arr1)):

        #check for repeating key 
        if map.keys() != arr1[i]:
            map[arr1[i]] = True
 
    # Loop through second array and check if item in second exist on the created object 

    for j in range(len(arr2)):

        #check  for item  in object    
        if arr2[j] in map:
            return True

    return False

if __name__ == "__main__":

    print(f"{contain_common_items(array_1, array_2)}")