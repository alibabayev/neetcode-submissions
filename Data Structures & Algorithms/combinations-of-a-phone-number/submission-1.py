class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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
    
        res = []
        
        def backtrack(i, curr_str):
            if len(curr_str) == len(digits):
                res.append(curr_str)
                return
        
            for ch in digitToChar[digits[i]]:
                backtrack(i+1, curr_str + ch)
            
        if digits:
            backtrack(0, "")
            
        return res
        
        