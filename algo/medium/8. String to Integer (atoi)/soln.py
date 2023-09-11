def myAtoi(s: str) -> int:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. Set a check to start parsing for nums. Iterate through our string
    2. We start parsing when we see a +/- before a numeric string or just numeric string
    3. We stop once we reach a non numeric
    4. Return our int
    """
    to_parse = True
    output = ""

    for i in range(len(s)):
        if not to_parse:
            break
        elif s[i].isnumeric():
            if i+1 < len(s) and not s[i + 1].isnumeric():
                to_parse = False
            output += s[i]
        elif s[i] == " ":
            continue
        elif s[i] == '+' or s[i] == '-':
            if i+1 < len(s) and s[i + 1].isnumeric():
                output += s[i]
            else:
                break
        # If current is numeric and next is non-numeric to_parse is False
        else:
            break
    output = int(output) if output else 0
    output = min(max(-2**31, output), 2**31 -1)
    return int(output) if output else 0

    """
    Cleaner Implementation

    Time Complexity: O(n)
    Space Complexity: O(1)

    TODO:
    1. Same as above
    2. Instead of storing as string, which will take up space
    3. We use 10 * val
    """
    to_parse = True
    output = 0
    is_nega = False

    for i in range(len(s)):
        if not to_parse:
            break
        elif s[i].isnumeric():
            if i+1 < len(s) and not s[i + 1].isnumeric():
                to_parse = False
            output = 10 * output + int(s[i]) # Important method to approach int in strings
        elif s[i] == " ":
            continue
        elif s[i] == '+' or s[i] == '-':
            if i+1 < len(s) and s[i + 1].isnumeric():
                is_nega = s[i] == "-"
            else:
                break
        # If current is numeric and next is non-numeric to_parse is False
        else:
            break
    output = output * -1 if is_nega else output
    output = min(max(-2**31, output), 2**31 -1)
    return output