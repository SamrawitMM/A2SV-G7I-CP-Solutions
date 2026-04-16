class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        output = [[1]]
        def pascal(rows, n):

            if n == rows:
                return output

            
            lst = [1] * (n+1)
                            
            for i in range(1, n):
                lst[i] = output[-1][i-1] + output[-1][i]

            output.append(lst)
            

            return pascal(rows, n + 1)

        
        return pascal(numRows, n = 1)
