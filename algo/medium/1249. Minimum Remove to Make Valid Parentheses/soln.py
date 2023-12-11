def minRemoveToMakeValid(s: str) -> str:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. We do a two pass. We first take note of bad parenthesis to be removed. If there are remaining open parenthesis we add to the remove
    2. We then skip the indexes to be removed and build the string
    """
    to_remove = set()
    stack = []

    for i in range(len(s)):
        if s[i] == ')':
            if stack:
                stack.pop()
            else:
                to_remove.add(i)
        elif s[i] == '(':
            stack.append(i)
    for e in stack:
        to_remove.add(e)
    output = ""
    for i in range(len(s)):
        if i not in to_remove:
            output += s[i]
    return output