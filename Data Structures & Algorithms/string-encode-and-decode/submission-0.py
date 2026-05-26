class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            x = len(s)
            encoded = encoded + '#' + str(x) + '#' + s
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []
        while i < len(s):
            i += 1
            num_str = ''
            while s[i] != '#':
                num_str += s[i]
                i += 1
            i += 1
            str_length = int(num_str)
            str_decode = s[i: i + str_length]
            decoded.append(str_decode)
            i += str_length
        return decoded
