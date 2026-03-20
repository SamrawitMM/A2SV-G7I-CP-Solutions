class NumArray:
    
    def __init__(self, nums: List[int]):
        self.prefix_sum = [0] * (len(nums) + 1)
        
        for i in range(len(nums)):
            self.prefix_sum[i] = self.prefix_sum[i-1] + nums[i]


    
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right] - self.prefix_sum[left - 1]

    
    
    
    
    
    


















    
    
    # def __init__(self, nums: List[int]):
    #     self.nums = nums
    #     for i in range(1, len(self.nums)):
    #         self.nums[i] += self.nums[i-1]

    #     self.nums.append(0)



        

    # def sumRange(self, left: int, right: int) -> int:
    #     return self.nums[right] - self.nums[left - 1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)