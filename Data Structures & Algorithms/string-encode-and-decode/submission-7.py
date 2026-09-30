class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for string in strs:
            encoded_str = encoded_str + "sl:" + "{:3d}".format(len(string)) + ":" + string
        return encoded_str
    def decode(self, s: str) -> List[str]:
        lst = []
        length_length = 0
        for i in range(3,len(s)):
            if s[i-3] + s[i-2] + s[i-1] == "sl:":
                length = s[i:i+3]
                lst.append(s[i+4:i+4 + int(length)])
        return lst
