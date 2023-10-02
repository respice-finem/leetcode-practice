def singleNumber(nums: List[int]) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. Create an empty set
    2. Add if not in set, del if in
    3. Return last number
    """
    rep = set()
    for num in nums:
        if num not in rep:
            rep.add(num)
        else:
            rep.remove(num)
    return list(rep)[0]

    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    --> Answer from editorial

    TODO:
    1. We basically do XOR to get the unique number
    """
    a = 0
    for i in nums:
        a ^= i
    return a