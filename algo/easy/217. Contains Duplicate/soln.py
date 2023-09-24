def containsDuplicate(nums: List[int]) -> bool:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. Put in dictionary
    2. If appear more less than 2, return False
    """
    num_dict = {}
    
    for num in nums:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1

        if num_dict[num] >= 2:
            return True

    return False

    """
    Time Complexity: O(nlogn)
    Space Complexity: O(1)

    TODO:
    1. We sort the array
    2. If the next element is the same, we return True
    """
    nums = sorted(nums)

    for i in range(1, len(nums)):
        if nums[i-1] == nums[i]:
            return True

    return False

    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. Create set and minus the len
    2. Return if the difference is not 0
    """
    unique = set(nums)
    return len(unique) - len(nums) != 0