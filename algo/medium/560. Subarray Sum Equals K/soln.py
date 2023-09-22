def subarraySum(nums: List[int], k: int) -> int:
    """
    TLE
    We generate all possible combinations (Will timeout)
    Find ways to prune it
    Time Complexity: O(n^2)
    Space Complexity: O(n^2)

    TODO:
    1. We generate all combinations and check if matches sum
    2. Return the total count
    """
    superset = [0]
    count = 0
    for num in nums:
        temp = [0]
        for seen in superset:
            seen += num
            if seen == k:
                count += 1
            temp.append(seen)
        superset = temp
    return count

    """
    We generate the running sum

    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. We generate the running sum and then we check if we have previously encountered such value previously then we add the total count to it
    2. We then return the count
    """
    possible = {0 : 1}
    count = 0
    current_cumu = 0
    for num in nums:
        current_cumu += num
        temp = current_cumu - k
        if temp in possible:
            count += possible[temp]
        possible[current_cumu] = possible.get(current_cumu, 0) + 1
    return count