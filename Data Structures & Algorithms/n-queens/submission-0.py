class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [
            ["."] * n 
            for _ in range(n)
        ]

        columns = set()
        main_diagonals = set()
        anti_diagonals = set()


        def backtrack(row):
            if row == n:
                res.append([
                    "".join(board_row)
                    for board_row in board
                ])
                return

            for column in range(n):
                main_diagonal = row - column
                anti_diagonal = row + column
                if (
                    column in columns or 
                    main_diagonal in main_diagonals or 
                    anti_diagonal in anti_diagonals
                ):
                    continue

                columns.add(column)
                main_diagonals.add(main_diagonal)
                anti_diagonals.add(anti_diagonal)
                board[row][column] = "Q"

                backtrack(row + 1)

                columns.remove(column)
                main_diagonals.remove(main_diagonal)
                anti_diagonals.remove(anti_diagonal)
                board[row][column] = "."

        backtrack(0)
        return res

        
