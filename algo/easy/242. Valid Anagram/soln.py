def isAnagram(s: str, t: str) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(1) --> Since only 26 alphanumeric chars

        TODO:
        1. Check if s and t are same length. Fail if not
        2. Count the chars in s and store in dict
        3. Run through t and remove chars. Fail exceed limit for chars
        4. Check if there are any remaining vals
        """
        if len(s) != len(t):
            return False

        char_dict =  {}
        for char in s:
            if char not in char_dict:
                char_dict[char] = 1 
            else:
                char_dict[char] += 1
        
        for char in t:
            if char not in char_dict:
                return False
            else:
                char_dict[char] -= 1
                if char_dict.get(char) == 0:
                    del char_dict[char]

        return not char_dict