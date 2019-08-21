# Run solution
def solution(start, length):
    chkSum = 0
    for i in range(length,0,-1):
        if (start%4 != 0):
            for a in range(start, start + (4 - start % 4)): chkSum ^= a
        end = start + i
        if(end%4 != 0):
            for j in range((end - (int(end / 4) * 4)), 0, -1): chkSum ^= (end - j)
        start += length
    return chkSum
# Uncomment following to see the example
# print(solution(17,4))