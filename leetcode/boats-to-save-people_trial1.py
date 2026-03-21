class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l = 0
        r = len(people) - 1
        boats = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1

            r -= 1
            boats += 1

        return boats

            
































        # people.sort()
        # n = len(people)
        
        # left = 0
        # right = n - 1
        # boats = 0

        # while left <= right:
        #     if people[right] + people[left] <= limit:
        #         left += 1
            
        #     right -= 1
        #     boats += 1

        # return boats
            

        