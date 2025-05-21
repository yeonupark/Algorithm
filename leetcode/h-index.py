def solve(citations):
    citations.sort(reverse=True)
    ans = 0
    
    for (i, cit) in enumerate(citations):
        if i+1 >= cit: 
            if cit > ans:
                return cit
        else:
            ans = i+1
    
    return ans