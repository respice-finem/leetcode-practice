def missingNumber(nums: List[int]) -> int:
    """
    (Suboptimal: Spacewise)

    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. Setup range of n as a set
    2. Iterate through list of nums
    3. Remove those that are in the set
    4. Return what's left
    """
    distinct = set(range(0, len(nums)+1))
    for num in nums:
        distinct.remove(num)
    return list(distinct)[0]

    """
    (Optimal)
    --> Unique way of approaching finding distinct numbers
    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
    1. Generate number at start
    2. We are hoping to do a XOR chain, where the same terms will cancel out as (a + b) mod 2
    3. This would mean that we would want to do: A ^ (A ^ B) ^ (B ^ C) ==> (A ^ A) ^ (B ^ B) ^ C
    4. What's remaining would be one's that are left
    """
    missing = len(nums)
    for i in range(len(nums)):
        missing ^= i ^ nums[i]
    return missing

    """
    (Optimal)
    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
    1. Iterate through num against range nums
    2. Add the differences
    3. Return the absolute difference
    """
    output = 0
    for i in range(1, len(nums)+1):
        output += i - nums[i-1]
    return output