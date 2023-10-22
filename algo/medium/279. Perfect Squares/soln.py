def numSquares(self, n: int) -> int:
    """
    Time Complexity: O(n ^ (3/2))
    Space Complexity: O(n)
    Bottom Up

    TODO:
    1. Generate an empty array with the values that we want to fill
    2. We then build from scratch while getting the min count to generate the num
    3. Return array[target]
    """
    output = [float('inf')] * (n+1)
    output[0] = 0

    for i in range(1, len(output)):
        for e in range(1, i+1):
            sq = e * e
            temp = i - sq
            if temp >= 0:
                output[i] = min(output[i], output[temp]+1)
            else:
                break
    return output[n]

    """
    Time Complexity: O(n^(h/2))
    Space Complexity: O(n^(0.5) * h)
    --> Answer from Editorial

    TODO:
    1. We setup the possible square numbers and run a BFS to get the count
    """
    square_nums = [i * i for i in range(1, int(n ** 0.5)+1)]

    level = 0
    queue = {n}
    while queue:
        level += 1
        next_queue = set()
        for remainder in queue:
            for square_num in square_nums:
                if remainder == square_num:
                    return level
                elif remainder < square_num:
                    break
                else:
                    next_queue.add(remainder - square_num)
        queue = next_queue
    return level