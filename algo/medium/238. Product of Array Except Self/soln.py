def productExceptSelf(nums: List[int]) -> List[int]:
    """
    --> TBh this question is a puzzle, you see it or you don't, better revise it again before interviews
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. We have to perform multiplications from forward and from backward
    2. This will then allow us to make cross multiplications between the forward and backwards to complete the loop since product except self array follows a loop around the array
    3. We first obtain the two ends and obtain the remaining products through cross multiplication
    """
    output = [0] * len(nums)
    forward = [nums[0]]
    for i in range(1, len(nums)):
        forward.append(forward[-1] * nums[i])
    forward = forward[::-1]

    for i in range(len(nums)-2, -1, -1):
        nums[i] = nums[i + 1] * nums[i]

    output[0], output[-1] = nums[1], forward[1]
    for i in range(2, len(nums)):
        output[i-1] = nums[i] * forward[len(nums)+1-i]

    return output

    """
    Cleaner O(1) Implementation
    --> Solution from editorial (Concept here is forward and reverse sweep for O(1) patterns)
    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
    1. We basically do a forward pass and stepping one ahead with the multiplication
    2. We then do a reverse pass to multiply what's the remaining
    """
    answer = [0] * len(nums)
    answer[0] = 1
    
    for i in range(1, len(nums)):
        answer[i] = nums[i-1] * answer[i-1]

    R = 1
    for i in reversed(range(len(nums))):
        answer[i] = answer[i] * R
        R *= nums[i]

    return answer