import heapq



def solve( A, B, C):
    c= []
    A.sort(reverse=True)
    B.sort(reverse=True)
    # A.reverse()
    # B.reverse()
    if len(A)==1:
        return [A[0]+B[0]]
    print(A,B)
    eleB = B.pop(0)
    for i in range(C):
        c.append(eleB+A[i])
    heapq.heapify(c)
    while B:
        eleB = B.pop(0)
        for eleA in A:
            if eleB + eleA < c[0]:
                break
            else:
                heapq.heappop(c)
                heapq.heappush(c,eleB+eleA)
    return sorted(c,reverse=True)
              


A = [1, 4, 2, 3]
B = [2, 5, 1, 6]
C = 4
print(solve(A,B,C))
