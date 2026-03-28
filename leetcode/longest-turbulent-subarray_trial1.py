class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left = 0
        right = 1
        count = 1
        window_sum = 0
        max_turbulent = 1
        prev = ""

        while right < len(arr):

            if arr[right-1] < arr[right]:
                if prev != "<":
                    count += 1
                else:
                    count = 2
                prev = "<"


            elif arr[right-1] > arr[right]:
                if prev != ">":
                    count += 1
                else:
                    count = 2
                prev = ">"

            else:
                count = 1
                prev = "=" 
            
            max_turbulent = max(max_turbulent, count)

            right += 1



        return max_turbulent

        # return count



        