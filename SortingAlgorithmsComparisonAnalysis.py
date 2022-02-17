""" Authors:
    Sai Prasad Palli - 801254453
    Shourya Reddy Katkam - 801255429 """

# Comparison-based Sorting Algorithm

import random
import sys
sys.setrecursionlimit(10**6)
from time import time
import matplotlib.pyplot as myPlot

# Implementing INSERTION SORT
def insertion_sort(list_of_elements):
 for x in range(1, len(list_of_elements)):
    key = list_of_elements[x]
    y = x-1
    while y >= 0 and list_of_elements[y] > key:
        list_of_elements[y+1] = list_of_elements[y]
        y = y - 1
    list_of_elements[y+1] = key

#Implementing MERGE SORT
# Merge Function
def Merge(list_of_elements, l, m, h):
 n1 = m-l+1
 n2 = h-m
 left = [0]*n1
 right = [0]*n2
 for x in range(n1):
    left[x] = list_of_elements[x+l]
 for x in range(n2):
    right[x] = list_of_elements[x+1+m]
 x = 0
 y = 0
 z = l
 while x < n1 and y < n2:
    if left[x] < right[y]:
        list_of_elements[z] = left[x];
        x = x + 1
    else:
        list_of_elements[z] = right[y]
        y = y + 1
    z += 1
 while x < n1:
    list_of_elements[z] = left[x]
    z = z + 1
    x = x + 1
 while y < n2:
    list_of_elements[z] = right[y]
    z = z + 1
    y = y + 1

# Implementing MERGE SORT
def merge_sort(list_of_elements, l, h):
 if l < h:
    m = (l+h)//2
    merge_sort(list_of_elements, l, m)
    merge_sort(list_of_elements, m+1, h)
    Merge(list_of_elements, l, m, h)

# Implementing HEAP SORT
# heapify function
def heapify(list_of_elements, x, n):
    l = 2*x + 1
    h = 2*x + 2
    y = x
    if (l < n) and (list_of_elements[l] > list_of_elements[x]):
        x = l
    if (h < n) and (list_of_elements[h] > list_of_elements[x]):
        x = h
    if x != y:
        list_of_elements[x], list_of_elements[y] = list_of_elements[y], list_of_elements[x]
        heapify(list_of_elements, x, n)

# Implementing HEAP SORT
def heap_sort(list_of_elements, l, h):
    n = len(list_of_elements)
    for x in range(n//2, -1, -1):
        heapify(list_of_elements, x, n)
    for x in range(n-1, 0, -1):
        list_of_elements[x], list_of_elements[0] = list_of_elements[0], list_of_elements[x]
        heapify(list_of_elements, 0, x)

# Implementing QUICK SORT
# quick sort partition function
def quick_sort_partition(list_of_elements, l, h):
    pivot = list_of_elements[l]
    x = l+1
    y = h
    while x < y:
        while x <= h and list_of_elements[x] <= pivot:
            x += 1
        while y >= 0 and list_of_elements[y] > pivot:
            y -= 1
        if x < y:
            temp = list_of_elements[x]
            list_of_elements[x] = list_of_elements[y]
            list_of_elements[y] = temp
        else:
            temp = list_of_elements[y]
            list_of_elements[y] = pivot
            list_of_elements[l] = temp
    return y

# Implementing QUICK SORT
def quick_sort(list_of_elements, l, h):
    if l < h:
        pi = quick_sort_partition(list_of_elements, l, h)
        quick_sort(list_of_elements, l, pi-1)
        quick_sort(list_of_elements, pi+1, h)

# Implementing MODIFIED QUICK SORT
# Median function (Use median-of-three as pivot.)
def Median(list_of_elements, low, high, mid):
    i = list_of_elements[low]
    j = list_of_elements[mid]
    k = list_of_elements[high]
    if i <= j <= k:
        return j, mid
    if k <= j <= i:
        return j, mid
    if i <= k <= j:
        return k, high
    if j <= k <= i:
        return k, high
    return i, low

# modified quick sort partition function
def modified_quick_sort_Partition(list_of_elements, l, h):
    pivot, idx = Median(list_of_elements, l, h, (l+h)//2)
    x = l+1
    y = h
    while x < y:
        while x <= h and list_of_elements[x] <= pivot:
            x += 1
        while y >= 0 and list_of_elements[y] > pivot:
            y -= 1
        if x < y:
            temp = list_of_elements[x]
            list_of_elements[x] = list_of_elements[y]
            list_of_elements[y] = temp

        else:
            temp = list_of_elements[y]
            list_of_elements[y] = pivot
            list_of_elements[idx] = temp
    return y

#Implementing MODIFIED QUICK SORT
def modified_quick_sort(list_of_elements, l, h):
    if l < h:
        if (h-l) >= 8:  #For small sub-problem of size <= 8 , you must use insertion sort.
            pi = modified_quick_sort_Partition(list_of_elements, l, h)
            quick_sort(list_of_elements, l, pi-1)
            quick_sort(list_of_elements, pi+1, h)
    else:
        for x in range(l+1, h+1):
            key = list_of_elements[x]
            y = x-1
            while y >= l and list_of_elements[y] > key:
                list_of_elements[y+1] = list_of_elements[y]
                y = y - 1
            list_of_elements[y+1] = key

# Variables declarations

# declaring the array sizes of the different inputs sizes  (e.g. n = 1000, 2000, 4K, 5K, 10K, 20K, 40K, 50K, 60K, 80K, 100K).

# sizes = [x for x in range(0,100000,1000)]
sizes = [0,1000,2000,4000,5000]
# Algorithms time declaration
insertion_sort_time = {}
merge_sort_time = {}
heap_sort_time = {}
quick_sort_time = {}
modified_quick_sort_time = {}

# Sorted Algorithms time declaration (special case)
insertion_sort_time_sorted = {}
merge_sort_time_sorted = {}
heap_sort_time_sorted = {}
quick_sort_time_sorted = {}
modified_quick_sort_time_sorted = {}

# reverse sorted Algorithms time declaration (special case)
insertion_sort_time_reverse = {}
merge_sort_time_reverse = {}
heap_sort_time_reverse = {}
quick_sort_time_reverse = {}
modified_quick_sort_time_reverse = {}


for x in sizes:         # executing each sizes from the given instructions
    list_of_elements = []
    for xyz in range(x):
        list_of_elements.append(random.randint(1, 1000)) # generating random values in the range of 1 to 1000
    print(list_of_elements)
    randomArray = list_of_elements
    sortedArray = sorted(list_of_elements)
    reverseSortedArray = sorted(list_of_elements)[-1::-1]

    t = time()
    insertion_sort(randomArray)
    t = time()-t
    insertion_sort_time[x] = t

    t = time()
    insertion_sort(sortedArray)
    t = time()-t
    insertion_sort_time_sorted[x] = t

    t = time()
    insertion_sort(reverseSortedArray)
    t = time()-t
    insertion_sort_time_reverse[x] = t

    t = time()
    merge_sort(randomArray, 0, len(randomArray)-1)
    t = time()-t
    merge_sort_time[x] = t

    t = time()
    merge_sort(sortedArray, 0, len(randomArray)-1)
    t = time()-t
    merge_sort_time_sorted[x] = t

    t = time()
    merge_sort(reverseSortedArray, 0, len(randomArray)-1)
    t = time()-t
    merge_sort_time_reverse[x] = t

    t = time()
    heap_sort(randomArray, 0, len(randomArray)-1)
    t = time()-t
    heap_sort_time[x] = t

    t = time()
    heap_sort(sortedArray, 0, len(randomArray)-1)
    t = time()-t
    heap_sort_time_sorted[x] = t

    t = time()
    heap_sort(reverseSortedArray, 0, len(randomArray)-1)
    t = time()-t
    heap_sort_time_reverse[x] = t


    randomArray = list_of_elements
    t = time()
    quick_sort(randomArray, 0, len(randomArray)-1)
    t = time()-t
    quick_sort_time[x] = t

    t = time()
    quick_sort(sortedArray, 0, len(randomArray)-1)
    t = time()-t
    quick_sort_time_sorted[x] = t

    t = time()
    quick_sort(reverseSortedArray, 0, len(randomArray)-1)
    t = time()-t
    quick_sort_time_reverse[x] = t

    randomArray = list_of_elements
    t = time()
    modified_quick_sort(randomArray, 0, len(randomArray)-1)
    t = time()-t
    modified_quick_sort_time[x] = t

    t = time()
    modified_quick_sort(sortedArray, 0, len(randomArray)-1)
    t = time()-t
    modified_quick_sort_time_sorted[x] = t

    t = time()
    modified_quick_sort(reverseSortedArray, 0, len(randomArray)-1)
    t = time()-t
    modified_quick_sort_time_reverse[x] = t

print("Random Generated Values")

print("Insertion Sort")
for i in insertion_sort_time.items():
    print("%s\t%s"%(i[0], i[1]))

print("Merge Sort")
for i in merge_sort_time.items():
    print("%s\t%s"%(i[0], i[1]))

print("Heap Sort")
for i in heap_sort_time.items():
    print("%s\t%s"%(i[0], i[1]))

print("Quick Sort")
for i in quick_sort_time.items():
    print("%s\t%s"%(i[0], i[1]))

print("Modified Quick Sort")
for i in modified_quick_sort_time.items():
    print("%s\t%s"%(i[0], i[1]))

print("\n")

print("Random Generated Values Sorted")

print("Insertion Sort")
for i in insertion_sort_time_sorted.items():
    print("%s\t%s"%(i[0], i[1]))

print("Merge Sort")
for i in merge_sort_time_sorted.items():
    print("%s\t%s"%(i[0], i[1]))

print("Heap Sort")
for i in heap_sort_time_sorted.items():
    print("%s\t%s"%(i[0], i[1]))

print("Quick Sort")
for i in quick_sort_time_sorted.items():
    print("%s\t%s"%(i[0], i[1]))

print("Modified Quick Sort")
for i in modified_quick_sort_time_sorted.items():
    print("%s\t%s"%(i[0], i[1]))

print("\n")

print("Random Generated Values Reverse Sorted")

print("Insertion Sort")
for i in insertion_sort_time_reverse.items():
    print("%s\t%s"%(i[0], i[1]))

print("Merge Sort")
for i in merge_sort_time_reverse.items():
    print("%s\t%s"%(i[0], i[1]))

print("Heap Sort")
for i in heap_sort_time_reverse.items():
    print("%s\t%s"%(i[0], i[1]))

print("Quick Sort")
for i in quick_sort_time_reverse.items():
    print("%s\t%s"%(i[0], i[1]))

print("Modified Quick Sort")
for i in modified_quick_sort_time_reverse.items():
    print("%s\t%s"%(i[0], i[1]))

print("\n")

# Graph plotting for all algorithms time.
myPlot.plot(sizes, list(insertion_sort_time.values()), "r",label = "Insertion Sort" )
myPlot.plot(sizes, list(merge_sort_time.values()), "g", label = "Merge Sort" )
myPlot.plot(sizes, list(heap_sort_time.values()), "b",label="Heap Sort")
myPlot.plot(sizes, list(quick_sort_time.values()), "y",label = "Quick Sort")
myPlot.plot(sizes, list(modified_quick_sort_time.values()), "m",label="Modified Quick Sort")
myPlot.title("randomly generated Numbers")
myPlot.xlabel("Number of elements")
myPlot.ylabel("Time taken by each Algorithms")
myPlot.legend()
myPlot.show()

# Graph plotting for all sorted algorithms time.
myPlot.plot(sizes, list(insertion_sort_time_sorted.values()), "r",label = "Insertion Sort")
myPlot.plot(sizes, list(merge_sort_time_sorted.values()), "g",label = "Merge Sort")
myPlot.plot(sizes, list(heap_sort_time_sorted.values()), "b",label = "Heap Sort")
myPlot.plot(sizes, list(quick_sort_time_sorted.values()), "y",label = "Quick Sort")
myPlot.plot(sizes, list(modified_quick_sort_time_sorted.values()), "m",label = "Modified Quick Sort")
myPlot.title("Sorted Numbers")
myPlot.xlabel("Number of elements")
myPlot.ylabel("Time taken by each Algorithms")
myPlot.legend()
myPlot.show()

# Graph plotting for all reverse sorted algorithms time.
myPlot.plot(sizes, list(insertion_sort_time_reverse.values()), "r",label = "Insertion Sort")
myPlot.plot(sizes, list(merge_sort_time_reverse.values()), "g",label = "Merge Sort")
myPlot.plot(sizes, list(heap_sort_time_reverse.values()), "b",label = "Heap Sort")
myPlot.plot(sizes, list(quick_sort_time_reverse.values()), "y",label = "Quick Sort")
myPlot.plot(sizes, list(modified_quick_sort_time_reverse.values()), "m",label = "Modified Quick Sort")
myPlot.title("Sorted Numbers in reverse order")
myPlot.xlabel("Number of elements")
myPlot.ylabel("Time taken by each Algorithms")
myPlot.legend()
myPlot.show()