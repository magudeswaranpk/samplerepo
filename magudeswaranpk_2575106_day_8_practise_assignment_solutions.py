# -*- coding: utf-8 -*-
"""MagudeswaranPK_2575106_day_8_practise_assignment_solutions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rTRLGYok8feH51iDwyRsRwwNzT2mqjAH

# 3. Write a Python program for sorting a list of elements using selection sort algorithm:

a. Assume two lists: Sorted list- Initially empty and Unsorted List-Given input list.

b. In the first iteration, find the smallest element in the unsorted list and place it in the sorted list.

c. In the second iteration, find the smallest element in the unsorted list and place it in the correct position by comparing with the element in the sorted list.

d. In the third iteration, again find the smallest element in the unsorted list and place it in the correct position by comparing with the elements in the sorted list.

e. This process continues till the unsorted list becomes empty.

f. Display the sorted list.
"""

def selection_sort(input_list):
    sorted_list = []

    while input_list:
        min_element = min(input_list)
        sorted_list.append(min_element)
        input_list.remove(min_element)

    return sorted_list

num_elements = int(input("Enter the number of elements: "))

input_list = []

for i in range(num_elements):
    element = int(input(f"Enter element {i + 1}: "))
    input_list.append(element)

sorted_result = selection_sort(input_list)

print("Sorted List:", sorted_result)

"""# 4.Write a Python program for sorting a list of elements using insertion sort algorithm:

a. Assume two lists: Sorted list- Initially empty and Unsorted List-Given input list.

b. In the first iteration, take the first element in the unsorted list and insert it in Sorted list.

c. In the second iteration, take the second element in the given list and compare with the element in the sorted sub list and place it in the correct position.

d. In the third iteration, take the third element in the given list and compare with the elements in the sorted sub list and place the elements in the correct position.

e. This process continues until the last element is inserted in the sorted sub list.

f. Display the sorted elements.
"""

def insertion_sort(input_list):
    for i in range(1, len(input_list)):
        current_element = input_list[i]
        j = i - 1

        while j >= 0 and current_element < input_list[j]:
            input_list[j + 1] = input_list[j]
            j -= 1

        input_list[j + 1] = current_element

num_elements = int(input("Enter the number of elements: "))

input_list = []

for i in range(num_elements):
    element = int(input(f"Enter element {i + 1}: "))
    input_list.append(element)

insertion_sort(input_list)
print("Sorted List:", input_list)

"""# 5. Write a Python program that performs merge sort on a list of numbers:

    a. Divide: If the given array has zero or one element, return.

    1. Otherwise

ii. Divide the input list in to two halves each containing half of the elements. i.e. left half and right half.

b. Conquer: Recursively sort the two lists (left half and right half).

    a. Call the merge sort on left half.

    b. Call the merge sort on right half.

C. Combine: Combine the elements back in the input list by merging the two sorted lists into a sorted sequence.
"""

def merge_sort(input_list):
    if len(input_list) <= 1:
        return

    mid = len(input_list) // 2
    left_half = input_list[:mid]
    right_half = input_list[mid:]

    merge_sort(left_half)
    merge_sort(right_half)

    merge(input_list, left_half, right_half)

def merge(input_list, left_half, right_half):
    i = j = k = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            input_list[k] = left_half[i]
            i += 1
        else:
            input_list[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        input_list[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        input_list[k] = right_half[j]
        j += 1
        k += 1

num_elements = int(input("Enter the number of elements: "))

input_list = []

for i in range(num_elements):
    element = int(input(f"Enter element {i + 1}: "))
    input_list.append(element)

merge_sort(input_list)
print("Sorted List:", input_list)