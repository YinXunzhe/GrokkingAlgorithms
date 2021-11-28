# 冒泡排序
# 基本思想：从数组末端开始两两比较，若前面的大于后面的，则交换，这样最小的便排到最前面，到达前面后继续排下一轮
def bubble_sort(list):
    l = len(list)
    for i in range(l):
        for j in range(l - 1, i, -1):
            if list[j] < list[j - 1]:
                list[j - 1], list[j] = list[j], list[j - 1]
    return list
