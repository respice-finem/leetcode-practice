def countHomogenous(self, s: str) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. Total number of combis in homogenous string is n(n + 1)/2. Therefore we collate all the homogenous strings and add the number of combis together then do n(n+1) /2 % (10 ^ 9 + 7)  
    """
    homogen_string = []
    temp = s[0]

    for i in range(1, len(s)):
        if s[i] != temp[-1]:
            homogen_string.append(temp)
            temp = s[i]
        else:
            temp += s[i]
    if temp:
        homogen_string.append(temp)
    return int(sum([
        (len(e) * (len(e) + 1)) / 2
        for e in homogen_string
    ]) % (10**9 + 7))
    
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    NOTE: For running streaks, always check if we can just store the variable to move along, since this can save alot of space
    TODO:
    1. Optimizing above instead of storing the values in an array, we just keep the running count
    """
    output = 0
    curr_len = 0
    for i in range(len(s)):
        if i == 0 or s[i] == s[i-1]:
            curr_len += 1
        else:
            output = output + (curr_len * (curr_len +1)) / 2
            curr_len = 1
    return int((output + (curr_len * (curr_len +1)) / 2) % (10 ** 9 + 7))