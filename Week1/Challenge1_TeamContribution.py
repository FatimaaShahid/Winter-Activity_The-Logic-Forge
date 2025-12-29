def finding_impact(contributions):
    n = len(contributions)
    impact = [0]*n
    
    prev = 1

    for i in range(n):
        impact[i] = prev
        prev *= contributions[i]
    
    after = 1

    for i in range(n-1, -1, -1):
        impact[i] *= after
        after *= contributions[i]
    return impact
print(finding_impact([1, 2, 3, 4]))  
print(finding_impact([-1, 1, 0, -3, 3]))  