def search(nums: List[int], target: int) -> int:
    """
    (More to be explored on variants of binary search)
    Time Complexity: O(log n)
    Space Complexity: O(1)

    TODO:
    1. Setup left and right
    2. Stopping condition is we overlap the left and right
    3. While valid, get the mid
    4. Adjust end if mid number is greater than target
    4.5 We -1 from end boundary (right) since we do not need to include it anymore
    5. Adjust start if mid number is less than target
    5.5 We + 1 on start boundary (left) since we do not need to include it anymore
    6. Return if mid == target
    7. If stopping condition met, we return -1
    """
    left = 0
    right = len(nums) - 1
    

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    return -1