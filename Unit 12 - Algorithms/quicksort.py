def quicksort(items):
    # A list of a single item does not need sorting
    if len(items) <= 1:
        return items
    else:
        pointer1 = 1
        pointer2 = len(items)-1
        pivot_value = items[0]
        while pointer2 >= pointer1:
            while pointer1 <= pointer2 and items[pointer1] <= pivot_value:
                # move left pointer right
                pointer1 += 1
            while pointer2 >= pointer1 and items[pointer2] >= pivot_value:
                # move right pointer left
                pointer2 -= 1
            # swap items
            if pointer2 > pointer1:
                temp = items[pointer1]
                items[pointer1] = items[pointer2]
                items[pointer2] = temp
        # Put the pivot into the correctposition
        items[0] = items[pointer2]
        items[pointer2] = pivot_value
        
        # Recursively call the quick sort
        left = quicksort(items[:pointer2])
        right = quicksort(items[pointer2+1:])
        return left + [pivot_value] + right

unsorted = [34,56,23,81,28,66,35,17,88,37,18,50]
print(quicksort(unsorted))