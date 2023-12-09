def threeSum(nums: List[int]) -> List[List[int]]:
    """
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    NOTE: Answer from editorial
    TODO:
    1. We set the target value as the pivot and perform a two sum to move along.
    2. We then keep track of the duplicates and move forward
    """
    res, dups = set(), set()
    seen = {}

    for i, val1 in enumerate(nums):
        if val1 not in dups:
            dups.add(val1)
            for j, val2 in enumerate(nums[i+1:]):
                complement = -val1-val2
                if complement in seen and seen[complement] == i:
                    res.add(tuple(sorted((val1, val2, complement))))
                seen[val2] = i
    return res