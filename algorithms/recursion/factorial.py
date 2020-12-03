


def find_factorial_recursive(number):

    if number == 2 or number == 1:
        return number 
    return number * find_factorial_recursive(number - 1)


def find_factorial_iterative(number):

    answer = 1 

    if (number == 2):
        return 2 

    while(number >= 2):
        answer = answer * number
        number -= 1
    
    return answer


if __name__ == "__main__":
    print(find_factorial_recursive(0))
