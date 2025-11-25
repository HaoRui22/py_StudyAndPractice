def findMinAndMax(L):
    if not L:
        return(None, None)
    minVal = maxVal = L[0]
    for x in L[1:]:
        if x < minVal:
            minVal = x
        elif x > maxVal:
            maxVal = x
    return(minVal, maxVal)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')