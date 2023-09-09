def evalRPN(tokens: List[str]) -> int:
    """
    Two Pointers in Place
    --> Answer here is from editorial
    --> Feels like there is a O(n) solution but
    --> lots of effort to deal with the in-place movements
    Time Complexity：O(n^2)
    Space Complexity: O(1) --> interviewer may ask what is space optimal of doing so

    TODO:
    1. Iterate through the numbers
    2. Once we hit an operator, we perform operation on index and index-1 (guaranteed to be numbers)
    3. Replace them on the operator
    4. Pop the two numbers from index and index-1
    5. Set the index to be -1 since (curr_index - 2 + 1) = curr_index - 1
    6. Repeat until one element is left
    7. Return the element
    """
    curr_pos = 0

    while len(tokens) > 1:

        while tokens[curr_pos] not in "+-*/":
            curr_pos += 1
        
        operator = tokens[curr_pos]
        n1 = int(tokens[curr_pos - 2])
        n2 = int(tokens[curr_pos - 1])

        if operator == "+":
            tokens[curr_pos] = n1 + n2
        elif operator == "-":
            tokens[curr_pos] = n1 - n2
        elif operator == "*":
            tokens[curr_pos] = n1 * n2
        else:
            tokens[curr_pos] = int(n1/n2)
        tokens.pop(curr_pos - 2)
        tokens.pop(curr_pos - 2)
        curr_pos -= 1
    return tokens[0]

    """
    (Stacks)
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. Instantiate empty stack
    2. If number push into stack
    3. If operands, we take out the two numbers and perform operand before putting it in
    4. Repeat until one number remains
    """
    stack = []
    for t in tokens:
        if t.isnumeric() or (t[0] == "-" and len(t) > 1):
            stack.append(int(t))
        else:
            t1 = stack.pop()
            t2 = stack.pop()
            if t == "+":
                stack.append(t2+t1)
            elif t == "-":
                stack.append(t2-t1)
            elif t == "*":
                stack.append(t2*t1)
            elif t == "/":
                stack.append(int(t2/t1)) # // Floor would round to smallest integer as it is non 0
    return stack[0]
            
    """
    Cleaner Implementation
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    stack = []

    for t in tokens:
        if t not in "+-/*":
            stack.append(int(t))
            continue
        t1 = stack.pop()
        t2 = stack.pop()
        if t == "+":
            result = t2+t1
        elif t == "-":
            result = t2-t1
        elif t == "*":
            result = t2*t1
        elif t == "/":
            result = int(t2/t1) # // Python Floor does not truncate to 0
        stack.append(result)
    return stack.pop()