def addBinary(a: str, b: str) -> str:
    """
    Time Complexity: O(m+n)
    Space Complexity: O(max(m,n))

    TODO:
    1. Iterate through each of the string
    2. Perform the carry if needed
    3. Join the strings again
    """
    output = []
    carry = False
    while a or b:
        if a and b:
            temp = int(a[-1]) + int(b[-1]) + carry
        elif a:
            temp = int(a[-1]) + carry
        elif b:
            temp = int(b[-1]) + carry
        carry = temp // 2
        output.append(str(temp % 2))
        a = a[:-1]
        b = b[:-1]
    if carry:
        output.append(str(carry))
    return "".join(output[::-1])

    """
    Time Complexity: O(m+n)
    Space Complexity: O(max(m,n))

    TODO:
    1. Convert the bin strings to int
    2. Add the two ints
    3. Convert to bin again
    """
    a = int(a , 2)
    b = int(b, 2)
    return bin(a+b)[2:]

    """
    (Bit Manip Solution)
    Answer from editorial

    Time Complexity: O(max(m,n))
    Space Complexity: O(max(m,n))

    TODO:
    1. Convert x and y from string to a and b
    2. We then do XOR which does (a+b) mod 2
    3. We then check for carry (a & y) << 1
    """
    x, y = int(a, 2), int(b, 2)
    while y:
        answer = x ^ y
        carry = (x & y) << 1
        x, y = answer, carry
    return bin(x)[2:]