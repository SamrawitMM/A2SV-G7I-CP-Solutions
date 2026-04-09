class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        
        dic = {}

        for num in nums2:
            while stack and stack[-1] < num:
                dic[stack[-1]] = num
                stack.pop()

            stack.append(num)

        result = []
        for num in nums1:
            if num in dic:
                inx = dic[num]
                result.append(inx)
            else:
                result.append(-1)


        return result





        
