def binary_search(list,item):
    # 在list中找到item
    low=0
    high=len(list)-1
    while(low<=high):
        mid = low + (high - low) // 2
        guess = list[mid]
        if guess==item:
            return mid
        elif guess>item:
            high=mid-1
        else:
            low=mid+1
    return None