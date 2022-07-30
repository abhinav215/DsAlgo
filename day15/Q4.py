def myAtoi(self, s: str) -> int:
    s = s.strip(" ")
    if s=="":
        return 0
    sign=+1
    start = 0
    if s[0] == "+":
        sign=+1
        start += 1
    elif s[0] =="-":
        sign = -1
        start +=1
    n=len(s)
    if n==start:
        return 0
    MIN = -1<<31
    MAX= -MIN-1
    number = 0
    if ord(s[start])<48 or ord(s[start])>57:
        return 0
    for i in range(start,n):
        if ord(s[i])>=48 and ord(s[i])<=57:
            number = number*10+int(s[i])
        else:
            i-=1
            break
    ans = sign*number
    if ans<MIN:
        return MIN
    if ans>MAX:
        return MAX
    return ans
      
        