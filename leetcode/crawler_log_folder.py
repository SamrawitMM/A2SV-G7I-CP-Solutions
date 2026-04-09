class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        slashes = ['../', './']
        for f in logs:
            if f not in slashes:
                stack.append(f)
            
            elif f == slashes[0]:
                if stack:
                    stack.pop()

        return len(stack)
            
        
        
