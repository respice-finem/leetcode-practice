def lastStoneWeight(stones: List[int]) -> int:
    """
    Time Complexity: O(n log k)
    Space Complexity: O(n)

    TODO:
    1. We convert all stones to negative to simulate reverse order of stones
    2. We then heapify and pop. We then add back the negative diff to continue simulating the order of the heap
    3. We then stop once there are no more stones to pop by multiplying -1 for the remaining stones else 0
    """
    nega = [e * -1 for e in stones]
    heapq.heapify(nega)

    while len(nega) > 1:
        diff  = (heapq.heappop(nega) - heapq.heappop(nega)) * -1
        if diff > 0:
            heapq.heappush(nega, diff * -1)
    return nega[0] * -1 if len(nega) > 0 else 0

    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. We basically do counting sort and store them in array
    2. We then basically maintain a two pointer, if we are the same location, we do % 2 to remove
    3. We then move down and perform any minuses. The biggest weight would be the last known largest element in the array
    """
    max_weight = max(stones)
    count_arr = [0] * (max_weight + 1)
    for c in stones:
        count_arr[c] += 1

    biggest_weight = 0
    current_weight = max_weight
    while current_weight > 0:
        if count_arr[current_weight] == 0:
            current_weight -= 1
        elif biggest_weight == 0:
            count_arr[current_weight] %= 2
            if count_arr[current_weight] == 1:
                biggest_weight = current_weight
            current_weight -= 1
        else:
            count_arr[current_weight] -= 1
            if biggest_weight - current_weight <= current_weight:
                count_arr[biggest_weight - current_weight] += 1
                biggest_weight = 0
            else:
                biggest_weight -= current_weight
    return biggest_weight