class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        while tickets:
            tickets[0] -= 1
            count += 1

            if tickets[0] == 0 and k == 0:
                return count

            if tickets[0] > 0 :
                tickets.append(tickets.pop(0))

            else:
                tickets.pop(0)

            if k == 0 :
                k = len(tickets) - 1
            else:
                k -= 1

        return count
        
