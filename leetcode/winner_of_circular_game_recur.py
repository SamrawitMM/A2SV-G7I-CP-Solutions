class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        arr = list(range(1, n+1))
        def recu(arr, k, start):
            if len(arr) == 1:
                return arr[0]

            next_start = ((start + k - 1) % len(arr))
            del arr[next_start]

            return recu(arr, k, next_start)

        return recu(arr, k, 0)
