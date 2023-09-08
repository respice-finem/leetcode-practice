def sortColors(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    """
    NOTE: Important thing that was forgotten again while doing
    We have to move the pointer when it is 0, because we need to handle
    what was swapped back else we would miss it if we move forward immediately
    after swapping with 2. (Sorting question that is good to know.)

    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
    1. We setup three pointers, left, right, move
    2. Left and right sets where we place our 0s and 2s
    3. Everytime we encounter a 0 or 2 place them in the opposite end
    4. Once our move exceeds the right, we should stop searching since it has already been arranged
    """
    left = move = 0
    right = len(nums) - 1

    while move <= right:
        if nums[move] == 2:
            nums[right], nums[move] = nums[move], nums[right]
            right -= 1
        elif nums[move] == 0:
            nums[left], nums[move] = nums[move], nums[left]
            left += 1
            move += 1
        else:
            move += 1