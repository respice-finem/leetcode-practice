import heapq

def leastInterval(self, tasks: List[str], n: int) -> int:
    """
    Time Complexity: O(n log k)
    Space Complexity: O(n)

    TODO:
    1. We setup two heaps: One for priority queue for the execution and the another for the cooldown
    2. We check if we need to reintegrate any values from the cooldown into the execution heap. If items are cooled down we just feed it in. 
    3. We then check
    """
    tasks_ct = Counter(tasks)
    nega = [[-v, k] for k,v in tasks_ct.items()]
    cooldown = []
    heapq.heapify(nega)
    heapq.heapify(cooldown)
    time = 0
    while nega or cooldown:
        while cooldown and cooldown[0][0] < time:
            val = heapq.heappop(cooldown)[1]
            heapq.heappush(nega, val)
        if nega:
            curr = heapq.heappop(nega)
            curr[0] += 1
            if curr[0] < 0:
                heapq.heappush(cooldown, [time + n] + [curr])
        time +=1
    return time

    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    --> Answer from editorial
    TODO:
    1. We get the count of tasks and sort them
    2. The point is that we try space out the cooldowns accordingly and in between we fill up the amount of tasks available between the idle time
    """
    frequencies = [0] * 26
    for t in tasks:
        frequencies[ord(t) - ord('A')] += 1
    
    frequencies.sort()

    f_max = frequencies.pop()
    idle_time = (f_max -1) * n
    while frequencies and idle_time > 0:
        idle_time -= min(f_max - 1, frequencies.pop())
    idle_time = max(0, idle_time)

    return idle_time + len(tasks)