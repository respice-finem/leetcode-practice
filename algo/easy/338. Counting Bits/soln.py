def countBits(n: int) -> List[int]:
    """
    (DP Solution)
    Time Complexity: O(n)
    Space Complexity: O(1) --> Apparently doesnt count in our values

    TODO:
    1. We create an empty list of vals to match our output range
    2. Iterate through num and check for two things
    2.5 If it is a exponent of 2, we append 1, else we reuse our previous number to add to the number of ones to our current exponent
    3. Return the nums
    """
    nums = [0] * (n+1)
    twos = 1
    for i in range(1, n+1):
        if twos << 1 == i:
            nums[i] = 1
            twos = twos << 1
        else:
            nums[i] = 1 + nums[i-twos]
    return nums

    """
    Cleaner Implementation using the least significant bit method
    (DP Solution) --> Difficult to think of during interview
    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
    1. We create an empty list of vals to match our output range
    2. Iterate through num
    3. For each num, we always add 1 since there would always be a 1 in it
    4. We then check nums[n&(n-1)], it maintains all the other ones other than the LSB 1
    5. This basically ensures that we reuse our calculations prior
    """
    nums = [0] * (n+1)
    for x in range(1, n+1):
        nums[x] = nums[x & (x-1)] + 1
    return nums