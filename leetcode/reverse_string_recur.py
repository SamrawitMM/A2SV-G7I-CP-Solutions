class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(s: List[str], start, end):

            if start >= end:
                return
                
            s[start], s[end] = s[end], s[start]
            return reverse(s, start + 1, end - 1)

        print(reverse(s, 0, len(s)-1))
            
        
        # left_pointer = 0
        # right_pointer = len(s) - 1

        # while left_pointer < right_pointer:
        #     s[left_pointer], s[right_pointer] = s[right_pointer], s[left_pointer]

        #     left_pointer += 1
        #     right_pointer -= 1
        
        # return s
            



        
