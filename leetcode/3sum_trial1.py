class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
     
        output = set()

        nums.sort()
        for i in range(len(nums)-2):
            x = nums[i]
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                sum = x + nums[left] + nums[right]

                if sum == 0:
                    output.add((x, nums[left], nums[right]))
                    left += 1
                    right -= 1

                elif sum > 0:
                    right -= 1
                
                elif sum < 0:
                    left += 1

         
        return [list(lst) for lst in output]     

            



        