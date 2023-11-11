def topKFrequent(words: List[str], k: int) -> List[str]:
    """
    Time Complexity: O(n log n)
    Space Complexity: O(n)

    TODO:
    1. We count and perform sort based on the count (We have to desc sort x and asc sort)
    2. Return the top k frequent values
    """
    # counts = sorted([(v, k) for k,v in Counter(words).items()], key=lambda x: (-x[0], x[1]))[:k]
    # return [e[1] for e in counts]
    
    """
    Time Complexity: O(n log k)
    Space Complexity: O(n)

    TODO:
    1. We convert the counts into a max heap, and we then remove it
    2. We then return the values by converting them back to char
    """
    count_dict = Counter(words)
    heap = [(-freq, word) for word, freq in count_dict.items()]   # During the check, if first element has two equal values, it will get the lower of the second likewise as it moves forward n-steps
    heapify(heap)
    return [heappop(heap)[1] for _ in range(k)]