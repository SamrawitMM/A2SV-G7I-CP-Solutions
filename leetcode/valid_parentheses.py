class Solution:
    def isValid(self, s: str) -> bool:

        braces = { ')': '(', ']': '[', '}' : '{'}
        stack = []
        for b in s:
            if b in braces :
                
                if stack and  stack[-1] == braces[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
            
        return True if len(stack) == 0 else False
        
