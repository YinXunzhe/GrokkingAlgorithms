from find_mango_seller import find_mango_seller

if __name__ == '__main__':
    # 使用散列表表示一度关系和二度关系形成的图
    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["jonny", "thom"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["jonny"] = []
    graph["thom"] = []

    ans = find_mango_seller(graph)
    print(ans)
