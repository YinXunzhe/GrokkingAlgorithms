def longest_common_subsequence(str1, str2):
    """
    找出两个字符串中的最长公共子序列的长度
    :param str1:字符串1
    :param str2: 字符串2
    :return:最长公共子序列的长度
    """
    m = len(str1)
    n = len(str2)
    if m > 0 and n > 0:
        table = [[0 for col in range(n)] for row in range(m)]
    else:
        return 0

    for i in range(m):
        for j in range(n):
            if str2[j] == str1[i]:
                if i > 0 and j > 0:
                    table[i][j] = table[i - 1][j - 1] + 1
                # 因为首行或者首列最多只有一个相同的公共子序列
                else:
                    table[i][j] = 1
            else:
                if i > 0 and j > 0:
                    table[i][j] = max(table[i - 1][j], table[i][j - 1])
                elif i == 0 and j > 0:
                    table[i][j] = table[i][j - 1]
                elif i > 0 and j == 0:
                    table[i][j] = table[i - 1][j]
                else:
                    table[i][j] = 0
    return table[-1][-1]
