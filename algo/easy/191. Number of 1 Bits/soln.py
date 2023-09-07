def hammingWeight(n: int) -> int:
    """
    (String approach: Suboptimal)

    Time Complexity: O(n)/ Or techincally O(1) since it is fixed to a 32 length binary string
    Space Complexity: O(n) --> Converting to binary string

    TODO:
    1.Convert n to binary string
    2. Count how many 1s
    3. Return output
    """
    bin_n = bin(n)[2:]
    output = 0
    for char in bin_n:
        if char == "1":
            output += 1
    return output

    """
    (Bit Manipulation Solution: Optimal)

    Time Complexity: O(n)/ Or techincally O(1) since it is fixed to a 32 length binary string
    Space Complexity: O(1)

    TODO:
    1. Setup an empty output int
    2. Add n & 1 (Check if last digit of binary is 1) then shift right (Essentially n // 2)
    3. Return output
    """
    output = 0
    while n:
        output += n & 1
        n >>= 1
    return output

    """
    (Bit Manipulation Solution: Advanced)
    --> Least Significant Bit (Improvement for Soln 2)

    Time Complexity: O(n)/ Or techincally O(1) since it is fixed to a 32 length binary string
    Space Complexity: O(1)

    TODO:
    1. While all the num is not 0
    2. We basically do n & (n-1), this is a neat trick that basically flips the 1s that we are looking at by chunks
    3. So we repeat this step till num becomes 0 and add 1 to our counter
    4. Return counter once num is 0
    """
    output = 0
    while n != 0:
        output += 1
        n &= n - 1
    return output