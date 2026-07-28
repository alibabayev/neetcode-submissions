class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        start = 0
        while start < len(s):
            end = start
            while s[end] != "#":
                end += 1
            length = int(s[start : end])
            start = end + 1
            end = start + length
            res.append(s[start : end])
            start = end
        return res
            
            
