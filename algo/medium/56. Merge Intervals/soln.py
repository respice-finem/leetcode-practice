def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    Time Complexity: O(nlogn)
    Space Complexity: O(n)

    TODO:
    1. Sort to ensure that all values are in order
    2. Instantiate stack to compare
    3. While values in stack are not less than (start and end), we perform merging
    4. Else we append the latest value
    5. Return stack
    """
    intervals = sorted(intervals)
    stack = []
    for e in intervals:
        temp = e
        while stack and not stack[-1][1] < temp[0]: # Only check if we need to merge (But redundant since we know that it will be monotonically increasing, we just need to deal with the closing range)
            val = stack.pop() # Wasted operation here
            temp[0] = min(val[0], temp[0]) # Redundant since the values will always be smaller in the stack
            temp[1] = max(val[1], temp[1])
        stack.append(temp)
    return stack

    """
    Cleaner Implementation for above

    Time Complexity: O(nlogn)
    Space Complexity: O(n)

    TODO:
    1. Concept is same as above
    2. But we can minimize our operations to just compare the ends and update the ends (Merge)
    3. Else, we can just append the new values
    """
    intervals = sorted(intervals) # By sorting we ensure that our starts are always monotonically increasing
    stack = []
    for e in intervals:
        if not stack or stack[-1][1] < e[0]: # If curr start is larger than end. No overlaps
            stack.append(e)
        else:
            stack[-1][1] = max(stack[-1][1], e[1]) # We get the max closing range as this covers all related overlaps
    """
    Examples of overlaps that it covers. Don't have to care for other way round since sorted.
    (1,3) and (2, 5) --> (1,5)
    (1,4) and (2, 3) --> (1,4)
    (1,3) and (3 ,5) -- > (1,5)
    """
    return stack