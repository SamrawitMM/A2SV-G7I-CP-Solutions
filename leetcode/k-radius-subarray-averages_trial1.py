class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        ans = [-1] * n
        window_size = 2 * k + 1

        sum_k = [0] * len(nums)
        sum_k[0] = nums[0]

        if window_size > n:
            return ans


        for j in range(1, len(nums)):
            sum_k[j] = sum_k[j-1] + nums[j]


        for i in range(k, n-k):
            left = i - k
            right = i + k

            window_sum = sum_k[right]
            if left > 0:
                window_sum -= sum_k[left -1]
            ans[i] = window_sum // window_size

        



        return ans

        