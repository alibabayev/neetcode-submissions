class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0

        stack = []
        operators = {'+', '-', '/', '*'}

        for token in tokens:
            if token in operators:
                r, l = stack.pop(), stack.pop()
                if token == '+':
                    stack.append(l + r)
                elif token == '-':
                    stack.append(l - r)
                elif token == '*':
                    stack.append(l * r)
                else:
                    division = abs(l) // abs(r)

                    if (l < 0) ^ (r < 0):
                        division *= -1
                    stack.append(division)
            else:
                stack.append(int(token))

        return stack[-1]