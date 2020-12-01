import time 

nemo = ['nemo'] * 100

def find_nemo(array):
    t0 = time.time()

    for i in range(len(array)):

        if array[i] == 'nemo':

            print("Found nemo")

    t1 = time.time()

    print(f"It took {t1 - t0} milliseconds to run find_nemo method")
if __name__ == "__main__":
    find_nemo(nemo)