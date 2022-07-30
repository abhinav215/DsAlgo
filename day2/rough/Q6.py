# Input Format: N = 5, array[] = {5,4,3,2,1}

# Result: 10

# Explanation: we have a reverse sorted array and we will 
# get the maximum inversions as for i < j we will always 
# find a pair such that A[j] < A[i]. 
# Example: 5 has index 0 and 3 has index 2 now (5,3) pair 
# is inversion as 0 < 2 and 5 > 3 which will satisfy out 
# conditions and for reverse sorted array we will get 
# maximum inversions and that is (n)*(n-1) / 2.

# For above given array there is 4 + 3 + 2 + 1 = 10 inversions.


#bruteforce hai ye O(N^2)
# def answer(lt):
#   ans = sorted(lt)
#   # print(lt,ans)
#   n = len(lt)
#   if n<=1:
#     return 0
#   value = 0
#   for i in range(n-1,0,-1):
#     for j in range(len(lt)):
#       if ans[i] == lt[j]:
#         value += i-j
#         break
#     lt.remove(ans[i])
#     # print(lt,value)
#     # print(i)
#   return value
    

def mergeSort(lt):
  n = len(lt)
  temp = [0]*n  
  return countInversion(lt,temp,0,n-1)

def countInversion( lt,temp,left ,right):
  n = len(lt)
  if n==1:
    return 0
  mid = n//2
  arr1 = lt[:mid]
  arr2 = lt[mid:]
  ans = countInversion(arr1,temp,left, right) + countInversion(arr2,temp,left right)



# lt=[5,4,3,2,1]
# lt = [2 ,5, 1, 3 ,4]
# lt = [2 ,1]
# lt=[1, 2 ,7, 10, 6 ,3 ,4, 9, 8 ,5]
lt=[52244275, 123047899, 493394237, 922363607 ,378906890, 188674257, 222477309 ,902683641, 860884025 ,339100162]
print(mergeSort(lt))

#https://takeuforward.org/interviews/strivers-sde-sheet-top-coding-interview-problems/