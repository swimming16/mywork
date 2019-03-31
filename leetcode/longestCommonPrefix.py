def longestCommonPrefix( strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    res = ""
    if len(strs) == 0:
        return ""
    for each in zip(*strs):#zip(*strs)类似解压，每个单词相同位置的字母构成一组
        print(each)
        if len(set(each)) == 1:#利用集合创建一个无序不重复元素集
        	res += each[0]
    else:
        return res
print(longestCommonPrefix(["flower","flow","flight"]))