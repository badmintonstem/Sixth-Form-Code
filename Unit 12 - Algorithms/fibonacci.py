# program fibonacci.py
# recursive algorithm to calculate the numbers in the
# Fibonacci sequence 0,1,1,2,3,5,8..
# in which each number after the first two
# is the sum of the previous pair of numbers
#each routine is timed


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1    
    return fibonacci(n-1) + fibonacci(n-2)

#iterative method
def fibonacci2(n):
    fibNumbers = [0,1]  #list of first two Fibonacci numbers
# now append the sum of the two previos numbers to the list    
    for i in range(2, n+1):
        fibNumbers.append(fibNumbers[i-1] +fibNumbers[i-2])
    return fibNumbers[n]  

if __name__ == '__main__':
    import timeit
    #input how many items in series
    while True:
        repeats = 20
        n = 0
        while not (n in range(2,41)):
            n = int(input("input how many numbers (between 3 and 40) in the series to calculate: "))
            if (n < 3) or (n > 40):
                print("Number out of range: please enter a number between 3 and 40")
        
        res = fibonacci(n)
        time = timeit.timeit('fibonacci(n)', setup = 'from __main__ import fibonacci, n', number = repeats)
        print('\n')
        print(f'The {n}th term of the fibonacci sequence is {res} and it took {time/repeats}s on average to complete with a recursive function')
        print('\n')
        res = fibonacci2(n)
        time = timeit.timeit('fibonacci2(n)', setup = 'from __main__ import fibonacci2, n', number = repeats)
        print(f'The {n}th term of the fibonacci sequence is {res} and it took {time/repeats}s on average to complete with an iterative function')
        print('\n')
        if input('press any key to continue or type "exit" to quit') == 'exit':
            break