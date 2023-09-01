def isValid(self, s: str) -> bool:
        '''
        Time Complexity: O(n)
        Space Complexity: O(n)

        TODO:
        1. Create empty stack
        2. Get opening bracket and push
        3. Remove when we see corresponding, otherwise we return False
        4. If stack is empty after iterating everything, we return True
        '''

        stack = []
        bracket_dict = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for char in s:
            curr_val = bracket_dict.get(char, None)
            if curr_val:
                if len(stack) == 0 or stack[-1] != curr_val:
                    return False
                elif stack[-1] == curr_val:
                    stack.pop()
            else:
                stack.append(char)

        return len(stack) == 0

        # -------------------------
        # Cleaner Implementation
        # -------------------------
        stack = []
        bracket_dict = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for char in s:
            if char in bracket_dict:
                # Cleaner approach to deal with empty stack edge cases
                top_e = stack.pop() if stack else "#"
                if top_e != bracket_dict[char]:
                    return False
            else:
                stack.append(char)

        return not stack