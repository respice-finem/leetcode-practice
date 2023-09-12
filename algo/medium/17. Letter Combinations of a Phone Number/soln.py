def letterCombinations(digits: str) -> List[str]:
    """
    Time Complexity: O(4^N * N)
    Space Complexity: O(N) --> Call Stack

    TODO:
    1. Instantiate char list for each num
    2. Perform DFS on the numbers
    3. Return values
    """
    char_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': 'wxyz'
    }

    def dfs(num, ans, char_map, cache=[]):
        if num == '':
            return ans
        else:
            for e in char_map[num[0]]:
                val = dfs(num[1:], ans+e, char_map, cache)
                if val:
                    cache.append(val)

    output = []
    dfs(digits, '', char_map, output)
    return output