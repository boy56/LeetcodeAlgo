# 面试部门: 京东搜索
# 问题: 二叉树直径
# 时间: 20200301

class TreeNode:
    def __init__(self):
        self.value = 0
        self.left = None
        self.right = None

root_node = None
cur_node = root_node

res = [] # 最大层的节点列表
res_num = 0 # 最大层的数量

tmp_squeue = [root_node]
curdepth_num = 1

while tmp_squeue:
    nextdepth_num = 0
    nextdepth_nodes = []

    for i in range(curdepth_num):
        cur_node = tmp_squeue.pop(0)

        if cur_node.left: 
            tmp_squeue.append(cur_node.left)
            nextdepth_num += 1
            nextdepth_nodes.append(cur_node.left)

        if cur_node.right: 
            tmp_squeue.append(cur_node.right)
            nextdepth_num += 1
            nextdepth_nodes.append(cur_node.right)

    if nextdepth_num > res_num:
        res_num = nextdepth_num
        res = nextdepth_nodes
    
    curdepth_num = nextdepth_num 
    

# 查找最大值然后输出列表


