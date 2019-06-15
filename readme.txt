File: sortCompare.py
Author: Samy Masadi

This program will demonstrate a comparison of various sorting methods on lists of 
different types and lengths. The intended use of the program is to compare the times
taken by the different sorting methods in order to better understand each method's
strengths and weaknesses.

The comparisons available:
1. Quick Sort vs. Merge Sort vs. Bubble Sort
2. Quick Sort vs. Quick Sort Variation
3. Merge Sort vs. Merge Sort Variation

Information on the Sorts:
Quick Sort: Attempts a divide and conquer approach that partitions the list based
	on a pivot value. The pivot is always selected from the first element in the list. 
	Elements less than or equal to the pivot are placed in one partition, while 
	elements greater than the pivot are place in the other. Quick Sort is then 
	called recursively on each partition.
Merge Sort: Another divide and conquer method that splits the list into equal halves.
	Merge Sort is called recursively on each half. The halves are then merged and
	sorted in ascending order.
Bubble Sort: A brute force method that loops through the list, selects the largest element
	on each pass, and moves the element to the end of the list.
Quick Sort Variation: This performs a quick sort except the pivot is select from the median
	value of three elements.
Merge Sort Variation: This performs a merge sort except halves that are 10 elements or less
	in length are sorted with an insertion sort. The insertion sort takes the first
	element in the unsorted portion of the list then inserts it in the proper position
	in the sorted portion of the list.

The list types available:
1. In-Order Length 10
2. Reverse Length 10
3. Random Length 10
4. In-Order Length 50
5. Reverse Length 50
6. Random Length 50

Required for use: Python 3.0 or later version must be installed.

To run in Windows command line:
Double-click the sortCompare.py file or navigate to the file's directory and
enter "sortCompare.py".

To run in IDLE Python Shell:
1. Run IDLE.
2. Click "File" then "Open".
3. Navigate to "sortCompare.py" then click "Open".
4. To run the program, Press F5 on the keyboard, or click "Run" then "Run Module".

Instructions for use, once running:
1. Enter a number to select one of the comparison options in the top menu:
	- Enter "1" for Quick Sort vs. Merge Sort vs. Bubble Sort
	- Enter "2" for Quick Sort vs. Quick Sort Variation
	- Enter "3" for Merge Sort vs. Merge Sort Variation
	- Enter "0" to exit.
2. Enter a number to select one of the list options in the sub menu:
	- Enter "1" for In-Order Length 10
	- Enter "2" for Reverse Length 10
	- Enter "3" for Random Length 10
	- Enter "4" for In-Order Length 50
	- Enter "5" for Reverse Length 50
	- Enter "6" for Random Length 50
	- Enter "0" to go back to the top menu