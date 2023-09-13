def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    """
    (Suboptimal)
    Time Complexity: O(nlogn)
    Space Complexity: O(n)

    TODO:
    1. Append new interval into intervals and sort (If bigger system then might not be scalable if multiple calls are required since each time we have to sort..?)
    2. We follow same approach as 57. Merge Intervals i.e.
    3. We only check for closing ranges. If start of curr is greater than prev (NO OVERLAPS), we append our value into stack
    4. Else, we deal with the overlaps
    5. Return stack
    """
    intervals.append(newInterval)
    intervals = sorted(intervals)

    stack = []
    for e in intervals:
        if not stack or stack[-1][1] < e[0]:
            stack.append(e)
        else:
            stack[-1][1] = max(stack[-1][1], e[1])
        """
        Examples of overlaps that it covers. Don't have to care for other way round since sorted.
        (1,3) and (2, 5) --> (1,5)
        (1,4) and (2, 3) --> (1,4)
        (1,3) and (3 ,5) -- > (1,5)
        """
    return stack

    """
    (Optimal) --> Improves on the above method
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. Instead of appending then sorting, we find the index to insert which would take O(n)
    2. We then do the above from 2 to 5 as above
    """
    start, end = 0, len(intervals) - 1
    ans = 0 if len(intervals) == 0 else len(intervals)
    while start <= end:
        mid = (start + end) // 2
        if intervals[mid][0] > newInterval[0]:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    intervals.insert(ans ,newInterval)
    stack = []
    for e in intervals:
        if not stack or stack[-1][1] < e[0]:
            stack.append(e)
        else:
            stack[-1][1] = max(stack[-1][1], e[1])
        """
        Examples of overlaps that it covers. Don't have to care for other way round since sorted.
        (1,3) and (2, 5) --> (1,5)
        (1,4) and (2, 3) --> (1,4)
        (1,3) and (3 ,5) -- > (1,5)
        """
    return stack