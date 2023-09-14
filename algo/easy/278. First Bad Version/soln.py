def firstBadVersion(n: int) -> int:
    """
    Time Complexity: O(log n)
    Space Complexity: O(1)

    TODO:
    1. Perform binary search with a twist:
    a) If current is good, if current is good we can start to look after this
    b) If current is bad, we check if previous is good (this would mean the current mid is bad)
    c) If current is bad, we check if previous is bad (this would mean that we have end before this since it is not what we are looking for)
    """
    start = 1
    end = n

    while start <= end:
        mid = (start + end) // 2
        if isBadVersion(mid) and not isBadVersion(mid - 1):
            return mid
        elif isBadVersion(mid) and isBadVersion(mid - 1):
            end = mid - 1
        elif not isBadVersion(mid):
            start = mid + 1

    """
    Cleaner Implementation for above
    --> Answer from editorial

    Time Complexity: O(log n)
    Space Complexity: O(1)

    TODO:
    1. Perform binary search
    a) If current is bad, we limit the end of our search space to the current value
    b) If current is good, we can just ignore everyth up to that point and continue searching
    """
    start = 1
    end = n

    while start < end:
        mid = (start + end) // 2
        if isBadVersion(mid):
            end = mid
        else:
            start = mid + 1
    return start