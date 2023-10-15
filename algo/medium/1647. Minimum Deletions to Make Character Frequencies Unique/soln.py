def minDeletions(s: str) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. We basically count each elements and store their counts
    2. We then iterate through the counts and check whether the current value exists in our array.
    3. If not, we increment in a running count array. Else we decrement the count for our existing value till it does not exist in value array and add to the deletion count
    4. Return the deletion count
    """
    count_dict = Counter(s)
    counts = count_dict.values()
    val_arr = [0] * (max(counts) + 1)

    output = 0
    for c in counts:
        while val_arr[c] != 0 and c != 0:
            c -= 1
            output += 1
        val_arr[c] = 1
    return output

    """
    Time Complexity: O(nlogn)
    Space Complexity: O(n)
    --> Answer from Editorial

    TODO:
    1. Similar to above, but all we need to do is sort first by descending
    2. Delete the current sorted to convert it to the max frequency only when frequency is greater than max
    3. We then update the allowed frequency to max(0, freq-1)
    """
    frequency = [0] * 26
    for char in s:
        frequency[ord(char)-ord('a')] += 1
    frequency.sort(reverse=True)

    delete_count = 0
    max_freq_allowed = len(s)
    for freq in frequency:
        if freq > max_freq_allowed:
            delete_count += freq - max_freq_allowed
            freq = max_freq_allowed
        max_freq_allowed = max(0, freq-1)
    return delete_count