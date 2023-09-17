def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    """
    (Iterative Approach)
    Time Complexity: O()
    Space Complexity: O()

    TODO:
    1. We do a power set and iterate through the possible combinations
    2. If combination exceeds the target we discard. If lower then keep for next iteration. If meets, we discard from power set and store the sorted output in the output. Check for repetition
    3. Return output once all powerset has been exhausted
    """
    power_set = [[0]]
    output = []
    while power_set:
        curr = power_set.pop()
        for c in candidates:
            temp = curr.copy()
            if curr[0] + c < target:
                temp[0] += c
                temp.append(c)
                power_set.append(temp)
            elif curr[0] + c == target:
                temp.append(c)
                if sorted(temp[1:]) not in output: # Wasteful operations here as we perform a search and sort
                    output.append(sorted(temp[1:]))
    return output

    """
    Cleaner Implementation for above
    Time Complexity: O()
    Space Complexity: O()

    TODO:
    1. We keep track of where we want to start looking, i.e. the index that we want to start checking
    2. We then do not have to sort our output since we would only prevent overlaps by deciding where we want to start checking
    3. We the return our output once completed
    """
    power_set = [[0,0]]
    output = []
    while power_set:
        curr = power_set.pop()
        for i in range(curr[1], len(candidates)):
            temp = curr.copy()
            c = candidates[i]
            if curr[0] + c < target:
                temp[0] += c
                temp[1] = i
                temp.append(c)
                power_set.append(temp)
            elif curr[0] + c == target:
                temp.append(c)
                output.append(temp[2:])
    return output

    """
    Recursive Approach

    Time Complexity: O(N * (T/M + 1))
    Space Complexity: O(T/M)

    TODO:
    1. Same as above but recursive
    """
    output = []

    def dfs(remain, combi, start, output):
        if remain == 0:
            # Make deep copy of current combination (Important!!)
            # NOTE: If we do not deep copy, it will append references that will be mutated along the call stack
            output.append(list(combi))
            return
        elif remain < 0:
            return
        for i in range(start, len(candidates)):
            combi.append(candidates[i])
            dfs(remain-candidates[i], combi, i, output)
            combi.pop()
    dfs(target, [], 0, output)
    return output