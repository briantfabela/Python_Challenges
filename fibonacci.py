from functools import lru_cache # one line way to add memorization to funcs

# using recusion without memorrization

def fibonacci(n): # returns the Nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2: 
        return fibonacci(n-1) + fibonacci(n-2) # return the sum of the prev 2 terms

# using recusion with memorrization

fibonacci_cache = {} # stores values to avoid unecessary repetition

def memoryFibonacci(n):
    # If value in cache, return it
    if n in fibonacci_cache: return fibonacci_cache[n]
    
    # compute Nth term
    if n == 1 or n == 2:
        value = 1
    elif n > 2: 
        value = memoryFibonacci(n-1) + memoryFibonacci(n-2)
    
    fibonacci_cache[n] = value
    return value

# recursive memorization with lru_cache

@lru_cache(maxsize = 1000) # will store the most recent 1000 used values
def lruFibonacci(n):
    
    if n == 1 or n == 2: return 1
    else:
        return lruFibonacci(n-1) + lruFibonacci(n-2)

def main():
    # for n in range(1, 11): print(n, ":", fibonacci(n))

    # for n in range(1,1001): print(n, ":", memoryFibonacci(n))

    for n in range(1,1001): print(n, ":", lruFibonacci(n))


if __name__ == "__main__":
    main()