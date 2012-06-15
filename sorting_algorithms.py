def bubble_sort(file):
    """ Sorts a list of numbers based on the bubble sort algorithm, in place

    >>> file = [4,7,-9,8,0,1]
    >>> bubble_sort(file)
    >>> print file
    [-9, 0, 1, 4, 7, 8]

    Args:
        A list of numbers

    """
    for j in range (len(file)): #Iterate through the entire list.
        for i in range (len(file) - j - 1): #Iterate up the the outer index
            #Swap until the element being swapped meets it match
            if file[i] > file[i+1]:
                file[i], file[i+1] = file[i+1], file[i]

def selection_sort(file):
    """ Sorts a list of numbers based on the selection sort algorithm, in place

    >>> file = [4,7,-9,8,0,1]
    >>> selection_sort(file)
    >>> print file
    [-9, 0, 1, 4, 7, 8]

    Args:
        A list of numbers
    """
    #Replace one element at a time with the next smallest value
    for outer in range (len(file)-1):
        for inner in range (outer, len(file)):
            if file[inner] < file[outer]:
                file[inner], file[outer] = file[outer], file[inner]

def insertion_sort(file):
    """ Sorts a list of numbers based on the insertion sort algorithm, in place

    >>> file = [4,7,-9,8,0,1]
    >>> insertion_sort(file)
    >>> print file
    [-9, 0, 1, 4, 7, 8]

    Arguments:
    file -- a list of numbers

    """
    #Swap current value with all values to the left until it is in place
    for outer in range(1, len(file)):
        current_pos = outer
        while file[current_pos] < file [current_pos - 1] and current_pos > 0:
            file[current_pos], file [current_pos -1] = (file[current_pos-1],
                                                        file[current_pos])
            current_pos += -1

def quick_sort(file):
    """ Sorts a list of numbers based on a the quicksort algorithm

    >>> file = [4,7,-9,8,0,1]
    >>> quick_sort(file)
    [-9, 0, 1, 4, 7, 8]

    """
    #Base case
    if len(file) <= 1:
        return file
    #Pivot is halfway-ish value
    pivot = file[len(file)//2]
    small_pile = []
    large_pile = []
    pivot_count = 0
    #Group values according to their relationship to the pivot
    small_pile = [x for x in file if x < pivot]
    large_pile = [x for x in file if x > pivot]
    pivot_count = file.count(pivot)
    return(quick_sort(small_pile) +
           [pivot]*pivot_count +
           quick_sort(large_pile))

if __name__ == "__main__":
    import doctest
    doctest.testmod()