def canAttendMeetings(intervals: List[List[int]]) -> bool:
    """
    (Suboptimal)
    Time Complexity: O(n^2)
    Space Complexity: O(1)

    TODO:
    1. Compare each and every one of the elements. If any exceeds, return False
    2. Else return True
    """
    def overlap(i1, i2):
        return i1[0] >= i2[0] and i1[0] < i2[1] or i2[0] >= i1[0] and i2[0] < i1[1]

    for i in range(len(intervals)):
        for j in range(i+1, len(intervals)):
            i1, i2 = intervals[i], intervals[j]
            if overlap(i1, i2): # Lots of wasted oprations here
                return False
    return True

    """
    (Optimal)
    Time Complexity: O(nlogn)
    Space Complexity: O(1)

    TODO:
    1. Sort the list
    2. For each adjacenet intervals, we check if the end is greater than the next start. If so return False
    3. Else, return True
    """
    intervals = sorted(intervals)
    for i in range(len(intervals)-1):
        if not (intervals[i][1] <= intervals[i+1][0]):
            return False
    return True