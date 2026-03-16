class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_distance = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):

            x = nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = x + nums[left] + nums[right]
                
                if abs(current_sum - target) < abs(min_distance - target):
                    min_distance = current_sum

                if current_sum == target:
                    return current_sum

                elif current_sum > target:
                    right -= 1

                else:
                    left += 1

        return min_distance

            
            
            
        