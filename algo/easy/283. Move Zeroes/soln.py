def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    """
    One Pass
    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
    1. Set two pointers, left and right
    2. While left has not reached the end
    3. We continue swapping if left == 0 and right is num
    3. Else, we move forward
    """
    left, right = 0, 1

    while right < len(nums) and left < len(nums):
        if nums[left] == 0 and nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        elif nums[left] != 0:
            left += 1
        right += 1

    """
    Two Pass
    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
    1. Keep a counter, this is for us to replace our elements later
    2. First loop will replace the elements with our non-zero in order
    3. Second loop will replace the rest with zeros
    """
    count = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[count] = nums[i]
            count += 1
    for i in range(count, len(nums)):
        nums[i] = 0