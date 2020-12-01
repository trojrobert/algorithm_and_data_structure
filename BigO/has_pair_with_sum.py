


def has_pair_with_sum(array, expected_sum):

    my_set = set()

    for i in range(len(array)):

        #check for the item in a set
        if array[i] in my_set:
            return True

        my_set.add(expected_sum - array[i])
    
    return False


if __name__ == "__main__":

    print(has_pair_with_sum([6, 4, 3, 2, 1, 7], 9))