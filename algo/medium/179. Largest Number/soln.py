def largestNumber(nums: List[int]) -> str:
    """
    Time Complexity: O(nlogn)
    Space Complexity: O(n)
    --> Read more about custom comparators (From editorial)
    NOTE: Hard to come up with this solution
    --> Key idea would be to understand the x + y > y + x

    TODO:
    1. If each elements is greater than or equal to the another element it should come first
    2. We sort based on 1 then combine them together
    """
    class LargerNumKey(str):
        def __lt__(x, y):
            return x+y > y+x

    vals = ''.join(sorted([str(num) for num in nums], key=LargerNumKey))
    return '0' if vals[0] == '0' else vals

    """
    More intuitive explanation

    Time Complexity: O(n^2)
    Space Complexity: O(n)

    TODO:
    1. We do a swap between each element if the order x + y > y + x is not fulfilled
    """
    str_nums = [str(num) for num in nums]

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if str_nums[i] + str_nums[j] <= str_nums[j] + str_nums[i]:
                str_nums[i], str_nums[j] = str_nums[j], str_nums[i]

    output = ''.join(str_nums)

    return output if output[0] != '0' else '0'