class Codec:
    """
    Non ASCII separator
    """
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        sep = str(chr(200))
        return sep.join(strs)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        sep = str(chr(200))
        return s.split(sep)

    """
    Chunked Transfer Encoding
    --> Answer from Editorial
    --> Industry standard

    Idea is that we separate our strings based on len and marking.
    This allows us to safely parse our data accordingly
    """
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        output = ""
        for s in strs:
            output += str(len(s)) + "/:" + s
        return output

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        output = []
        i = 0
        while i < len(s):
            delim = s.find("/:", i)
            length = int(s[i:delim])
            str_ = s[delim+2:delim+2+length]
            output.append(str_)
            i = delim + 2 + length
        return output


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))