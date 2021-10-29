"""
Math 560
Project 1
Fall 2021

Partner 1: Fangting Ma (fm128)
Partner 2: Kaifeng Yu (ky99)
Date: 10/27/2021
"""

"""
swap

This function will swap the two values specified by their indices 
in the original list

INPUTS
list: the original list
i: the index of the first element need to swap
j: the index of the second element need to swap

OUTPUTS
there is no return, since it modifies the original list
"""
def swap(list, i, j):
    tmp = list[i]
    list[i] = list[j]
    list[j] = tmp

"""
find_min_index

This function will find the index of the minimum element in a list 
starting from a specific index, and returns the index of the minimum value

INPUTS
list: the list that needs to search
start_index: the first index to start searching

OUTPUTS
returns the index of the minimum value of the list
"""
def find_min_index(list, start_index):
    min_val = list[start_index]
    min_index = start_index
    for i in range(start_index, len(list)):
        if list[i] < min_val:
            min_val = list[i]
            min_index = i
    return min_index

"""
SelectionSort

This function will separate a list into sorted and unsorted parts 
by specifying the index of the first element of unsorted part,
iteratively find the minimum value of unsorted part,
then swap to the end of unsorted part, finally it will return the sorted list

INPUTS
listToSort: the original unsorted list

OUTPUTS
returns the sorted list
"""
def SelectionSort(listToSort):
    for unsort_index in range(len(listToSort)):
        min_index = find_min_index(listToSort, unsort_index)
        swap(listToSort, min_index, unsort_index)

    return listToSort

"""
InsertionSort

This function will separate a list into sorted and unsorted parts 
by specifying the index of the first element of unsorted part,
insert the first element of unsorted part into the sorted part,
and swaps with the former element until it is in the right position, 
finally it will return the sorted list

INPUTS
listToSort: the original unsorted list

OUTPUTS
returns the sorted list
"""
def InsertionSort(listToSort):
    for unsort_index in range(len(listToSort)):

        # swap the first element of the unsorted part backwards
        # into its right position
        for i in range(unsort_index - 1, -1, -1):
            if listToSort[i + 1] < listToSort[i]:
                swap(listToSort, i, i + 1)
            else:
                break;

    return listToSort

"""
BubbleSort

This function will repeatedly iterate a list and swap two adjacent elements 
until there is no swap any more, finally it will return the sorted list

INPUTS
listToSort: the original unsorted list

OUTPUTS
returns the sorted list
"""
def BubbleSort(listToSort):
    swapped = 1 # the dummy variable to indicate whether swap happens
    while swapped == 1:
        swapped = 0

        # iterate through the list
        # and swap two adjacent elements if they are in the wrong order
        for i in range(0, len(listToSort) - 1):
            if listToSort[i + 1] < listToSort[i]:
                swap(listToSort, i, i + 1)
                swapped = 1

    return listToSort

"""
merge:

This function will combine two sorted lists into a single list which 
is in an ascending order, and returns the combined list

INPUTS
list1: the first list to combine
list2: the second list to combine

OUTPUTS
returns the combined list
"""
def merge(list1, list2):
    i = 0
    j = 0
    combined_list = []

    # find the minimum value of two lists and append it into the combined list
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            combined_list.append(list1[i])
            i += 1
        else:
            combined_list.append(list2[j])
            j += 1

    # if there are values left in one list,
    # add them to the end of the combined list
    if i < len(list1):
        combined_list.extend(list1[i:])
    if j < len(list2):
        combined_list.extend(list2[j:])

    return combined_list

"""
MergeSort

This function will recursively split a list into two halves, 
and do merge sort on both halves, then merge two sorted halves,
finally it will return the sorted list

INPUTS
listToSort: the original unsorted list

OUTPUTS
returns the sorted list
"""
def MergeSort(listToSort):
    # if there is only one element in the list, it is already sorted
    if len(listToSort) == 1:
        return listToSort

    # split the list into two halves and recursively merge sort them,
    # then merge them into one list
    half_len = len(listToSort)//2
    sorted_list = merge(MergeSort(listToSort[:half_len]),
                        MergeSort(listToSort[half_len:]))

    # modify the original list according to the sorted list
    listToSort[0: len(listToSort)] = sorted_list[0: len(sorted_list)]
    return listToSort

"""
partition

This function will put all the elements that are smaller than 
the pivot value in the front of the list, and put all the elements 
that are larger than the pivot value in the back of the list, 
and it will return the index of pivot value when the partition ends

INPUTS
listToSort: the original unsorted list
i: the first index of part of the list to partition
j: the last index of part of the list to partition
pivot_index: the index of pivot value when the partition begins

OUTPUTS
returns the index of pivot value when the partition ends
"""
def partition(listToSort, i, j, pivot_index):
    pivot = listToSort[pivot_index]
    low_index = i
    up_index = j - 1

    # swap the two elements if the former is larger than the pivot
    # and the latter is smaller than the pivot,
    # until the low index and the high index meets in the middle of list
    while low_index < up_index:
        while listToSort[low_index] <= pivot and low_index < up_index:
            low_index += 1
        while listToSort[up_index] > pivot and low_index < up_index:
            up_index -= 1
        if low_index == up_index:
            break;
        swap(listToSort, low_index, up_index)
        low_index += 1
        up_index -= 1

    # if the end value where the low index and the high index meets
    # is smaller than the pivot, swap the end value and the pivot,
    # and update the pivot index
    if listToSort[low_index] <= listToSort[pivot_index]:
        swap(listToSort, pivot_index, low_index)
        pivot_index = low_index
    # if the end value is larger than the pivot value,
    # swap the end value and the element ahead of the pivot,
    # and update the pivot index
    else:
        swap(listToSort, pivot_index, low_index - 1)
        pivot_index = low_index - 1

    return pivot_index

"""
QuickSort

Sort a list with the call QuickSort(listToSort),
or additionally specify i and j.

This function will choose a pivot and do the partitioning, 
which means put all the elements that are smaller than the pivot value 
into the former part of the list, and put all the elements 
that are larger than the pivot value into the latter part of the list,
then recursively call the quick sort on both parts.
It will finally return the sorted list.

INPUTS
listToSort: the original unsorted list
i: the first index of the list to sort. (default value = 0)
j: the last index of the list to sort. (default value = None)

OUTPUTS
returns the sorted list
"""
def QuickSort(listToSort, i=0, j=None):
    # Set default value for j if None.
    if j == None:
        j = len(listToSort)

    # If the part only has one or less element, it does not need to sort
    if j - i <= 1:
        return listToSort

    # choose the pivot and do partitioning according to the pivot
    pivot_index = i # set the pivot index as the first element
    pivot_index = partition(listToSort, i, j, pivot_index)

    # do quick sort to the part that all the elements are larger than the pivot
    # and the part that all the elements are smaller than the pivot
    QuickSort(listToSort, i, pivot_index)
    QuickSort(listToSort, pivot_index + 1, j)

    return listToSort

"""
Importing the testing code after function defs to ensure same references.
"""
from project1tests import *

"""
Main function.
"""
if __name__ == "__main__":
    print('Testing Selection Sort')
    print()
    testingSuite(SelectionSort)
    print()
    print('Testing Insertion Sort')
    print()
    testingSuite(InsertionSort)
    print()
    print('Testing Bubble Sort')
    print()
    testingSuite(BubbleSort)
    print()
    print('Testing Merge Sort')
    print()
    testingSuite(MergeSort)
    print()
    print('Testing Quick Sort')
    print()
    testingSuite(QuickSort)
    print()
    print('UNSORTED measureTime')
    print()
    measureTime()
    print()
    print('SORTED measureTime')
    print()
    measureTime(True)
