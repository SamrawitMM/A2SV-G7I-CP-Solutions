class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # where is that target located -> left or right

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = ( left + right ) // 2

            if nums[left] <= nums[mid]:
                
                if nums[left] <= target and target <= nums[mid]:
                    right = mid - 1

                else:
                    left = mid + 1

            elif nums[mid] < nums[right]:

                if nums[mid] <= target and target <= nums[right]:
                    left = mid + 1
   
                else:
                    right = mid - 1
            
            if target == nums[mid]:
                return mid

              
        return -1

        
        