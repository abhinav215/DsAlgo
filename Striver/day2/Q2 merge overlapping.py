

def answer(lt):
  lt = sorted(lt, key= lambda x:x[0])
  final = []
  print(lt)
  n = len(lt)
  ans = lt[0]
  for i in range(1,n):
    # print(i)
    if ans[1]>=lt[i][0]:
      ans = [min(ans[0],lt[i][0]),max(ans[1],lt[i][1])]
    else:
      # print(ans)
      final.append(ans)
      ans = lt[i]
  print(ans)
  final.append(ans)
  return final



intervals=[[1,3],[2,6],[8,10],[15,18]]

intervals=[[2,3],[4,5],[6,7],[8,9],[1,10]]
# intervals=[[1,4],[4,5]]
print(answer(intervals))