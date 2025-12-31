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
print("Challenge 1: Team Contribution Multiplier")
print("Input : [1, 2, 3, 4] Output :" , finding_impact([1, 2, 3, 4]))  
print("Input : [-1, 1, 0, -3, 3] Output :" , finding_impact([-1, 1, 0, -3, 3]))  