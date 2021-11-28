def steal_samrtly(capacity: int, goods: dict):
    """
    :param capacity: 背包最大容量，int
    :param goods: 可偷的物品，dict，key为物品名称，value为依次存放物品价值和重量的list
    :return: dict:
    key=max_value:可偷得的最大价值;
    value=goods_steal:应该偷的物品集合；
    """
    n=len(goods)
    goods_list=[0]+list(goods.keys())
    goods_steal=[set() for i in range(capacity+1)]
    # good_steal[c]表示容量为c时，可偷得的最大价值物品集合

    # 创建动态规划网格:table，
    # 横坐标为 1，2，...capacity 的背包容量；纵坐标为 物品1,物品2....物品n
    # 表格中的值table[i][j]为 在容量大小是j，可偷物品为物品1至物品i的情况下可偷得的最大价值
    # 为便于索引与代表的容量和物品序列对应，首列和首行不放东西
    table=[[0 for col in range(capacity+1)] for row in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,capacity+1):
            current_good=goods_list[i]
            current_value=goods[current_good][0]
            current_weight=goods[current_good][1]
            # 计算如果偷当前物品，剩余的容量
            left_cap=j - current_weight
            # 根据容量情况，计算如果偷当前物品，可获得的价值，若容量超标，则无法偷该物品，价值记为0
            if left_cap>=0:
                v_steal_current_good=current_value+table[i-1][left_cap]
            else:
                v_steal_current_good=0
            # 目前可偷得最大值=（上一个单元格的值）与 （当前商品价值加上剩余空间最大值） 的较大值
            table[i][j] = max(table[i - 1][j], v_steal_current_good)
            if table[i][j]> table[i - 1][j]:
                # 如果当前最大值超过上一个单元格的值，肯定会偷当前物品
                # TO FIX
                # j=3时 有问题
                goods_steal[j].add(current_good)
                if left_cap>0:
                    # 如果偷完当前物品后仍有剩余空间，则加上剩余空间对应的应偷物品
                    goods_steal[j]=goods_steal[j] | goods_steal[left_cap]
                else:
                    # 如果偷完当前物品后没有剩余空间，需要仍掉之前偷的物品
                    goods_steal[j]=goods_steal[j] - goods_steal[j-1]
            else:
                if j>1:
                    goods_steal[j] = goods_steal[j-1]
                else:
                    goods_steal[j] = goods_steal[j]


    max_value=table[-1][-1]

    return {max_value:goods_steal[capacity]}



