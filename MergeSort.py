def MergeSort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr) // 2]
        right_arr = arr[len(arr) // 2:]

        MergeSort(left_arr)
        MergeSort(right_arr)

        # Merge Step

        i = 0 # Track left_arr
        j = 0 # Track right_arr
        k = 0 # Track merged arr
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
                
            else:
                arr[k] = right_arr[j]
                j += 1
            
            k += 1

        # Incase leftover values

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
        
# Test

test_arr = [2,5,8,3,1,3,4,90,10000]
MergeSort(test_arr)
print(test_arr)
