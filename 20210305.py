# 百度-商业场景营销研发部-机器学习-一面

# 1、二叉树前序

# # 递归
# def foo(node):
#     if not node: return
#     foo(node.left)
#     foo(node.right)


# # 非递归
# tmp_list = []
# root_node = None
# tmp_list.append(root_node)
# result = []

# while tmp_list:
#     cur_node = tmp_list.pop()
#     result.append(cur_node.val)
#     tmp_list.append(cur_node.right)
#     tmp_list.append(cur_node.left)
    
    


# print(result)


# 2、插入排序 
# nums = [0, 4, 3, 5, 5, 2]
nums = [0, 0, 2, 5, 2]
nums_len = len(nums)

for i in range(nums_len - 1):
    for j in range(i+1, nums_len):
        
        if nums[j] < nums[i]:
            nums[i], nums[j] = nums[j], nums[i]
    print(nums)
print("-----result-----")
print(nums)
