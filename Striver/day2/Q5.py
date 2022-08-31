def answer(A):
    A.sort()
    ans1 = -1
    ans2 = -1
    n = len(A)
    for i in range(n-1):
        if A[i]==A[i+1]:
            ans1=A[i]
        elif A[i+1]-A[i]!=1:
            ans2=A[i]+1
        if ans1!=-1 and ans2!=-1:
          break
    return [ans1,ans2]


ltb = [3 ,1 ,2,5 ,3] 
print(answer(ltb))