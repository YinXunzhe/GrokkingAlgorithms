# 冒泡排序
# 基本思想：从数组末端开始两两比较，若前面的大于后面的，则交换，这样最小的便排到最前面，到达前面后继续排下一轮
def bubble_sort(list):
    for i in range(len(list)-1):
        l=len(list[i:])-1
        for j in range(l,0,-1):
            if list[j]<list[j-1]:
                temp=list[j-1]
                list[j-1]=list[j]
                list[j]=temp
    return list