class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        maxCapacity = high

        def canCapacity(capacity):

            currCapacity = capacity
            currShip = 1
            for w in weights:
                if w > currCapacity:
                    currCapacity = capacity
                    currShip += 1

                currCapacity -= w

            return currShip <= days

        

        while low <= high:
            mid = (low + high) // 2

            if canCapacity(mid):
                high = mid - 1
                maxCapacity = min(maxCapacity, mid)

            else:
                low = mid + 1

        
        return maxCapacity

        

        