# 使用贪婪算法求广播站覆盖问题的近似最优解

if __name__ == '__main__':

    # 使用集合set表示要覆盖的州，可以方便地计算重合的元素
    states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

    # 使用字典表示各广播站的覆盖州情况
    stations = {}
    stations["kone"] = set(["id", "nv", "ut"])
    stations["ktwo"] = set(["wa", "id", "mt"])
    stations["kthree"] = set(["or", "nv", "ca"])
    stations["kfour"] = set(["nv", "ut"])
    stations["kfive"] = set(["ca", "az"])

    final_stations = set()

    while states_needed:
        best_station = None
        states_covered = set()
        # 遍历剩余的广播站，找出可覆盖还需覆盖州数目做多的作为best station
        for station, states_for_station in stations.items():
            covered = states_needed & states_for_station
            if len(covered) > len(states_covered):
                states_covered = covered
                best_station = station

        final_stations.add(best_station)
        states_needed -= states_covered

    print(final_stations)
