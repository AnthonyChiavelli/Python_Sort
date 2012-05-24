'''
Created on May 20, 2012

@author: Anthony Reid
'''



def bubble_sort(file):
    """ Sorts a list of numbers based on the bubble sort algorithm
    
    The bubble sort algorithm takes each element in the list and continuously swaps it to the right until the element
    to the right of it is larger or the end of the list is encountered. At each completion of the inner loop, a new element 
    at the right of the array is in place because the largest value will "bubble" over to the right (it will always compare
    lesser to the element next to it, so it will be exchanged until it reaches the end). This means that from the outer index
    onward, the list is sorted. Thus the inner loop only needs to go from 0 to the outer index, rather than traversing the
    entire array each time (this would produce the same result, but it is wasteful). 
    
    If we pass this function a list (4, 1, 3, 8, 5, 9), the inner loop will first swap the 4 until it compares greater
    than the element to the right of it, then do the same for each other element. Note that when the largest element in
    the list is encountered, it will necessarily end up at the right of the list, in its final place. As this process is
    repeated, the sorted region at the right of the list grows (and thus the inner loop can stop before this region) until
    the entire list is sorted
    
    
    
    """
    for j in range (len(file)):                         #Iterate through the entire list. This is the outer index
        
        for i in range (len(file) - j - 1):             #Iterate up the the outer index. Anything beyond this outer index has
                                                        #already been sorted, since each outer iteration results in one element
                                                        #reaching its final place on the right of the list
            
            if file[i] > file[i+1]:                     #If the current value is greater than the next value, swap adjacent values
                                                        #until this is not the case. This works as an if statement rather than a
                                                        #while statement because each time a swap occurs, the initial values is
                                                        #shifted to the right. Each iteration of the inner loop increments the
                                                        #inner index, so the inner loop essentially "follows" the value around,
                                                        #swapping it until no more swaps are needed. 
                file[i], file[i+1] = file[i+1], file[i]
    

def selection_sort(file):
    """ Sorts a list of numbers based on the selection sort algorithm
    
    Selection sort works by selecting the smallest element in progressively smaller sublists, and moving it to the front.
    The outer loop index, which is incremented each pass, represents the beginning of the sublist, while the inner loop 
    finds the smallest element in the sublist and exchanges it with the first element in the sublist.
    
    Let's define a list (6, 8, 4, 2, 1, 3, 5). The outer loop starts at zero, so the first sublist is the entire list. The
    inner loop seeks the smallest value and exchanges it with the first element of the sublist (which is the first element
    of the whole list in this particular case). As 1 is the smallest value, this leaves us with (1, 8, 4, 2, 6, 3, 5). The
    1 (and in general anything before the index of the outer loop) is in its final place. The outer loop index is incremented,
    and now our sublist is (8, 4, 2, 6, 3, 5). A similar seek and exchange leaves us with (2, 4, 8, 6, 3, 5), the 2 and 8 
    having been exchanged. This continues until the last non-trivial sublist ((3, 5)) is sorted
    
    Arguments:
    file -- a list of numbers
    """                               
    for outer in range (len(file)-1):                   #Iterate through the list, stopping before the last element, as this
                                                        #would cause a trivial sublist to be sorted unnecessarily 
        
        for inner in range (outer, len(file)):          #Iterate from the outer index to the end of the file, as anything
                                                        #before the outer index is already sorted. This is because each pass
                                                        #puts one element in its final place. 
                                                        
            if file[inner] < file[outer]:                           #If the element at our inner index is less than the file
                file[inner], file[outer] = file[outer], file[inner] #at the outer index, swap them. 




def insertion_sort(file):                  
    """ Sorts a list of numbers based on the insertion sort algorithm
    
    Insertion sort works by ordering progressively larger sub-lists. The outer loop increases each iteration and represents the
    size of the sub-list being sorted by its inner loop. Each time the outer loop index is incremented, a new element is inserted
    into an already sorted sublist. To find its place, adjacent swaps are made until it is larger than the element to its left
    
    Imagine a list (5, 3, 4, 6, 8). The first iteration of the outer loop would examine the sublist consisting of 5 and 3. The
    inner loop would swap the 3 to the left until it is greater than the element prior to it, or until it is at the end of the
    list. In this case, the swapping terminates because the end is reached. The list is now (3, 5, 4, 6, 8). The next iteration
    of the outer loop looks at the 3, 5, and 4. The inner loop swaps the 4 to the left until it compares positively to the element
    to the right of it. This 4 is not greater than 3, so a swap is made. Now, it is greater than the element prior to it (3), so 
    the inner loop terminates, leaving us with (3, 4, 5, 6, 8). This continues until the outer loop has reached the end, even though
    it so happens that our list is already ordered. 
    
    Notice that after n iterations of the outer loop, n+1 numbers are in place on the right (the case of swapping the first element
    is ignored because that element is always self-ordered). Each iteration of the outer loop simply introduces one new element
    which then must be pushed down the list until it is in place.


    Arguments:
    file -- a list of numbers

    """             
    for outer in range(1, len(file)):                   #Iterate from the second element to the end of the file. Each element
                                                        #is compared with the previous element, so we do not want to start
                                                        #at the very beginning
        
        current_pos = outer                             #Save the outer index so it can be modified without messing up the
                                                        #outer loop
        
                                                        #As long as the element at the current position is lesser than the 
                                                        #value at the prior position (and we have not escaped the lower bounds
                                                        #of the list), keep swapping and moving to the left as needed 
        while file[current_pos] < file [current_pos - 1] and current_pos > 0:
            file[current_pos], file [current_pos -1] = file[current_pos-1], file[current_pos]
            current_pos += -1
         
         
         
def quick_sort(file):
    """ Sorts a list of numbers based on a simple version of quicksort
    
    Quicksort is a recursive algorithm that chooses a value called a pivot (this value can be any from the list), and traverses 
    the list, placing anything larger than the pivot value into one group and anything smaller than the pivot value into a another
    group. In this simple implementation, a group here is another list. Once this is done, the pivot is in its final place. Now
    two recursive calls are made: one with the 'smaller' list as a parameter and one with a call to the 'larger' list as a parameter.
    The results are concatenated together along with the pivot value (which was not placed into any group).
    
    If a single value is passed to quick_sort, it is simple returned as is with no recursive call. This is our base case.
    
    Let's use as an example a list [4, 8, 6, 3, 5, 1]. We will from now on choose the middle (rounding down if needed) value as our
    pivot value, so we will choose 6. We group each element according to its relationship to 6. The smaller list will contain
    [4, 3, 5, 1] and the larger list will contain [8]. We return quick_sort[4, 3, 5, 1] + 6 + quick_sort[8]. We can immediately
    see that the right portion of the list will contain [...6, 8] (quick_sort[8] will return 8). The first recursive call will
    continue to make further recursive calls until the top-most calls return the base case. This results in the complete sorting
    of the list. 
    
    Note also that we keep track of the number of occurrences of the pivot value. Because it is not included in either the
    larger or smaller list, it is lost unless we concatenate it between the recursive calls as many times as it occurs in the
    original list
    
    Unlike the other implementations of sorting methods shown here, this one does not sort in place. This means it requires
    extra memory storage, which can be a problem when sorting large lists. 
    
    Arguments:
    file -- a list of numbers
    
    Returns:
    a sorted list of numbers
    
    """
    if len(file) <= 1:                                  #This is our base case; if the list passed contains 0 or 1 values,
                                                        #simply return it. 
        return file
    
    pivot = file[len(file)//2]                          #Choose a pivot point. This can be any value in the list. I have
                                                        #chosen the (roughly) halfway point. 
                                                        
    small_pile = []                                     #Create lists to store larger and smaller values (compared to the 
    large_pile = []                                     #pivot
    
    pivot_count = 0                                     #To keep track of the number of occurrences of the pivot value
    
    for value in file:                                  #Iterate through each value in the file. If it is smaller than the
        if value < pivot:                               #pivot, place it in small_pile. If it is greater, place it in the
            small_pile.append(value)                    #larger pile. If it is the pivot value, increase the pivot value
        if value > pivot:                               #count.
            large_pile.append(value)
        if value == pivot:
            pivot_count += 1
            
                                                        #Concatenate a recursive call on the smaller pile, the pivot count as
                                                        #many times as it occurs, and a recursive call on the larger pile.
    return(quick_sort(small_pile) + [pivot]*pivot_count + quick_sort(large_pile))




def quick_sort_inplace(file, lower = "zoidberg", upper = "zoidberg"):
    """ Sorts a list of numbers using an in-place implementation of quicksort
    
    This version of quicksort works similar to the naive implementation above but does not require the creation of additional 
    lists and thus uses less memory. Rather than place all the larger-than-pivot values into a new list, this function moves
    them to the left of the pivot by exchange. There are two indices in the inner loop, one beginning at the right and one
    at the left. These indices move in opposite directions and stop when the left index has reached a value larger than the
    pivot value and the right index has reached a value smaller than the pivot value. If and when this occurs, the two values
    at the two indices are swapped. This continues until the two indices collide. At this point, the list is partitioned into
    two sections: one with values larger than the pivot value, and one with values smaller than the pivot value. Note that it
    does not matter where the pivot value actually is, because it is now moved into place by swapping it with the value at the
    right index. This places it in between the two sections, which is its final place. 
    
    The function then makes a recursive call on the first half of the list (up to the pivot value, which is already properly
    placed) and again on the latter half of the list (from the pivot value to the end of the list). Thus, quicksort is usually
    referred to as a divide-and-conquer method as it breaks down a problem into smaller and smaller sub-problems until the entire
    problem is solved. 
    
    Notice the use of default parameters. When the function is called recursively, bounds for the sub-list it is to sort must
    be provided but most of the time, the client calling the method intends to sort the entire list. We want this to be the
    default case, so that the client does not need to include the latter two parameters when calling this function. However,
    we cannot assign the default value of upper to "len(file)-1" because "file" is not in scope until the actual body of the
    function. So we assign it a dummy value (why not Zoidberg?) and test for this dummy value in the body.
    
    Arguments:
    file -- a list of numbers to be sorted
    lower -- An inclusive lower bounds on the portion of the list to be sorted (default value 0)
    upper -- An inclusive upper bounds on the portion of the list to be sorted (default value (len(file)-1))
    
    """
    if lower == "zoidberg" : lower = 0                              #If the upper and lower limit parameters were not specified
    if upper == "zoidberg" : upper = len(file) -1                   #(and thus were assigned a default dummy value) set them to
                                                                    #include the entire list
    
    if upper-lower > 0:                                             #Only proceed to sort if lower and upper define the limits
                                                                    #of a proper list (i.e. upper is larger than lower)

        pivot_index = (lower+upper)//2                              #Assign a pivot index and value. This pivot will form the
        pivot_value = file[pivot_index]                             #basis for the sorting that occurs. Values larger than the
                                                                    #pivot will be placed on the right of it, while lesser values    
                                                                    #will be placed on the left.

        l , h = lower, upper                                        #l and h are the two indices we will use to scan the list in
                                                                    #the inner loop. They will start off at the ends of the list
                
        while h > l:                                                #As long as the indices have not crossed yet
            
            while file[l] <= pivot_value and h > l:                 #Keep increasing l until it encounters a value that is larger
                l += 1                                              #than the pivot value, making sure that the indices have not
                                                                    #crossed before incrementing l (even though this is checked for
                                                                    #in the outer loop, l and h are both changing in the inner loops
                                                                    #so this condition could become false at any point)
         
            while file[h] > pivot_value and h >= l:                 #Keep decreasing h until it encounters a value that is smaller
                h -= 1                                              #than the pivot value, making sure again that the indices do 
                                                                    #not cross before decrementing h. 
                                                           
                
            if h > l:                                               #Check one final time that the indices have not crossed. If they
                file[l], file[h] = file[h], file[l]                 #have not, perform a swap. Note that at this point in the loop,
                                                                    # if h and l have not crossed, h points to a value smaller than
                                                                    #the pivot and l points to a value larger than the pivot. Because
                                                                    #h and l are on the right and left sides of the list, the values
                                                                    #must be out of order and require swapping. The goal is to rearrange
                                                                    #the values until there is some spot such that every value to the
                                                                    #left is lesser than the pivot value and every value to the right is
                                                                    #is greater. The ordering within each section of the list is not
                                                                    #important now, and will be taken care of by the recursive calls.
                
        file[pivot_index],file[h] = file[h],file[pivot_index]       #Put the pivot value in its place. After the loops run, the pointer
                                                                    #H is sitting between the two partitions of the list and should be
                                                                    #swapped with the pivot

        quick_sort_inplace(file, lower, h-1)                        #Make a recursive call to do this to the first partition
       
        quick_sort_inplace(file, h+1, upper)                        #Make a recursive call to do this to the latter partition

              


