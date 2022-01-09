def longest_common_substring_opt(str1, str2):
    """
    找出两个字符串中的最长公共子串的长度
    优化：在状态更新的过程中，我们只用到了dp[i-1][j-1]的值，所以可以只使用一个变量来记录dp[i-1][j-1]的值。
    :param str1:字符串1
    :param str2: 字符串2
    :return:最长公共子串的长度
    """
    m = len(str1)
    n = len(str2)
    if m > 0 and n > 0:
        # l定义为以str1[i]和str2[j]结尾的公共子串的最长公共子串长度
        # 若str2[j] != str1[i]，以str1[i]和str2[j]结尾不可能组成公共子串，此时长度为0
        l, maxlen = -1, 0
        row = 0
        col = n - 1
    else:
        return 0
    # 因为遍历对角线起点时，打算先遍历列再遍历行，所以行的循环约束放在最外面
    while row < m:
        # 遍历以[i][j]开头的对角线
        i = row
        j = col
        while i < m and j < n:
            if str2[j] == str1[i]:
                if i > 0 and j > 0:
                    l += 1
                # 因为首行或者首列最多只有一个相同的公共子串
                else:
                    l = 1
                maxlen = max(l, maxlen)
            else:
                l = 0
            i += 1
            j += 1
        # 遍历完一条对角线后，先从右上角的对角线起点开始遍历,再从上到下遍历每一行的对角线起点
        if col > 0:
            # col还没到最左端时，列从右向左走遍历第一行的每条对角线
            col -= 1
        else:
            # col走到最左端后，说明第一行以每列开头的对角线已经遍历完了，开始走下一行
            row += 1

    # 返回记录的最大len
    return maxlen
