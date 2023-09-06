def romanToInt(self, s: str) -> int:
    """
    (Optimal) 
    Time Complexity: O(n)
    Space Complexity: O(1) --> Fixed since roman numerals do not exceed 3999

    TODO: (Assumption that all s is valid)
    1. Form an array holding all roman numerals
    2. Iterate through the array
    3. Get the quotient and multiply with the roman numeral
    4. Append it to output
    5. Once end is reached, we return our output
    """
    roman = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    index = 0
    output = 0
    for e in roman: # Iterate through each
        while s[index: index+len(e[1])] == e[1]: # If not same we move on
            output += e[0]
            index += len(e[1])
    return output

    """
    Instead of listing everything down, we can use the minimum and minus
    when necessary

    Time Complexity: O(n)
    Space Complexity: O(1) --> Fixed since roman numerals do not exceed 3999

    TODO: (Assumption that all s is valid)
    1. Form dictionary holding all roman numerals
    2. Iterate through s
    3. Check if exists in our and handle any minuses that we need to perform before adding
    4. Once end is reached, we return our output
    """
    roman = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }

    index = 0
    output = 0
    while index < len(s):
        if index + 1 < len(s) and roman[s[index]] < roman[s[index+1]]:
            output -= roman[s[index]]
            output += roman[s[index+1]]
            index += 2
        
        elif s[index] in roman:
            output += roman[s[index]]
            index += 1
    return output