#INSERTION SORTING ALGORITHM
To sort an array of size N in ascending order iterate over the array and compare the current element (key) to its predecessor,
if the key element is smaller than its predecessor, compare it to the elements before.
Move the greater elements one position up to make space for the swapped element.

#WHY NEED INSERTION SORT

- Its simplicity and low overhead make it efficient when the number of elements to be sorted is relatively small.
- Insertion Sort has an adaptive nature, meaning that its performance improves when dealing with nearly sorted or partially sorted data. In such cases, it can achieve better-than-O(n^2) time complexity.
- Insertion Sort is an in-place sorting algorithm, meaning it doesn't require additional memory to store temporary data structures. It operates directly on the input array, making it memory-efficient.

#PSEUDOCODE HERE 

InsertionSort(arr)
len_arr = length of arr

for i from 1 to len_arr - 1 do
a = arr[i]
j = i - 1

    while j >= 0 and a < arr[j] do
      arr[j + 1] = arr[j]
      j = j - 1

    arr[j + 1] = a

main()
print("Enter the array:")
arr = split input string into an array of integers

print("Sorted array:")
InsertionSort(arr)

for i from 0 to length of arr - 1 do
print arr[i] with a space, end=" "
