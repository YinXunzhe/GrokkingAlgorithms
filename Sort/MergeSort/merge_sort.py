# merge_sort()，每一步对半拆解成两个子列表，
# 递归调用直到分解出的子列表只含一个元素，然后调用merge()对子列表反过来进行合并
def merge_sort(list):
    n = len(list)
    if n == 1:
        return list
    else:
        m = n // 2
        list1 = merge_sort(list[:m])
        list2 = merge_sort(list[m:])
        merge(list1, list2)


def merge(list1, list2):
    m = len(list1)
    n=len(list2)
    merged_list=[]
    i=j=0
    k=0

    while i<m and j<n:
        if list1[i]>list2[j]:
            merged_list[k]=list2[j]
            j+=1
        else:
            merged_list[k]=list1[i]
            i+=1
        k+=1
    return merged_list


