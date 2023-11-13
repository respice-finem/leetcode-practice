def sortVowels(s: str) -> str:
    """
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    
    TODO:
    1. We get all the ascii and their count. We then start from the replace the list with vowels at their index with the respective sorted vowel
    """
    s_arr = list(s)
    vowels = "AEIOUaeiou"
    vowel_stack = []
    pointer = 0

    for i in range(len(s_arr)):
        if s_arr[i] in vowels:
            vowel_stack.append(s_arr[i])
    vowel_stack.sort(reverse=True)

    for i in range(len(s_arr)):
        if s_arr[i] in vowels:
            s_arr[i] = vowel_stack.pop()

    return ''.join(s_arr)

    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    TODO:
    1. Count the words and place them in a dict. We then get form the sorted count array for the vowels via counting sort
    2. We then iterate through the string and replace the vowels based on the vowel stack
    3. We then return the output
    """
    w_ct = Counter(s)
    vowels = "AEIOUaeiou"
    vowel_stack = [w_ct[v] for v in vowels]
    left = 0
    output = []
    for i in range(len(s)):
        if s[i] not in vowels:
            output.append(s[i])
        else:
            while vowel_stack[left] <= 0 and left < len(vowel_stack):
                left += 1
            output.append(vowels[left])
            vowel_stack[left] -= 1
            
    return ''.join(output)