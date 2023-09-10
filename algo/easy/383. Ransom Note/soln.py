def canConstruct(ransomNote: str, magazine: str) -> bool:
    """
    Time Complexity: O(n)
    Space Complexity: O(1) --> Only 26 alphabets

    TODO:
    1. Count number of letters in magazine
    2. Iterate through ransomNote and delete the letters
    3. If in any case if doesnt appear, we return False, else return True
    """
    e_dict = {}
    for char in magazine:
        if char not in e_dict:
            e_dict[char] = 1
        else:
            e_dict[char] += 1

    for char in ransomNote:
        if char in e_dict:
            e_dict[char] -= 1
            if e_dict[char] == 0:
                del e_dict[char]
        else:
            return False
    return True

    """
    (Suboptimal)
    Time Complexity: O(nlogn)
    Space Complexity: O(1)

    TODO:
    1. Sort letters and ranso
    """
    mag_list = sorted(magazine, reverse=True)
    ran_list = sorted(ransomNote, reverse=True)
    
    while ran_list and mag_list:
        if ran_list[-1] == mag_list[-1]:
            ran_list.pop()
            mag_list.pop()
        elif mag_list[-1] < ran_list[-1]:
            mag_list.pop()
        else:
            return False
    return not ran_list