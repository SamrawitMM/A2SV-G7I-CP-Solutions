class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        

        def place_ball(distance):

            balls = 1

            prev_position = position[0]
            count = 0

            placed = False
            for i in range(1, len(position)):
                if position[i] - prev_position >= distance:

                    balls += 1
                    prev_position = position[i]

                    if balls >= m:
                        return True
                        

            return False




        position.sort()

        left = 1
        right = position[-1] - position[0]

      

        while left < right:

            mid = (left + right + 1) // 2

            if place_ball(mid):
                left = mid
           


            else:
                right = mid - 1


        return left

    



        