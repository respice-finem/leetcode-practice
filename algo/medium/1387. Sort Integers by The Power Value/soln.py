def getKth(lo: int, hi: int, k: int) -> int:
    """
    Time Complexity: O(n log n)
    Space Complexity: O(n)

    TODO:
    1. We memorize the values to be formed while building the path. We then add this to the dictionary
    2. We continue to build the values for each until we reach the end and sort the output and return the kth value
    """
    power_value = {1: 0}
    output = []

    for i in range(lo, hi+1):
        if i not in power_value:
            temp = [i]
            power_value[i] = 1
            curr = i
            while curr != 1:
                if curr % 2 == 0:
                    curr = curr / 2
                else:
                    curr = 3 * curr + 1
                for e in temp:
                    if e not in power_value:
                        power_value[e] = 1
                    else:
                        power_value[e] += power_value.get(curr, 1)
                if curr in power_value:
                    break
                else:
                    temp.append(curr)
                    power_value[curr] = 1
                # print(curr, power_value)
        output.append((i, power_value[i]))

    return sorted(output, key=lambda x: x[1])[k-1][0]

    """
    Cleaner Implementation of Above
    NOTE: In this case, faster to do recursion to deal with the seen values

    Time Complexity: O(nlogn)
    Space Complexity: O(n)

    TODO:
    1. Recursive implementation for above 
    """
    cache = {1: 0}
    def powervals(n):
        if n not in cache:
            if n % 2 == 0:
                cache[n] = 1 + powervals(n/2)
            else:
                cache[n] = 1 + powervals(3*n + 1)
        return cache[n]
    return sorted((powervals(i), i) for i in range(lo, hi+1))[k-1][1]
