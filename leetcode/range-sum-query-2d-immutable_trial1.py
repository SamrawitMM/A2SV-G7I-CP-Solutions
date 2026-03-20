class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        
        r = len(self.matrix)
        c = len(self.matrix[0])
        self.prefix_sum = [ [0] * (c+1) for _ in range(r+1)]

        for i in range(r):
            for j in range(c):
                self.prefix_sum[i+1][j+1] = self.prefix_sum [i+1][j] + self.prefix_sum[i][j+1] - self.prefix_sum[i][j] + self.matrix[i][j]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        return self.prefix_sum[row2+1][col2+1] - self.prefix_sum[row1][col2+1] - self.prefix_sum[row2+1][col1] + self.prefix_sum[row1][col1]


























    
    # def __init__(self, matrix: List[List[int]]):
    #     self.matrix = matrix

    #     r = len(matrix)
    #     c = len(matrix[0])
    #     self.prefix_sum = [[0]*(c+1) for _ in range(r+1)]

        
    #     for i in range(r):
    #         for j in range(c):
    #             self.prefix_sum[i+1][j+1] = self.prefix_sum[i][j+1]+ self.prefix_sum[i+1][j] - self.prefix_sum[i][j] + self.matrix[i][j]

    #     # print(*self.prefix_sum)
        

    # def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    #     top_i = row1
    #     top_j = col2 + 1

    #     left_i = row2 + 1
    #     left_j = col1

    #     diagonal_i = row1
    #     diagonal_j = col1

    #     return self.prefix_sum[row2+1][col2+1] - self.prefix_sum[top_i][top_j] - self.prefix_sum[left_i][left_j] + self.prefix_sum[diagonal_i][diagonal_j] 

        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)