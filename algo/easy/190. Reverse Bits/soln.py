def reverseBits(self, n: int) -> int:
    # --> More advanced algos requires
    # --> Specific bit shifting
    # --> Look into it if I have time since this is a small subset
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
    1. Instantiate empty output
    2. If & 1 == 0, we multiply
    3. If & 1 == 0, we just left shift 1
    4. Once we run it down to 0 we return
    """
    ret, power = 0, 31
    while n:
        ret += (n & 1) << power # Shift to 32 spaces 
        n >>= 1
        power -= 1
    return ret
    """
    (Not optimal spacewise)
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. Convert n to string
    2. Iterate and fit into string
    3. Convert output to int again when completed
    """
    n_str = bin(n)[2:].zfill(32)
    output = ""
    for i in range(len(n_str)-1 , -1, -1):
        output += n_str[i]
    return int(output, 2)