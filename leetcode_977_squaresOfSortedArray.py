def sortedSquares(A):
    result = []
    for num in A:
        result.append(num*num)
        for i in range(len(result)):
            for j in range(i):
                if result[j] > result[i]:
                    result[j], result[i] = result[i], result[j]
    return result

def sortedSquaresInternet(A):
    result = []
    negativeList = []
    for num in A:
        if num < 0:
            negativeList.append(num*-1)
        else:
            while negativeList and num > negativeList[-1]:
                number = negativeList.pop()
                result.append(number*number)
            result.append(num*num)
    while negativeList:
        number = negativeList.pop()
        result.append(number*number)
        
    return result

print(sortedSquaresInternet([-4,-1,0,3,10]))