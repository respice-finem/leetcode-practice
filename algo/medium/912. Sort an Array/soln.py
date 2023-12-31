def sortArray(nums: List[int]) -> List[int]:
    """
    Time Complexity: O(nlogn)
    Space Complexity: O(n)
    NOTE: This approach is meant to reuse space instead of creating extra space for the output array
    -- Neetcode approach for this
    TODO:
    1. We do merge sort
    """
    def merge(arr, l, m, r):
        left, right = arr[l:m+1], arr[m+1:r+1]
        i, j, k = l, 0, 0

        while j < len(left) and k < len(right):
            if left[j] <= right[k]:
                arr[i] = left[j]
                j += 1
            else:
                arr[i] = right[k]
                k += 1
            i += 1

        while j < len(left):
            nums[i] = left[j]
            i += 1
            j += 1

        while k < len(right):
            nums[i] = right[k]
            k += 1
            i += 1

    def mergeSort(arr, l, r):
        if l == r:
            return arr
        m  = (l + r) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)
        return arr
    
    return mergeSort(nums, 0, len(nums)-1)  