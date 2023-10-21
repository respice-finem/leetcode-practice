def countVowelStrings(self, n: int) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    Bottom Up

    TODO:
    1. We keep a cumulative sum starting from 1-5.
    2. We then repeatedly add this cumulative sum until we hit our desired n, we then sum the total combi together and return the output
    """
    output = [1] * 5

    for i in range(1,n):
        for j in range(1, 5):
            output[j] = output[j] + output[j-1]
    return sum(output)