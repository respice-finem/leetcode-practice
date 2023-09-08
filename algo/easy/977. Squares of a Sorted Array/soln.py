def sortedSquares(nums: List[int]) -> List[int]:
    """
    (Suboptimal: Timewise)

    Time Complexity: O(nlogn)
    Space Complexity: O(1)

    TODO:
    1. Square each element in nums
    2. Sort the array and return
    """
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
    return sorted(nums)

    """
    Two Pointer Approach
    (Optimal)

    Time Complexity: O(n)
    Space Complexity: O(n)
    NOTE: Sometimes it's better to see which one is the larger rather than smaller
    TODO:
    1. Square all the elements
    2. Setup two pointers and compare which number is larger
    3. Append the larger one and move the pointer either rightwards on leftwards depending which one is larger
    4. Return the reversed output
    """
    nums = [num ** 2 for num in nums]
    left, right = 0, len(nums) -1
    output = []
    while left <= right:
        if nums[left] >= nums[right]:
            output.append(nums[left])
            left += 1
        else:
            output.append(nums[right])
            right -= 1
    return output[::-1]