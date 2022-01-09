def longest_common_substring(str1, str2):
    """
    找出两个字符串中的最长公共子串的长度
    :param str1:字符串1
    :param str2: 字符串2
    :return:最长公共子串的长度
    """
    m = len(str1)
    n = len(str2)
    if m > 0 and n > 0:
        table = [[0 for col in range(n)] for row in range(m)]
    else:
        return 0
    # table[i][j]状态定义为以str1[i]和str2[j]结尾的公共子串的最长公共子串长度
    # 若str2[j] != str1[i]，以str1[i]和str2[j]结尾不可能组成公共子串，此时长度为0
    for i in range(m):
        for j in range(n):
            if str2[j] == str1[i]:
                if i > 0 and j > 0:
                    table[i][j] = table[i - 1][j - 1] + 1
                # 因为首行或者首列最多只有一个相同的公共子串
                else:
                    table[i][j] = 1
            else:
                table[i][j] = 0
    # 注意此处是寻找表中的最大值，而非最后一个元素
    return max(max(row) for row in table)
