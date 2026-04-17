class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pairs = [ [position[i] , speed[i]] for i in range(len(position))]

        stack = []
        for p, s in sorted(pairs)[::-1]:
            time = (target - p) / s

            if not stack or time > stack[-1]:
                stack.append(time)

        
        return len(stack)

