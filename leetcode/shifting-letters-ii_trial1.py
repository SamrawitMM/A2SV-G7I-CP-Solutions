class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

            diff = [0] * (len(s)+1)

            for left, right, direction in shifts:

                if direction == 1:
                    diff[left] += 1
                    diff[right + 1] -= 1
                
                else:
                    diff[left] -= 1
                    diff[right + 1] += 1

            print(diff)
            s_list = list(s)
            current_shift = 0
            for i in range(len(s)):
                current_shift += diff[i]

                pos = (ord(s_list[i]) - ord('a') + current_shift + 26) % 26
                s_list[i] = chr(pos + ord('a'))

            
            return "".join(s_list)


                


                































        # diff = [0] * ( len(s) + 1)

        # for left, right, direction in shifts:
        #     if direction == 1:
        #         diff[left] += 1
        #         diff[right+1] -= 1
        #     elif direction == 0:
        #         diff[left] -= 1
        #         diff[right + 1] += 1

        # s_list = list(s)
        # current_shift = 0
        # for i in range(len(s)):
        #     current_shift += diff[i]
        #     shifted_pos = (ord(s_list[i]) - ord('a') + current_shift) % 26
        #     s_list[i] = chr(shifted_pos + ord('a'))
        
        # return ''.join(s_list)

    

            

             
        