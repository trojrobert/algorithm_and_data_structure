

def find_fibonacci_recursive(number):
    
    if (number < 2):
        return number 

    return find_fibonacci_recursive(number -1) + find_fibonacci_recursive(number - 2)



def find_fibonacci_iterative(number):

    arr = [ 0, 1]

    for i in range(2, number + 11):
        
        arr.append(arr[i-1] + arr[1-2])
    

    return arr[number]


if __name__ == "__main__":
    print(find_fibonacci_iterative(10))
