class Solution:
    # Iterative
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        res = [""]   
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
            }
        
        for d in digits:
            new_strs = []
            for s in res:
                for ch in digitToChar[d]:
                    new_strs.append(s + ch)
            res = new_strs
        return res    