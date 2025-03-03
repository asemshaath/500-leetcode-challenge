class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = '/*-+'

        for token in tokens:
            if token in operators:
                rhs = stack.pop()
                lhs = stack.pop()
                if token == '+':
                    r = int(rhs) + int(lhs)
                elif token == '*':
                    r = int(rhs) * int(lhs)
                elif token == '/':
                    r = int(int(lhs) / int(rhs))
                elif token == '-':
                    r = int(lhs) - int(rhs)
                stack.append(str(r))
            else:
                stack.append(token)
        return int(stack[0])



