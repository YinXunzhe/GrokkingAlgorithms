# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':

    states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

    stations = {}
    stations["kone"] = set(["id", "nv", "ut"])
    stations["ktwo"] = set(["wa", "id", "mt"])
    stations["kthree"] = set(["or", "nv", "ca"])
    stations["kfour"] = set(["nv", "ut"])
    stations["kfive"] = set(["ca", "az"])

    final_stations = set()

    while states_needed:
        best_station=None
        states_covered=set()

        for station, states_for_station in stations.items():
            covered = states_needed & states_for_station
            if len(covered) > len(states_covered):
                states_covered=covered
                best_station = station

        final_stations.add(best_station)
        states_needed -=states_covered

    print(final_stations)

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
