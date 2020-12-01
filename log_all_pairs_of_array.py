boxes = [1, 2, 3, 4, 5]

def log_all_pairs_array(array):

    for i in range(len(array)):

        for j in range(len(array)):

            print(f"{array[i]}, {array[j]}")


if __name__ == "__main__":

 log_all_pairs_array(boxes)