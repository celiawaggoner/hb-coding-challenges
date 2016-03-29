#create a list of single digit numbers
lst = [4, 6, 7, 5, 9, 7, 8, 2, 3, 1]

#goal is to sort the list from highest to lowest with the best possible runtime

#define a function that takes in a list, a start point, and an end point
#use this function to establish a pivot --> move all numbers lower than
#the value at the pivot to the end of the list and numbers larger
#than the value at the pivot to the left of the pivot
def partition(lst, start, end):
    pivot = start
    for i in range(start+1, end+1):
        if lst[i] >= lst[start]:
            #increment pivot
            pivot += 1
            #swap list items
            lst[i], lst[pivot] = lst[pivot], lst[i]
    lst[pivot], lst[start] = lst[start], lst[pivot]
    return pivot


#use a recursive function to partition the list at all pivots
#until the list is sorted
def quicksort(lst, start=0, end=len(lst) - 1):
    #establish base case
    if start >= end:
        return
    pivot = partition(lst, start, end)
    quicksort(lst, start, pivot-1)
    quicksort(lst, pivot+1, end)

quicksort(lst)

print lst
# [9, 8, 7, 7, 6, 5, 4, 3, 2, 1]
# runtime on average is O(nlog(n)), and the worse case is O(n*n)
# I used quicksort over merge sort because it operates in place