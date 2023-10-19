def twoSum(numbers: List[int], target: int) -> List[int]:
    """
    Time Complexity: O(nlogn)
    Space Complexity: O(1)

    TODO:
    1. We start from the first index and perform a binary search
    2. We reduce the search space i.e. start from the right
    """
    def bin_search(start, end, target):
        left, right = start, end
        while left <= right:
            mid = (left + right) // 2
            if numbers[mid] == target:
                return mid
            elif numbers[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
    
    for i in range(len(numbers)):
        temp = target - numbers[i]
        index = bin_search(i + 1, len(numbers)-1, temp)
        if index != -1:
            return [i+1, index+1]

    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
    1. We basically start with left and right. Using the the left, we shift the right till we see the difference is greater than or equal to the value
    2. We then return the two index
    """
    left, right = 0, len(numbers)-1

    while True:
        temp = target - numbers[left]
        while numbers[right] > temp:
            right -= 1
        if numbers[right] == temp:
            return [left+1,right+1]
        left += 1