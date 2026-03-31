class Solution:
    def validPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1

   
        flag1 = True
        flag2 = True
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1

            else:
                # senario 1
                l1 , r1 = left + 1, right
                # senario 2
                l2, r2 = left, right -1

                while l1 < r1:
                    if s[l1] == s[r1]:
                        l1 += 1
                        r1 -= 1

                    else:
                        flag1 = False
                        break

                
                while l2 < r2:
                    if s[l2] == s[r2]:
                        l2 += 1
                        r2 -= 1

                    else:
                        flag2 = False
                        break


                return flag1 or flag2

        return True
      