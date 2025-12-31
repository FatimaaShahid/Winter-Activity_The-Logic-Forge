
def findingingMedian(scoreA, scoreB):
    n = len(scoreA)
    m = len(scoreB)
    i = 0
    j = 0
    m1 = 0
    m2 = 0

    for _ in range(0, (n + m) // 2 + 1):
        m2 = m1
        if i < n and j < m:
            if scoreA[i] > scoreB[j]:
                m1 = scoreB[j]
                j += 1
            else:
                m1 = scoreA[i]
                i += 1
        elif i < n:
            m1 = scoreA[i]
            i += 1
        else:
            m1 = scoreB[j]
            j += 1

    if (n + m) % 2 == 1:
        return float(m1)
    else:
        ans = float(m1) + float(m2)
        return ans / 2.0
print(findingingMedian([1, 3], [2]))  
print(findingingMedian([1, 2], [3, 4]))