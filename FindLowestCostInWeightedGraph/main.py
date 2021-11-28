from find_lowest_cost import find_lowest_cost

if __name__ == '__main__':

    # 表示加权图的字典，
    # key为节点名称，value也是字典（key为可到的下一节点，value为到下一节点的开销）
    graph = {}
    graph["start"] = {}
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2
    graph["a"] = {}
    graph["a"]["fin"] = 1
    graph["b"] = {}
    graph["b"]["a"] = 3
    graph["b"]["fin"] = 5
    graph["fin"] = {}

    # 记录经当前节点可到达的节点的最小开销
    costs = {}
    infinity = float("inf")
    costs["a"] = 6
    costs["b"] = 2
    costs["fin"] = infinity

    # 记录最小开销时各节点的父节点
    parents = {}
    parents["a"] = "start"
    parents["b"] = "start"
    parents["fin"] = None

    # 第二组数据 7.1 A题
    # 表示加权图的字典，
    # key为节点名称，value为表示到下一节点的字典（key为下一节点，value为到此的开销）
    # graph = {}
    # graph["start"] = {}
    # graph["start"]["a"] = 2
    # graph["start"]["b"] = 5
    # graph["a"] = {}
    # graph["a"]["b"] = 8
    # graph["a"]["c"] = 7
    # graph["b"] = {}
    # graph["b"]["c"] = 2
    # graph["b"]["d"] = 4
    # graph["c"] = {}
    # graph["c"]["fin"] = 1
    # graph["d"]={}
    # graph["d"]["c"] = 6
    # graph["d"]["fin"] = 3
    # graph["fin"] = {}
    #
    # # 记录经当前节点可到达的节点的最小开销
    # costs = {}
    # infinity = float("inf")
    # costs["a"] = 2
    # costs["b"] = 5
    # costs["c"] =infinity
    # costs["d"] =infinity
    # costs["fin"] = infinity
    #
    # # 记录最小开销时各节点的父节点
    # parents = {}
    # parents["a"] = "start"
    # parents["b"] = "start"
    # parents["c"] = None
    # parents["d"] = None
    # parents["fin"] = None

    # 7.1 B
    # 表示加权图的字典，
    # key为节点名称，value为表示到下一节点的字典（key为下一节点，value为到此的开销）
    # graph = {}
    # graph["start"] = {}
    # graph["start"]["a"] = 10
    # graph["a"] = {}
    # graph["a"]["c"] =20
    # graph["c"]={}
    # graph["c"]["fin"]=30
    # graph["c"]["b"]=1
    # graph["b"] = {}
    # graph["b"]["a"] = 1
    # graph["fin"] = {}
    #
    # # 记录经当前节点可到达的节点的最小开销
    # costs = {}
    # infinity = float("inf")
    # costs["a"] =10
    # costs["b"] =infinity
    # costs["c"] =infinity
    # costs["fin"] = infinity
    #
    # # 记录最小开销时各节点的父节点
    # parents = {}
    # parents["a"] = "start"
    # parents["b"] = None
    # parents["c"] = None
    # parents["fin"] = None

    # 第二组数据 7.1 c题
    # 表示加权图的字典，
    # key为节点名称，value为表示到下一节点的字典（key为下一节点，value为到此的开销）
    # graph = {}
    # graph["start"] = {}
    # graph["start"]["a"] = 2
    # graph["start"]["b"] = 2
    # graph["a"] = {}
    # graph["a"]["fin"] = 2
    # graph["a"]["c"] = 2
    # graph["a"]["b"] = 2
    # graph["b"] = {}
    # graph["b"]["a"] = 2
    # graph["c"] = {}
    # graph["c"]["fin"] = 2
    # # 存在负权重，不再适用
    # graph["c"]["b"] = -1
    # graph["fin"] = {}
    #
    # # 记录经当前节点可到达的节点的最小开销
    # costs = {}
    # infinity = float("inf")
    # costs["a"] = 2
    # costs["b"] = 2
    # costs["c"] =infinity
    # costs["fin"] = infinity
    #
    # # 记录最小开销时各节点的父节点
    # parents = {}
    # parents["a"] = "start"
    # parents["b"] = "start"
    # parents["c"] = None
    # parents["fin"] = None

    ans=find_lowest_cost(graph,costs,parents)
    print(ans)

