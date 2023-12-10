def numberOfArithmeticSlices(nums: List[int]) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. We get the differences between each element
    2. We then do a sliding window to check if the prev element is the same. If length of sliding window > 1, we cumulatively add len(temp) - 1 to the output
    3. Return the output
    """
    output = 0
    diff = [nums[i-1] - nums[i] for i in range(1, len(nums))]
    right = 0
    temp = []
    while right < len(diff):
        if temp:
            if temp[-1] == diff[right]:
                temp.append(diff[right])
            else:
                temp = [diff[right]]
        else:
            temp.append(diff[right])

        if len(temp) > 1:
            output += len(temp) - 1
        right += 1

    return output