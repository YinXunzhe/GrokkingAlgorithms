# 记录已经处理过的节点
processed = []

def find_lowest_cost(graph,costs,parents):
    """
    在权重图中找到最小开销
    :return:
    """
    # 找到开销表中还未处理过且为最小开销的节点
    node=find_lowest_cost_node(costs)
    # 只要开销表中还有未处理过的，就进行计算
    while node is not None:
        neighbors=graph[node]
        # 计算该节点邻居的开销
        for neighbor in neighbors.keys():
            # 开销包括到当前节点的历史开销加上到节点邻居的开销
            cost=costs[node]+neighbors[neighbor]
            # 若找到了新的最小开销，更新开销表和父节点
            if cost<costs[neighbor]:
                costs[neighbor]=cost
                parents[neighbor]=node
        # 将该节点加入检查过的表
        processed.append(node)
        # 继续查找
        node=find_lowest_cost_node(costs)
    # 所有节点检查过后
    return costs["fin"]

def find_lowest_cost_node(costs):
    """
    在开销表中寻找最小开销的节点
    :param costs:开销表
    :return:
    """
    lowest_cost=float("inf")
    lowest_cost_node=None
    for node,cost in costs.items():
        # 如果当前节点未被处理过 且 开销低于目前记录的最低开销
        if node not in processed and cost<lowest_cost:
            # 就将该节点视为最小开销的节点
            lowest_cost_node=node
            lowest_cost=cost
    return lowest_cost_node
