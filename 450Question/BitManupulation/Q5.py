


def isPowerofTwo(n):
  if n<=0:
    return False
  if n & n-1 != 0:
      return "NO"
  return "Yes"


print(isPowerofTwo(23))