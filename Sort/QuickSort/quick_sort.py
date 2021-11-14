def quick_sort(list):
    # 基线条件：数组为空或者只有一个元素，直接返回即可
    if len(list) < 2:
        return list
    else:
        # 以首元素为基准值分区
        pivot = list[0]
        # 注意此时的遍历对象需要排除list[0]
        less = [i for i in list[1:] if i <= pivot]
        greater = [i for i in list[1:] if i > pivot]
        # 递归调用quick_sort
        return quick_sort(less) + [pivot] + quick_sort(greater)
