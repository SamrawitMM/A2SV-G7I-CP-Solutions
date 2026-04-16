class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = ['+', '-', '*', '/']

        def calculate(x, y, o):
            if o == operations[0]:
                return x + y
            elif o == operations[1]:
                return x - y
            elif o == operations[2]:
                return x * y
            else:
                return int(x / y)

        stack = []
        for t in tokens:
            if t not in operations:
                stack.append(int(t))
            else:
                y = stack.pop()
                x = stack.pop()
                o = t

                num = calculate(x, y, o)
                stack.append(num)
            
        return stack[-1]

        
