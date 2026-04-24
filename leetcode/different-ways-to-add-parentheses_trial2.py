class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:


        def recur(expression):

            res = []

            for i in range(0, len(expression)):
                op = expression[i]

                if op == '*' or op == '+' or op == '-':

                    a = expression[:i]
                    b = expression[i + 1 :]

                    nums1 = recur(a) 
                    nums2 = recur(b)

                    for n1 in nums1:
                        for n2 in nums2:

                            if op == '*':

                                res.append(n1 * n2)

                            elif op == '+':
                                
                                res.append(n1 + n2)

                            elif op == '-':

                                res.append(n1 - n2)

            if res == []:
                res.append(int(expression))
                
            return res



        return recur(expression)



# operation = ['+', '-', '*']
2 - 1 - 1
# minus(-) at index 1

# 1 split -> 2 -> 2
# 2nd split -> 1 - 1

# minus -
# 1 split 1
# 2nd split 1

2 - 1 - 1
# minus ( - ) at index 3

# 1 split = 2 - 1 -> [1]
# 2nd split - > 1 [1]

#minus - 
# 1 split = 2 -> int("2") -> [2]
# 2ns aplit = 1 - > int("1") -> [1]



# [2, 0]










































   # def recur(left, right):
        #     operations = {
        #     '*' : lambda x, y : x * y,
        #     '-' : lambda x, y : x - y,
        #     '+' : lambda x, y : x + y
        #     }

        #     res = []

        #     for i in range(left, right + 1):
        #         op = expression[i]

        #         if op in operations:

        #             nums1 = recur(left, i - 1)
        #             nums2 = recur(i + 1, right)

        #             for n1 in nums1:
        #                 for n2 in nums2:

        #                     res.append(operations[op](n1, n2))

        #     if res == []:
        #         res.append(int(expression[left:right+1]))
                
        #     return res



        # return recur(0, len(expression)-1)

            

        