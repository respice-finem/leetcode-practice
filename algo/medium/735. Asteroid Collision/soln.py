def asteroidCollision(asteroids: List[int]) -> List[int]:
    """
    Time Complexity: O(n)
    Space Complexity: O(n) --> List reversal

    TODO:
    1. Instantiate an empty stack
    2. We pop the first asteroids from the list
    3. We then check the sum between them. We check if the one in the stack is positive and the one from the list is negative. If the value is above 0 we keep left, if value is below 0 we pop left and take right. Else, we pop both
    """
    stack = []
    asteroids = asteroids[::-1]
    while asteroids:
        if not stack:
            stack.append(asteroids.pop())
        else:
            while asteroids and stack and stack[-1] > 0 and asteroids[-1] < 0:
                if stack[-1] + asteroids[-1] < 0:
                    stack.pop()
                elif stack[-1] + asteroids[-1] == 0:
                    stack.pop()
                    asteroids.pop()
                else:
                    asteroids.pop()
            if asteroids:
                stack.append(asteroids.pop())

    return stack

    """
    Cleaner Implementation for above

    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. We iterate through the asteroids
    2. While the stack is not empty and we have a left > 0 and right < 0 situation
    3. We pop stack if left + right < 0 else left + right == 0 we pop from stack then we move on to the next asteroid
    4. Else we append the value from the stack
    5. Return the output
    """

    stack = []

    for ast in asteroids:
        while stack and ast < 0 < stack[-1]: # Interesting new approach is that we can do a while else loop
            if stack[-1] < -ast:
                stack.pop()
                continue
            elif stack[-1] == -ast:
                stack.pop()
            break
        else:
            stack.append(ast)
    return stack