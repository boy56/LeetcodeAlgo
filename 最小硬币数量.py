# 面试公司: 金证优智
# 问题: 最小硬币数量
# 硬币面值: 1、6、10
# 总金额: n

n = 22 
min_count = n
coins = [1, 6, 10]
memo = [0] * (n + 1)


#总金额的遍历
for i in range(1, n+1):
    tmp_min = i
    # tmp_count = n
    for coin in coins: # 增加的硬币遍历
        if coin > i: continue # 硬币面值大于当前遍历金额
        if memo[i - coin] + 1 < tmp_min:
            tmp_min = memo[i - coin] + 1
    
    memo[i] = tmp_min
    
    # memo[i] = min(memo[i - 1] + 1, memo[i - 6] + 1, memo[i - 10] + 1)

print(memo[-1])