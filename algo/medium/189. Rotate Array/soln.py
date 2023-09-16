def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. Find the index that we want to rotate
    2. Cut it then append it to where we want
    3. Return the output
    """
    to_rotate = (len(nums) - k) % len(nums)
    temp = nums[to_rotate:] + nums[:to_rotate]
    for i in range(len(nums)):
        nums[i] = temp[i]

    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
    1. We can do an instant swap by identifying the location
    """
    to_rotate = (len(nums) - k) % len(nums)
    # Good to know that we can swap contiguous amounts of array
    nums[to_rotate:], nums[:to_rotate] = nums[:to_rotate], nums[to_rotate:]

    """
    (Cyclic Replacement)
    --> Answer from editorial
    NOTE: Important to understand swaps. Look more into this
    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
    1. We find the index that we need to swap next. Store the existing number and move on to the next until we hit the start again. For each element that we swap, we increment the count
    2. Repeat this until we hit all the elements
    """
    n = len(nums)
    k %= n

    start = count = 0
    while count < n:
        current, prev = start, nums[start]
        while True:
            next_idx = (current + k) % n
            nums[next_idx], prev = prev, nums[next_idx]
            current = next_idx
            count += 1
            if start == current:
                break
        start += 1