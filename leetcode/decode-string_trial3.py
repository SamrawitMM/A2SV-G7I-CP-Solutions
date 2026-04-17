class Solution:
    def decodeString(self, s: str) -> str:

        # stack = []
        # for char in s:

        #     if char != ']':
        #         stack.append(char)

        #     else:
        #         curr_str = ""
        #         while stack and stack[-1] != '[':
        #             curr_str = stack.pop() + curr_str

        #         stack.pop()

        #         curr_num = ''
        #         while stack and stack[-1].isdigit():
        #             curr_num = stack.pop() + curr_num

                
        #         stack.append(int(curr_num) * curr_str)

        
        # return "".join(stack)
                


   
        # Recurssion

        def recur(s, inx):
            output = ""
            times = ""

            while inx < len(s):
                
                if s[inx].isdigit():
                    times += s[inx]
                
                elif s[inx] == '[':
                    sub, nxt_inx = recur(s, inx+1)
                    output += int(times) * sub
                    inx = nxt_inx
                    times = ""


                elif s[inx] == ']':
                    return output, inx

                else:
                    output += s[inx]

                inx += 1

            return output


        return recur(s, 0)
    
        



