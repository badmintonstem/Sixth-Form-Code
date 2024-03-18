def linearSearch(listToSearch, item):
    #index = -1
    i = 0
    #found = False
    for i, currentItem in enumerate(listToSearch):
        if currentItem == item:
            return i
    return -1

def binarySearchR(listToSearch, item):
    if len(listToSearch) == 0:
        return -1
    
    midPoint = len(listToSearch)//2
    if listToSearch[midPoint] == item:
        return midPoint
    elif listToSearch[midPoint] > item:
        return binarySearchR(listToSearch[:midPoint], item)
    elif listToSearch[midPoint] < item:
        temp = binarySearchR(listToSearch[midPoint+1:], item)
        return temp + midPoint + 1 if temp >= 0 else temp

def binarySearchI(listToSearch, item):
    found = False
    first = 0
    last = len(listToSearch)-1
    while first <= last and not found:
        mid = (first + last)//2
        if listToSearch[mid] == item:
            return mid
        elif listToSearch[mid] < item:
            first = mid + 1
        else:
            last = mid - 1
    return -1

def read_words(filename):
    with open(filename) as f:
        return [line.strip().lower() for line in f]

if __name__ == '__main__':
    import os
    import timeit
    from random import randint
    
    REPEATS = 1000
    try:
        currDir = os.path.dirname(os.path.realpath(__file__))
        inputFile = os.path.join(currDir,"words.txt")
        words = read_words(inputFile)
    except OSError as e:
        print("Unable to read word file {}".format(e))
    
    girlsNames = ['Amelia', 'Ava', 'Emily', 'Isabella', 'Isla', 'Jessica', 'Lily', 'Olivia', 'Poppy', 'Sophie']
    #print(words)
    #numberList = [randint(0,100) for _ in range(50)]
    #numberList.sort()
    #print(numberList)
    word = 'zulu'
    item = linearSearch(words, word)
    time = timeit.timeit('linearSearch(words, word)', setup = 'from __main__ import linearSearch, words, word', number = REPEATS)
    print(f'it took {time}s to find the word {word} with a linear search')
    item = binarySearchI(words, word)
    time = timeit.timeit('binarySearchR(words, word)', setup = 'from __main__ import binarySearchR, words, word', number = REPEATS)
    print(f'it took {time}s to find the word {word} with a binary search (recursive)')
    item = binarySearchR(words, word)
    time = timeit.timeit('binarySearchI(words, word)', setup = 'from __main__ import binarySearchI, words, word', number = REPEATS)
    print(f'it took {time}s to find the word {word} with a binary search (iterative)')