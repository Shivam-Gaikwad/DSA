def bubble_sort(arr):
    n = len(arr)
    for i in range(0,n-1):
        for j in range(0 ,n-1-i):
            if arr[j] > arr[j+1] :
                arr[j] , arr[j+1] = arr[j+1], arr[j]

    return f"After sort array is: {arr}"

arr = [12,3,4,5,6,7,8]

sorted_array = bubble_sort(arr)
print(sorted_array)