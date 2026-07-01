def insertion_sort(arr):
    n = len(arr)
    for i in range(0 , n):
        j = i
        while j>0 and arr[j-1] > arr[j]:
            arr[j-1] ,arr[j] = arr[j] , arr[j-1]
            j -=1

    return f"Array after sorting is {arr}"

arr = [3,5,7,23,1,2,6,6,8]
sorted_array = insertion_sort(arr)
print(sorted_array)