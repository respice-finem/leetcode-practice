def majorityElement(nums: List[int]) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. Create dictionary of nums and count elements
    2. Return if value is more than n / 2 times
    """
    e_dict = {}
    for num in nums:
        if num not in e_dict:
            e_dict[num] = 1
        else:
            e_dict[num] += 1
    
    for key in e_dict:
        if e_dict[key] > int(len(nums)/2):
            return key
    
    """
    (Optimal)
    --> Only works if it our majority is above n / 2
    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
    1. We iterate and store our current candidate at the start. If we see the same we increase the count. Else we minus the count
    2. Once we hit 0, we switch to current candidate and perform same as 1
    """
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate