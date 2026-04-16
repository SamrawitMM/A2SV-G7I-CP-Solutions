class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        output = [[1]]

        def pascal(inx, n):

            if n > inx:
                return output[-1]


            lst = [1] * (n+1)

            for i in range(1, n):
                lst[i] = output[-1][i-1] + output[-1][i]

            output.append(lst)

            return pascal(inx, n + 1)

        return pascal(rowIndex, 1)

            


        
