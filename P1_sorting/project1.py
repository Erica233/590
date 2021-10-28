"""
Math 560
Project 1
Fall 2021

Partner 1: Fangting Ma (fm128)
Partner 2: Kaifeng Yu (ky99)
Date: 10/27/2021
"""
def swap(list, i, j):
    tmp = list[i]
    list[i] = list[j]
    list[j] = tmp

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
"""
def SelectionSort(listToSort):
    for unsort_index in range(len(listToSort)):
        min_index = find_min_index(listToSort, unsort_index)
        # print(min_index)
        swap(listToSort, min_index, unsort_index)
    return listToSort

"""
InsertionSort
"""
def InsertionSort(listToSort):
    for unsort_index in range(len(listToSort)):
        for i in range(unsort_index - 1, -1, -1):
            #print(i)
            if listToSort[i + 1] < listToSort[i]:
                swap(listToSort, i, i + 1)
            else:
                break;
    return listToSort

"""
BubbleSort
"""
def BubbleSort(listToSort):
    swapped = 1
    while swapped == 1:
        swapped = 0
        for i in range(0, len(listToSort) - 1):
            if listToSort[i + 1] < listToSort[i]:
                swap(listToSort, i, i + 1)
                swapped = 1
    return listToSort

def merge(list1, list2):
    combined_list = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        #print(i, j, combined_list)
        if (list1[i] <= list2[j]):
            combined_list.append(list1[i])
            i += 1
        else:
            combined_list.append(list2[j])
            j += 1
    if i < len(list1):
        combined_list.extend(list1[i:])
    if j < len(list2):
        combined_list.extend(list2[j:])
    return combined_list

def merge_sort(list):
    if len(list) == 1:
        return list
    half_len = len(list)//2
    return merge(merge_sort(list[:half_len]), merge_sort(list[half_len:]))

"""
MergeSort
"""
def MergeSort(listToSort):
    sorted_list = merge_sort(listToSort)
    listToSort[0: len(listToSort)] = sorted_list[0: len(sorted_list)]
    #print(sorted_list)
    return listToSort

"""
QuickSort

Sort a list with the call QuickSort(listToSort),
or additionally specify i and j.
"""
def QuickSort(listToSort, i=0, j=None):
    # Set default value for j if None.
    if j == None:
        j = len(listToSort)
    if j == 1:
        return listToSort
    pivot_index = i
    pivot = listToSort[pivot_index]
    low_index = i
    up_index = j-1
    while low_index <= up_index:
        while listToSort[low_index] <= pivot:
            low_index += 1
        while listToSort[up_index] > pivot:
            up_index -= 1
        swap(listToSort, low_index, up_index)
        low_index += 1
        up_index -= 1
        print(listToSort)
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
