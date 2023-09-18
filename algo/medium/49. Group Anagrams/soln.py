def groupAnagrams(strs: List[str]) -> List[List[str]]:
    """
    Time Complexity: O(n * (klogk))
    Space Complexity: O(n * k)

    TODO:
    1. Get sorted values for str then add into output dict
    2. We then return the values for each as list
    """
    output_dict = {}
    for string in strs:
        temp = ''.join(sorted(string))
        if temp not in output_dict:
            output_dict[temp] = [string]
        else:
            output_dict[temp].append(string)
    return list(output_dict.values())

    """
    (Count sort)
    Time Complexity: O(n * k)
    Space Complexity: O(n * k)

    TODO:
    1. We do by counts for each alphabet
    2. The counts will be the keys and we will append accordingly to the key
    """
    output_dict = {}
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        c_tuple = tuple(count)
        if c_tuple not in output_dict:
            output_dict[c_tuple] = [s]
        else:
            output_dict[c_tuple].append(s)
    return output_dict.values()