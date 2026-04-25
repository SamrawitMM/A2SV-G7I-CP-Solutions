class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []
        for a in asteroids:

            destroyed = False

            while stack and a < 0 and stack[-1] > 0:

                if abs(a) > abs(stack[-1]):
                    stack.pop()
                    continue

                elif abs(a) == abs(stack[-1]):
                    stack.pop()
                    destroyed = True
                    break

                else:
                    destroyed = True
                    break
                
            

            
            if not destroyed:
                stack.append(a)

        return stack





            


        