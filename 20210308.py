# 百度-商业场景营销研发部-机器学习-二面

# 1、插入新值、删除最新、返回已存储空间中数据最大值
time_stack = [] # 按照时间插入
# value_list = [] # 按照值进行排列
max_value = -10000

# tmp.append()
def insert(value):
    # O(1) 插入
    time_stack.append(value)
    if value > max_value: max_value = value

# tmp.pop()
def delete(value):
    time_stack.pop()
    # O(n) 修改max
    
    # max_value = new_value


# max
def get_max():
    # O(1) or O(n)
    return max_value



#2、 删除倒数第N个节点

def get_n_node(root_ptr, n):
    first_ptr = root_ptr
    second_ptr = root_ptr
    # n = 6

    for i in range(n):
        if first_ptr.next: first_ptr = first_ptr.next
        elif i == n-1: 
            root_ptr = root_ptr.next
            return root_ptr
        else: return None

    while first_ptr.next:
        first_ptr = first_ptr.next
        second_ptr = second_ptr.next

    second_ptr.next = second_ptr.next.next

    # first_ptr.next = None
    return root_ptr

