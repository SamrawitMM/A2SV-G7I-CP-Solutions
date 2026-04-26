class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        # def firstPosition():
        #     left = 0
        #     right = n - 1
        #     while left <= right:
                
        #         mid_point = (left + right ) // 2

        #         if nums[mid_point] == target:

        #             if mid_point == 0 or nums[mid_point - 1] != target:
        #                 return mid_point

        #             else:
        #                 right = mid_point - 1
                
        #         elif nums[mid_point] < target:
        #             left = mid_point + 1

        #         else: 
        #             right = mid_point - 1

        #     return -1

        # def lastPosition():
        #     left = 0
        #     right = n - 1

        #     while left <= right:
        #         mid_point = (left + right) // 2

        #         if nums[mid_point] == target:
        #             if mid_point == n - 1 or nums[mid_point + 1] != target:
        #                 return mid_point

        #             else:
        #                 left = mid_point + 1

        #         elif nums[mid_point] < target:
        #             left = mid_point + 1

        #         else:
        #             right = mid_point - 1

        #     return -1

        
        # first = firstPosition()
        # last = lastPosition()

        # return [first, last]



        def first_position(nums, target):

            if not nums: return -1

            left = 0
            right = len(nums) - 1

            while left < right:

                mid = ( left + right ) // 2

                if nums[mid] < target:
                    left = mid + 1

                else:
                    right = mid

                
            return left if nums[left] == target else -1


        def last_position(nums, target):
            if not nums: return -1

            left = 0
            right = len(nums) -1 


            while left < right:
                mid = ( left + right + 1) // 2

                if nums[mid] > target:
                    right = mid  - 1

                else:
                    left = mid

            return left if nums[left] == target else -1 
 




        first = first_position(nums, target)
        last = last_position(nums, target)

        return [first, last] 