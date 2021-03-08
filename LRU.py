# 面试公司: 金证优智
# 算法题目: lru
# 时间: 20210304
n = 10
memo = [-1] * n 
memo_flag = [-1] * n
memo_dict = {} # {key: (value, pos)}

# 插入值
def set(key, value):
    
    max_count = -1 # 设置最大值
    max_pos = -1
    cur_pos = -1

    if key in memo_dict: # 当前查询已经在内存中
        cur_pos = memo_dict[key][1]
        memo_dict[key] = value
        # memo_flag[cur_pos] = 0
    else: # 当前查询未在内存中
        
        # 遍历查找是否存在空内存, 如果不存在找出较长时间为用的内存
        for i in range(n):
            if memo_flag[i] == -1:
                memo[i] = key
                memo_dict[key] = (value, i)
                # memo_flag[i] = 0
                cur_pos = i
                break
            else:
                if memo_flag[i] > max_count:
                    max_count = memo_flag[i]
                    max_pos = i

        # 值已经插入 or 内存已满
        if cur_pos == -1: # 内存已满
            cur_pos = max_pos
            # memo_flag[cur_pos] = 0
            del memo_dict[memo[cur_pos]]

            memo[cur_pos] = key
            memo_dict[key] = (value, cur_pos)
    
    # 更新其他内存的占用时长
    for i in range(n):
        if i == cur_pos:
            memo_flag[i] = 0
            continue
        if memo_flag[i] != -1:
            memo_flag[i] += 1
        
    
def get(key):
    if key in memo_dict:
        return memo_dict[key][0]
    else:
        return None

