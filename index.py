#Insertion sorting algorithm

def insert_sort(arr):
    #lenght of the array..............
    len_arr = len(arr)
    for i in range(len_arr):
        a = arr[i]
        j =i-1
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
       