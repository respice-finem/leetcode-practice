def calculate(s: str) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    --> My implementation, cleand up repetition for code

    TODO:
    1. We add everything to stack, unless there are multiplications and divisions
    then we deal with them first. Add the output back to the stack
    2. Second run we complete the additions and subtractions (Don't forget to deal with the last number)
    """
    s = s.replace(' ', '')
    stack = []

    def handle_ops(stack, temp, prev_ops):
        result = 0
        if prev_ops == '-':
            result = -1 * temp
        elif prev_ops == '*':
            result = stack.pop() * temp
        elif prev_ops == '/':
            result = int(stack.pop()/temp)
        else:
            result = temp
        stack.append(result)
        return 0, char
    
    temp = 0
    prev_ops = ''
    for char in s:
        if char.isnumeric():
            temp = temp * 10 + int(char)
        else:
            temp, prev_ops = handle_ops(stack, temp, prev_ops)
    temp, prev_ops = handle_ops(stack, temp, prev_ops)

    return sum(stack)

    """
    Another Implementation

    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. Same as above but we run two if loops (slightly slower since we need to evaluate two logics at all times)
    """
    s = s.replace(' ', '')
    stack = []

    temp = 0
    prev_ops = ''
    for i in range(len(s)):
        if s[i].isnumeric():
            temp = temp * 10 + int(s[i])
        if not s[i].isnumeric() or i == len(s) - 1:
            result = 0
            if prev_ops == '-':
                result = -1 * temp
            elif prev_ops == '*':
                result = stack.pop() * temp
            elif prev_ops == '/':
                result = int(stack.pop()/temp)
            else:
                result = temp
            stack.append(result)
            temp, prev_ops = 0, s[i]
    return sum(stack)

    """
    (Optimal)
    Time Complexity: O(n)
    Space Compexity: O(1)

    TODO:
    1. Technically we do not need a stack since all we need to do is keep track of the previous number, current number and the output
    2. All we have to do is add together the previous number to the output which is similar to the stack approach
    """
    s = s.replace(' ', '')
    curr_num, last_num, result = 0, 0, 0
    ops = '+'

    for i in range(len(s)):
        if s[i].isnumeric():
            curr_num = curr_num * 10 + int(s[i])
        if not (s[i].isnumeric()) or i == len(s) - 1:
            if ops == '-' or ops == '+':
                result += last_num
                last_num = curr_num if ops == '+' else -1 * curr_num
            elif ops == "*":
                last_num = last_num * curr_num
            elif ops == '/':
                last_num = int(last_num / curr_num)

            ops = s[i]
            curr_num = 0

    result += last_num
    return result