class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        i = len(arr) - 1
        # new length
        j = len(arr) - 1 + arr.count(0)

        while i >= 0:
            # only interested in the range 
            # of the original length after modification
            if j < len(arr):
                arr[j] = arr[i]
            if arr[i] == 0:
                j -= 1
                # same here
                if j < len(arr):
                    arr[j] = 0

            i -= 1
            j -= 1

        return arr



        