def countVowelPermutation(n: int) -> int:
    """
    (Simple Bottom Up)
    Time Complexity: O(n)
    Space Complexity: O(1) # Constant array size

    TODO:
    1. We initialize an empty array to store our necessary values
    2. We then build the values while memorizing the value before and instantiate a deep copy to make sure that it does not double count
    3. Return the sum modulo 10 ^ 9 + 7
    """
    output = [1] * 5
    count = [0] * 5
    for i in range(2, n+1):
        count[0] = output[1]
        count[1] = output[0] + output[2]
        count[2] = sum([output[i] for i in range(5) if i != 2])
        count[3] = output[2] + output[4]
        count[4] = output[0]
        output = list(count)
    return sum(output) % (10 ** 9 + 7)

    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    TODO:
    1. Same as above but we use variables instead
    """
    a_count = e_count = i_count = o_count = u_count = 1

    for i in range(2, n + 1):
        a_new = e_count
        e_new = a_count + i_count
        i_new = a_count + e_count + o_count + u_count
        o_new = i_count + u_count
        u_new = a_count
        a_count, e_count, i_count, o_count, u_count = a_new, e_new, i_new, o_new, u_new
    return (a_count + e_count + i_count + o_count + u_count) % (10 ** 9 + 7)