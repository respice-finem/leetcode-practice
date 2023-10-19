from collections import Counter

def isNStraightHand(hand: List[int], groupSize: int) -> bool:
    """
    Time Complexity: O(nlogn)
    Space Complexity: O(n)

    TODO:
    1. We keep count of the elements in hand. We also keep track of the min and max to run through an iteration later on
    2. We then form our groups and minus from the dictionary of counts. If in any case we cannot form a group of K we return False. Else we return True
    """
    counts = Counter(hand)
    hash_set = sorted(set(hand))

    for i in hash_set:
        while i in counts and counts[i] > 0:
            for j in range(i+1, i + groupSize):
                if j not in counts:
                    return False
                counts[j] -= 1
                if counts[j] == 0:
                    del counts[j]
            counts[i] -= 1
            if counts[i] == 0:
                del counts[i]
    return True