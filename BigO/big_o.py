import time 

nemo = [ "century", "various", "tribes", "entered", "the", "nemo", "region", "from", "all", "directions", "From", "the", "16th", "century", "to", "the"]

def find_nemo(array):
    t0 = time.time()

    for i in range(len(array)):
        print(f"running")
        if array[i] == 'nemo':

            print("Found nemo")
            break

    t1 = time.time()

    print(f"It took {t1 - t0} milliseconds to run find_nemo method")
if __name__ == "__main__":
    find_nemo(nemo)