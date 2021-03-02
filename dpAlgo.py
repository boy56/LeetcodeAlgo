# dp类算法套路

# leetcode 931 下降路径最小和
def minFallingPathSum(matrix: List[List[int]]) -> int:
    n = len(matrix)
    res = 66666
    memo = [[66666] * n for i in range(n)] # 根据题目要求, 最大值为10000, 所以初始值设置比10000大即可

    def dp(matrix, i, j):    
        if i < 0 or j < 0 or j >= len(matrix): return 99999 
        
        # base
        if i == 0:
            return matrix[0][j]
        
        # 根据备忘录消除重合子问题
        if memo[i][j] != 66666:
            return memo[i][j]
        
        # 状态转移
        memo[i][j] = matrix[i][j] + min(dp(matrix, i-1, j-1), dp(matrix, i-1, j), dp(matrix, i-1, j+1))
        return memo[i][j]

    # 主函数, 遍历最后一行的所有位置, 获取最小值
    for j in range(n):
        res = min(res, dp(matrix, n-1, j))
    return res