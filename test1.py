def getRow(rowIndex):
    results = [[1]]
    for i in range(1, rowIndex + 1):
        result = []
        for j in range(i + 1):
            if j == 0 or j == i:
                result.append(1)
            else:
                result.append(results[-1][j - 1] + results[-1][j])
        results.append(result)
    return results[-1]

aaa = getRow(3)
