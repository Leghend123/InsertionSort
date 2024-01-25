#Insertion sorting algorithm

#function to do the sorting
def insert_sort(arr):
    #lenght of the array..............
    len_arr = len(arr)
    #tranvese through all lenght of the array
    for i in range(len_arr):
        a = arr[i]
        j =i-1
        #loop through the array
        while j>=0 and a<arr[j]:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = a

if __name__ == "__main__":
    print("Enter the array:")
    arr= list(map(int,input().split()))
    print("sorted array")
    insert_sort(arr)
    for i in range(len(arr)):
       print("% d " % arr[i], end=" ")
       