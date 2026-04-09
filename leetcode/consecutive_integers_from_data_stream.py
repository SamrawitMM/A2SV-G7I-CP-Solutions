from collections import deque
class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.q = deque()
        self.match = 0
        
        

    def consec(self, num: int) -> bool:
        self.q.append(num)

        if num == self.value:
            self.match += 1

        if len(self.q) > self.k:
            removed = self.q.popleft()

            if removed == self.value:
                self.match -= 1

        return len(self.q) == self.k and self.match == self.k


        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
