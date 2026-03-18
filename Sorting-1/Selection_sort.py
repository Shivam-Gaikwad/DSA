def selection_sort(arr):
    n = len(arr)

    for i in range (n-1):    # will revert through al element of the array
        min_ele = i    # marks first element as the lowest element

        for j in range (i+1, n):     # From 2nd element to n th element
            if arr[j] < arr[min_ele] :  # if element is founded less
                min_ele = j             # then change it with the min_ele

        arr[i] , arr[min_ele] = arr[min_ele] , arr[i]        # swap the min element with the first element of the unsorted array
    print('After selection sort')
    print(arr)

arr = [13,34,45,78,45,24,9]

selection_sort(arr)
