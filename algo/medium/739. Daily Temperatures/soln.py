def dailyTemperatures(temperatures: List[int]) -> List[int]:
    """
    (Suboptimal)
    Time Complexity: O(n^2) --> Isit O(n) 
    Space Complexity: O(n)

    TODO:
    1. For each element, we keep track of the next largest value from its element
    2. Since in each element we store the next closest largest value, as we iterate downwards, we are guaranteed to find the closest largest temp aft the current value
    3. We then output the number of days from it
    """
    stack = [0] * len(temperatures)
    stack[-1] = (-999, 0)
    # (Index where it is largest, Days)
    for i in range(len(temperatures)-2, -1, -1):
        index = i+1
        while index != -999:
            if temperatures[i] >= temperatures[index]:
                index = stack[index][0]
                if index == -999:
                    stack[i] = (-999, 0)
            else:
                stack[i] = (index, index - i)
                break
    return [e[1] for e in stack]

    """
    (Monotonic Stack)
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. Iterate from the start, if values are not larger than we add to stack
    2. If it is larger we pop and get the days. We then fill the vals in the output array
    3. Return the output once completed
    """
    output = [0] * len(temperatures)
    stack = []

    for curr_day, curr_temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < curr_temp:
            prev_day = stack.pop()
            output[prev_day] = curr_day - prev_day
        stack.append(curr_day)
    return output

    """
    Cleaner Implementation of my solution in 1

    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
    1. We start from the back, and perform checks
    2. We get the hottest at each point
    3. We then backtrack and correct the element values
    """
    n = len(temperatures)
    answer = [0] * n
    hottest = 0

    for curr_day in range(n - 1, -1, -1):
        current_temp = temperatures[curr_day]
        if current_temp >= hottest:
            hottest = current_temp
            continue

        days = 1
        while temperatures[curr_day + days] <= current_temp:
            days += answer[curr_day + days]
        answer[curr_day] = days
    
    return answer