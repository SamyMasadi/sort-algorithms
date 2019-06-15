######################################################################################
#
#
#  Name: Samy Masadi
#  Date: March 1, 2019
#  Due Date: March 1, 2019
#
#  This project compares quicksort, mergesort and bubblesort.  The steps
#  are as follows:
#    1) write/test the partition routine for quicksort. (20 points)  The rest of the code is given.
#    2) write/test the merging part of the mergesort. (20 points) The rest of the code is given.
#    3) write/test bubblesort. (10 points) No code is given.
#    4) compare the sorts using lists of 10 and 50 items (in-order, reverse order
#       and random (hard coded).  Be sure
#       to print out the initial and sorted arrays so I can see that your module
#       sorted properly. (10 points)
#    5) In your report (using LaTeX), create a table 1 that shows the times in seconds of the
#       lists (rows) and sorts (columns). (10 points)
#    6) In your report, create a table 2 that shows the order of growth in Big O
#       notation for time and space of Quicksort, Mergesort and Bubblesort (Best case,
#       worst case and average case) (5 points)
#    6) write/test a variation on quicksort (vqS) that makes the following
#       improvements:
#         chooses pivot by taking a small sample size (3 items) and using
#         median for pivot. (10 points)
#    7) write/test a variation on mergesort (vmS) that makes the following
#        improvement:
#         Use insertion sort for small arrays (10 items or less). (10 points)
#    8) run your new modules on your stored lists and add your findings to a
#       table 3 in your report.  (10 points)
#    9) Your report should have at least the following sections:
#        Summary of Findings
#        Methodology (what did you do?)
#        Your tables and graphs
#     10) Upload your code, a screenshot of the run of your code, and your report in .pdf format
# 
#
####################################################################################
import time
import random
from statistics import median

### Function Definitions ###

# The function swaps any two elements within a list
# It takes three parameters:
# 1. arr: the list
# 2. smallIndex: the smaller index of element to swap
# 3. bigIndex: the larger index of element to swap
def swap(arr, smallIndex, bigIndex):
   temp = arr[bigIndex]
   arr[bigIndex] = arr[smallIndex]
   arr[smallIndex] = temp

# The function performs a quick sort on a list.
# array: the list to sort
def qS(array):
   qSHelp(array,0,len(array)-1)

# The function carries out a quick sort by partitioning a list
# then recursively calling itself on the inner partitions.
# It takes three parameters:
# 1. array: the list to sort
# 2. first: index marking the beginning of the partition
# 3. last: index marking the end of the part
def qSHelp(array,first,last):
   if first<last:

       pivot = partition(array,first,last)

       qSHelp(array,first,pivot-1)
       qSHelp(array,pivot+1,last)

# The function partitions a list segment:
# One partition contains values less than or equal to the pivot.
# The other partition contains values greater than the pivot.
# It takes three parameters:
# 1. array: the list to partition
# 2. first: the index marking the beginning of the portion to partition
# 3. last: the index marking the end of the portion to partition
# Return: The final index of the pivot.
def partition(array,first,last):
   pivotvalue = array[first]

   lSide = first+1
   rSide = last

   check = True
   while check:
      while lSide <= last and array[lSide] <= pivotvalue:
         lSide+=1
      while array[rSide] > pivotvalue:
         rSide-=1
      if lSide < rSide:
         swap(array, lSide, rSide)
      if rSide < lSide:
         check = False
   swap(array, first, rSide)

   return rSide

# The function merges two smaller lists into a larger list.
# It assumes the smaller lists are sorted and merges elements into larger list in ascending order.
# It takes three parameters:
# 1. arr: the larger list to merge into
# 2. left: the left small list
# 3. right: the right small list
def merge(arr, left, right):
   a = l = r = 0
   lenA = len(arr)
   lenL = len(left)
   lenR = len(right)
   while l < lenL and r < lenR and a < lenA:
      if right[r] < left[l]:
         arr[a] = right[r]
         r+=1
         a+=1
      else:
         arr[a] = left[l]
         l+=1
         a+=1
   # Expect one half to complete merging into arr first.
   # Merge remaining elements from the other half into arr.
   if l < lenL:
      while l < lenL and a < lenA:
         arr[a] = left[l]
         l+=1
         a+=1
   if r < lenR:
      while r < lenR and a < lenA:
         arr[a] = right[r]
         r+=1
         a+=1
   # If for some reason there are still elements that can't fit into arr:
   if l < lenL or r < lenR:
      print("Error: Ran out of room in main number list.")

# The function performs a merge sort on a list.
# It divides the list into two halves then recursively calls itself on the halves.
# It then calls merge function to perform merging and order of the halves.
# array: the list to sort
def mS(array):
 #   print("Splitting ",items)
    if len(array)>1:
        mid = len(array)//2
        lefthalf = array[:mid]
        righthalf = array[mid:]

        mS(lefthalf)
        mS(righthalf)
        merge(array, lefthalf, righthalf)

# The function performs a bubble sort on a list.
# Iterates through the list for the largest element
# then moves the element to the end of the list until a larger element is found.
# array: the list to sort
def bS(array):
   for i in range(0, len(array)):
      for j in range(0, len(array)-1-i):
         if array[j] > array[j+1]:
            swap(array, j, j+1)

# A variation of the quick sort function.
# array: the list to sort.
def vQS(array):
   qSHelp(array,0,len(array)-1)

# A variation of qSHelp function.
# The function carries out a quick sort by partitioning a list
# then recursively calling itself on the inner partitions.
# It takes three parameters:
# 1. array: the list to sort
# 2. first: index marking the beginning of the partition
# 3. last: index marking the end of the part
def vQSHelp(array,first,last):
   if first<last:

       pivot = vPartition(array,first,last)

       qSHelp(array,first,pivot-1)
       qSHelp(array,pivot+1,last)

# A variation of the partition function.
# Determine median value of the elements at first, middle, and last elements.
# Swap the median element with first element to make it the pivot.
# Call standard partition function to complete partition.
# The function takes three parameters:
# 1. array: the list to partition
# 2. first: the index marking the beginning of the portion to partition
# 3. last: the index marking the end of the portion to partition
# Return: The final index of the pivot.
def vPartition(array,first,last):
   if (last - first + 1) >= 3:      # Only find median if 3+ elements are available
      mid = (first + last) // 2     # Determine middle index                                
      med = median([array[first],array[mid],array[last]])
         # Determine median of values at first, mid, and last
      if array[first] != med:       # If first element is not already the median value...
         if array[mid] == med:      # ...swap median element with first element
            swap(array, first, mid)
         else:
            swap(array, first, last)
   return partition(array, first, last)

# The function performs an insertion sort on a list.
# The sort iterates through the values of unsorted elements in the array
# then determines where they should be inserted in the sorted portion.
# It takes one parameter:
# arr: the list to sort.
def iS(arr):
   for i in range(1, len(arr)):
      key = arr[i]
      j = i-1
      while j>=0 and arr[j]>key:
         arr[j+1] = arr[j]
         j-=1
      arr[j+1] = key

# The function performs a variation of merge sort on a list.
# For lists greater than ten in length, a merge sort is performed.
# For lists of length ten or less, an insertion sort is performed.
# It takes one parameter:
# array: the list to sort.
def vMS(array):
   if len(array)>10:
      mid = len(array)//2
      lefthalf = array[:mid]
      righthalf = array[mid:]
      vMS(lefthalf)
      vMS(righthalf)
      merge(array, lefthalf, righthalf)
   else:
      iS(array) 

# Call and compare different sorts:
# Quick Sort, Merge Sort, and Bubble Sort.
# Takes two parameters:
# 1. items: the list of integers to sort
# 2. order: the presorted order of the list (in-order, reverse, or random)
# The function prints the sorting results and the time taken by each method
def compareSorts(items, order):
   size = len(items)
   items_sort = items.copy()

   print("Sort Comparison:")
   print("Size: ", size)
   print("Order: ", order)
   print()
   print("Quick Sort")
   print("Unsorted:")
   print(items)
   start_time_quickSort = time.perf_counter()
   qS(items_sort)
   end_time_quickSort = time.perf_counter()
   print("Sorted:")
   print(items_sort)
   print("Quick Sort CPU time (seconds): "  +str(end_time_quickSort - start_time_quickSort))
   print()
   
   print("Merge Sort")
   print("Unsorted:")
   print(items)
   items_sort = items.copy()
   start_time_mSort = time.perf_counter()
   mS(items_sort)
   end_time_mSort = time.perf_counter()
   print("Sorted:")
   print(items_sort)
   print("Merge Sort CPU time (seconds): "  +str(end_time_mSort - start_time_mSort))
   print()
   
   print("Bubble Sort")
   print("Unsorted:")
   print(items)
   items_sort = items.copy()
   start_time_bSort = time.perf_counter()
   bS(items_sort)
   end_time_bSort = time.perf_counter()
   print("Sorted:")
   print(items_sort)
   print("Bubble Sort CPU time (seconds): "  +str(end_time_bSort - start_time_bSort))
   print()

# Call and compare different sorts:
# Quick Sort, Quick Sort Variation.
# Takes two parameters:
# 1. items: the list of integers to sort
# 2. order: the presorted order of the list (in-order, reverse, or random)
# The function prints the sorting results and the time taken by each method
def compareQS(items, order):
   size = len(items)
   items_sort = items.copy()

   print("Sort Comparison:")
   print("Size: ", size)
   print("Order: ", order)
   print()
   print("Quick Sort")
   print("Unsorted:")
   print(items)
   start_time_quickSort = time.perf_counter()
   qS(items_sort)
   end_time_quickSort = time.perf_counter()
   print("Sorted:")
   print(items_sort)
   print("Quick Sort CPU time (seconds): "  +str(end_time_quickSort - start_time_quickSort))
   print()

   print("Quick Sort Variation")
   print("Unsorted:")
   print(items)
   items_sort = items.copy()
   start_time_quickSort = time.perf_counter()
   vQS(items_sort)
   end_time_quickSort = time.perf_counter()
   print("Sorted:")
   print(items_sort)
   print("Quick Sort Variation CPU time (seconds): "  +str(end_time_quickSort - start_time_quickSort))
   print()

# Call and compare different sorts:
# Merge Sort, Merge Sort Variation.
# Takes two parameters:
# 1. items: the list of integers to sort
# 2. order: the presorted order of the list (in-order, reverse, or random)
# The function prints the sorting results and the time taken by each method
def compareMS(items, order):
   size = len(items)
   items_sort = items.copy()

   print("Sort Comparison:")
   print("Size: ", size)
   print("Order: ", order)
   print()
   print("Merge Sort")
   print("Unsorted:")
   print(items)
   start_time_quickSort = time.perf_counter()
   mS(items_sort)
   end_time_quickSort = time.perf_counter()
   print("Sorted:")
   print(items_sort)
   print("Merge Sort CPU time (seconds): "  +str(end_time_quickSort - start_time_quickSort))
   print()

   print("Merge Sort Variation")
   print("Unsorted:")
   print(items)
   items_sort = items.copy()
   start_time_quickSort = time.perf_counter()
   vMS(items_sort)
   end_time_quickSort = time.perf_counter()
   print("Sorted:")
   print(items_sort)
   print("Merge Sort Variation CPU time (seconds): "  +str(end_time_quickSort - start_time_quickSort))
   print()

def menu1():
   print("Select a sorting comparison.")
   print("1. Quick Sort vs. Merge Sort vs. Bubble Sort")
   print("2. Quick Sort vs. Quick Sort Variation")
   print("3. Merge Sort vs. Merge Sort Variation")
   print("0. Exit")
   print()

def menu2():
   print("Select an array type and length to sort.")
   print("1. In-Order Length 10")
   print("2. Reverse Order Length 10")
   print("3. Random Order Length 10")
   print("4. In-Order Length 50")
   print("5. Reverse Order Length 50")
   print("6. Random Order Length 50")
   print("0. Go Back")
   print()

### Main Program ###

# Hard-coded lists for sorting
in_order10 = [0,1,2,3,4,5,6,7,8,9]
reverse10 = [9,8,7,6,5,4,3,2,1,0]
random10 = [55,27,90,18,78,30,44,56,21,67]
in_order50 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]
reverse50 = [49,48,47,46,45,44,43,42,41,40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]
random50 = [88,15,66,53,59,14,26,52,23,36,15,17,13,62,50,90,69,46,6,63,40,1,45,47,79,20,55,1,73,57,8,43,52,14,87,23,60,19,47,6,41,91,92,67,7,25,46,61,12,1]

run = True

print("This program shows comparisons between sorting methods.")
print("Procedure:")
print("1. Choose the comparison type.")
print("2. Choose the list type and length.")
print()

while run:
   menu1()  # Top Menu
   input1 = input("Enter a number: ")
   if len(input1) == 1:
      try:
         select1 = (int)(input1)
         if select1 > 0 and select1 <= 3:
            run2 = True
            while run2:               
               menu2()  # Sub Menu
               input2 = input("Enter a number: ")
               if len(input2) == 1:
                  try:
                     select2 = (int)(input2)
                     if select2 > 0 and select2 <= 6:
                        if select1 == 1:     # Quick vs Merge vs Bubble
                           if select2 == 1:
                              compareSorts(in_order10, "In-Order")
                           if select2 == 2:
                              compareSorts(reverse10, "Reverse")
                           if select2 == 3:
                              compareSorts(random10, "Random")
                           if select2 == 4:
                              compareSorts(in_order50, "In-Order")
                           if select2 == 5:
                              compareSorts(reverse50, "Reverse")
                           if select2 == 6:
                              compareSorts(random50, "Random")
                        if select1 == 2:     # Quick Sorts
                           if select2 == 1:
                              compareQS(in_order10, "In-Order")
                           if select2 == 2:
                              compareQS(reverse10, "Reverse")
                           if select2 == 3:
                              compareQS(random10, "Random")
                           if select2 == 4:
                              compareQS(in_order50, "In-Order")
                           if select2 == 5:
                              compareQS(reverse50, "Reverse")
                           if select2 == 6:
                              compareQS(random50, "Random")
                        if select1 == 3:     # Merge Sorts
                           if select2 == 1:
                              compareMS(in_order10, "In-Order")
                           if select2 == 2:
                              compareMS(reverse10, "Reverse")
                           if select2 == 3:
                              compareMS(random10, "Random")
                           if select2 == 4:
                              compareMS(in_order50, "In-Order")
                           if select2 == 5:
                              compareMS(reverse50, "Reverse")
                           if select2 == 6:
                              compareMS(random50, "Random")                           
                     elif select2 == 0:
                        run2 = False   # Go back to top menu.
                     else:
                        print()
                        print("Error! Please enter a number between 0 and 6.")
                        print()
                  except ValueError:
                     print()
                     print("Error! Please enter a number as an integer.")
                     print()
               else:
                  print()
                  print("Error! Please enter a single digit number.")
                  print()
         elif select1 == 0:
            print()
            print("Good-bye!")
            run = False    # Exit Program
         else:
            print()
            print("Error! Please enter a number between 0 and 3.")
            print()
      except ValueError:
         print()
         print("Error! Please enter a number as an integer.")
         print()
   else:
      print()
      print("Error! Please enter a single digit number.")
      print()
   
