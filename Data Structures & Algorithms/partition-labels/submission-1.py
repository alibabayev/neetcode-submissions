class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        
        for i, ch in enumerate(s):
            last[ch] = i
        
        res = []
        size = 0
        end = 0

        for i, ch in enumerate(s):
            size += 1
            end = max(end, last[ch])

            if i == end:
                res.append(size)
                size = 0
            
        return res
                

