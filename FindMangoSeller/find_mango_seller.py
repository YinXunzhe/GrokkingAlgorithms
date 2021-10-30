from collections import deque


def find_mango_seller(graph):
    """
    使用广度优先搜索算法找到我的人脉中销售芒果的人
    :param graph: 散列表，表示人际关系图
    :return: string（*** is a mango seller!） or False
    """
    # 记录检查过的人，防止反向关系导致死循环
    checked_person = []
    # 创建一个队列，记录依次待检查的人
    search_queue = deque()
    search_queue += graph["you"]
    while search_queue:
        person = search_queue.popleft()
        if person not in checked_person:
            if is_mango_seller(person):
                return person + " is a mango seller!"
            else:
                checked_person += person
                search_queue += graph[person]
    return False


def is_mango_seller(name):
    return name[-1] == "m"