class Solution:
    def isPalindrome(self, s: str) -> bool:
        # reversed_s = s.lower().strip()
        # reversed_s = [char for char in reversed_s if char.isalnum()]
        # if "".join(reversed_s[::-1]) == "".join(reversed_s):
        #     return True
        # else:
        #     return False

        # using left and right pointers

        left = 0
        right = len(s)-1

        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1

        return True

            
        