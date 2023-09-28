def characterReplacement(s: str, k: int) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
    1. We do a sliding window. Increase if the number of elements are within acceptable changes using k. If we meet an unacceptable threshold, we then slide our window left till we meet the target and continue moving using the right pointer
    2. During step 1, if it continues moving , we keep track of the running count and check if it is larger than the max count
    3. Once the right reaches the end, we return our max length
    """
    left, right = 0, 0
    running_count = {}
    count = 0
    max_len = 0

    def check_unfit(rcount, k): # Wasted operations here.
        max_val = max(rcount.values())
        max_key = [k for k in rcount if rcount[k] == max_val][0]
        other_vals = sum([v for k,v in rcount.items() if k != max_key])
        return other_vals > k


    while right < len(s):
        running_count[s[right]] = running_count.get(s[right], 0) + 1
        # Check if current strings can be replaced, if not we shift the left
        while len(running_count) > 1 and check_unfit(running_count, k):
            running_count[s[left]] -= 1
            if running_count[s[left]] == 0:
                del running_count[s[left]]
            count -= 1
            left += 1
        count += 1
        max_len = max(count, max_len)
        right += 1
    return max_len

    """
    Cleaner Implementation for above
    --> Answer from editorial (Quite Contrived Approach)
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    TODO:
    1. Similar to above, but we reduce the time needed to search the space.  At each step we check if the latest letter would give us the maximum frequency
    2. We get the maximum frequency of any window (Need to understand why this is made as such)
    3. We then move forward if it is within our threshold else, we move the left pointer by 1 to reduce size of sliding window. We then get maximum length since size of window never decreases
    """
    start = 0
    frequency_map = {}
    max_frequency = 0
    longest_substring_length = 0
    for end in range(len(s)):
        frequency_map[s[end]] = frequency_map.get(s[end], 0) + 1

        max_frequency = max(max_frequency, frequency_map[s[end]])

        is_valid = (end + 1 - start - max_frequency <= k)
        if not is_valid:
            frequency_map[s[start]] -= 1
            start += 1
        
        longest_substring_length = end + 1 - start
    return longest_substring_length