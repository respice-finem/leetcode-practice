from collections import Counter

def isPossibleDivide(nums: List[int], k: int) -> bool:
    """
    Time Complexity: O(nlogn)
    Space Complexity: O(n)

    TODO:
    1. We sort then do count
    2. Go through each number and determine if we can form the groups. If not we return False
    """
    counts = Counter(nums)
    nums = sorted(set(nums))
    for num in nums:
        while counts[num] > 0:
            for i in range(num + 1, num + k):
                if i not in counts or counts[i] == 0:
                    return False
                counts[i] -= 1
            counts[num] -= 1
    return True