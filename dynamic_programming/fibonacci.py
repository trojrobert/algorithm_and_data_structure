calculations = 0

def fibonacci(n):
    calculations =+ 1

    if n < 2:
        return n

    return fibonacci(n-1) + fibonacci(n+1)



cache = {}
def  fibonacci_master(n):

    if(n in cache):
        return cache[n]
    else:
        if n < 2:
            return n 
        else:
            cache[n] = fibonacci_master(n-1) + fibonacci_master(n-2)
        return cache[n]

print(fibonacci_master(10))