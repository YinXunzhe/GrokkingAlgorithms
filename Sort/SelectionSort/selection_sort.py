def find_smallest(list):
    # 返回列表中最小值的索引
    min=list[0]
    index=0
    for i in range(1,len(list)):
        if list[i]<min:
            min=list[i]
            index=i
    return index

def selection_sort(list):
    sorted_list=[]
    while(len(list)!=0):
        smallest_index=find_smallest(list)
        # 把最小的元素从原数组中弹出，并放入新的数组
        sorted_list.append(list.pop(smallest_index))
    return sorted_list