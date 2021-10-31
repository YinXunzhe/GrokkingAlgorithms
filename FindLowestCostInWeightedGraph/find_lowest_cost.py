# 记录已经处理过的节点
processed = []

def find_lowest_cost():
    """
    在权重图中找到最小开销
    :return:
    """
    # 表示加权图的字典，
    # key为节点名称，value为表示到下一节点的字典（key为下一节点，value为到此的开销）
    graph={}
    graph["start"]={}
    graph["start"]["a"]=6
    graph["start"]["b"]=2
    graph["a"]={}
    graph["a"]["fin"]=1
    graph["b"]={}
    graph["b"]["a"]=3
    graph["b"]["fin"]=5
    graph["fin"]={}

    # 记录经当前节点可到达的节点的最小开销
    costs={}
    infinity=float("inf")
    costs["a"]=6
    costs["b"]=2
    costs["fin"]=infinity

    # 记录最小开销时各节点的父节点
    parents={}
    parents["a"]="start"
    parents["b"]="start"
    parents["fin"]=None

    # 找到开销表中还未处理过且为最小开销的节点
    node=find_lowest_cost_node(costs)
    # 只要开销表中还有未处理过的，就进行计算
    while node is not None:
        # 计算该节点邻居的开销
        for neighbor in graph[node].keys():
            # 开销包括到当前节点的历史开销加上到节点邻居的开销
            cost=costs[node]+graph[node][neighbor]
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
# TODO
def find_lowest_cost_node(costs):
    lowest_cost=float("inf")
    lowest_cost_node=None
    for node,cost in costs.items():
        if node not in processed and cost<lowest_cost:
            lowest_cost_node=node
            lowest_cost=cost
    return lowest_cost_node
