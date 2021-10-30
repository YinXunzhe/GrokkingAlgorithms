def find_lowest_cost():
    """
    在权重图中找到最小开销
    :return:
    """
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

    costs={}
    infinity=float("inf")
    costs["a"]=6
    costs["b"]=2
    costs["fin"]=infinity

    parents={}
    parents["a"]="start"
    parents["b"]="start"
    parents["fin"]=None

    covered=[]

    # 找出最低开销的节点
    node=find_lowest_cost_node(graph)
    # 计算该节点邻居的开销
    for neighbor in node.key():
        cost=neighbor[node]

# TODO
def find_lowest_cost_node(graph):
    return node
