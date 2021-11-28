def steal_samrtly(capacity: int, goods: dict):
    """
    :param capacity: 背包最大容量，int
    :param goods: 可偷的物品，dict，key为物品名称，value为依次存放物品价值和重量的list
    :return: dict:
    key=max_value:可偷得的最大价值;
    value=goods_steal:应该偷的物品集合；
    """
    n = len(goods)
    goods_list = [0] + list(goods.keys())
    goods_steal = set()  # good_steal:可偷得的最大价值物品集合

    # 创建动态规划网格:table，
    # 横坐标为 1，2，...capacity 的背包容量；纵坐标为 物品1,物品2....物品n
    # 表格中的值table[i][j]为 在容量大小是j，可偷物品为物品1至物品i的情况下可偷得的最大价值
    # 为便于索引与代表的容量和物品序列对应，首列和首行不放东西
    table = [[0 for col in range(capacity + 1)] for row in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            current_good = goods_list[i]
            current_value = goods[current_good][0]
            current_weight = goods[current_good][1]
            # 计算如果偷当前物品，剩余的容量
            left_cap = j - current_weight
            # 根据容量情况，计算如果偷当前物品，可获得的价值，若容量超标，则无法偷该物品，价值记为0
            if left_cap >= 0:
                v_steal_current_good = current_value + table[i - 1][left_cap]
            else:
                v_steal_current_good = 0
            # 目前可偷得最大值=（上一个单元格的值）与 （当前商品价值加上剩余空间最大值） 的较大值
            table[i][j] = max(table[i - 1][j], v_steal_current_good)

    max_value = table[-1][-1]

    # 回溯应该偷的物品
    i = n
    j = capacity
    while i > 0:
        if table[i][j] > table[i - 1][j]:
            # 如果当前最大值超过上一个单元格的值，肯定偷了当前物品
            stolen_good = goods_list[i]
            goods_steal.add(stolen_good)
            i -= 1
            j -= goods[stolen_good][1]
        else:
            # 否则未偷该物品，继续回溯前一步的物品状态
            i -= 1

    return {max_value: goods_steal}
