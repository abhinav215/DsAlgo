def trap(height):
  n = len(height)
  leftmax = rightmax = 0
  l = 0
  r = n-1
  water = 0
  while l<=r:
    if height[l]<=height[r]:
      if height[l]>=leftmax:
        leftmax = height[l]
      else:
        water += leftmax - height[l]
      l+=1
    else:
      if height[r]>=rightmax:
        rightmax = height[r]
      else:
        water += rightmax- height[r]
      r-=1
  print(water)
  return water



#suffix and prefix method
def trap2(height):
  n = len(height)
  maxi = 0
  pre=[]
  for ele in height:
    maxi = max(ele,maxi)
    pre.append(maxi)
  print(pre)
  maxi = 0
  suffix = []
  for i in range(n-1,-1,-1):
    maxi = max(maxi,height[i])
    suffix.append(maxi)
  suffix.reverse()
  water = 0
  for i in range(n):
    water += max(min(suffix[i],pre[i])-height[i],0)
  return water

            

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap2(height))