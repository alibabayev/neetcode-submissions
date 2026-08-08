class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        res = []

        for word in words:
            current = root
            for c in word:
                if c not in current.children:
                    current.children[c] = TrieNode()
                current = current.children[c]
            current.word = word
            
        def dfs(r, c, node):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return
            
            ch = board[r][c]

            if ch not in node.children:
                return
            
            next_node = node.children[ch]

            if next_node.word:
                res.append(next_node.word)
                next_node.word = None
            
            
            board[r][c] = "#"
            
            dfs(r + 1, c, next_node)
            dfs(r - 1, c, next_node)
            dfs(r, c + 1, next_node)
            dfs(r, c - 1, next_node)

            board[r][c] = ch


        
        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, root)

        return res
        