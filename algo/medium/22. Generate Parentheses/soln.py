def generateParenthesis(n: int) -> List[str]:
    """
    Time Complexity: O(4^n/(n^0.5))
    Space Complexity: O(n)

    TODO:
    1. Instantiate empty list
    2. There are two patterns, one is adding () to left of any open parenthesis. Else we add it in the end
    3. We store the previous outputs and perform 2 until n numbers 
    4. Return output
    """
    created = set(['()'])
    for i in range(2, n+1):
        temp = set()
        for c in created:
            for i in range(len(c)):
                if c[i] == '(':
                    temp.add(c[:i+1] + '()' + c[i+1:])
            temp.add(c + '()')
            
        created = temp
    return list(created)

    """
    Time Complexity: O(4^n/(n^0.5))
    Space Complexity: O(n)
    --> Answer from editorial
    TODO:
    1. We do recursively. At each point there are two ways to move forward, we either add a left parenthesis
    """
    answer = []
    def backtracking(cur_string, left_count, right_count):
        if len(cur_string) == 2 * n:
            answer.append("".join(cur_string))
            return
        if left_count < n:
            cur_string.append("(")
            backtracking(cur_string, left_count + 1, right_count)
            cur_string.pop()
        if right_count < left_count:
            cur_string.append(")")
            backtracking(cur_string, left_count, right_count + 1)
            cur_string.pop()
    backtracking([], 0, 0)
    return answer