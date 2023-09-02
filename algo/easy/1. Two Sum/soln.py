def twoSum(nums: List[int], target: int) -> List[int]:
    """
    (Sub-optimal)

    Time Complexity: O(n^2)
    Space Complexity: O(1)

    TODO:
    1. Iterate through the nums list twice
    2. Find out the potential pairing based on the index
    3. Return our answer once found
    """
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    
    """
    (Optimal)
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. Set an empty dictionary to get all the solutions
    2. Iterate through the values and store the corresponding negative sum against the target
    2.5 Key Value Pair should be Answer, Curr Index
    3. If pair is found return return the two indexes
    """
    soln_dict = {}

    for i in range(len(nums)):
        temp = target - nums[i]
        if nums[i] in soln_dict:
            return [i, soln_dict[nums[i]]]
        else:
            soln_dict[temp] = i