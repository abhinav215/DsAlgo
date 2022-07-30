# Calculate square of a number without using *, / and pow()

from asyncio import events


# if n==0:
#   sqaure(n)=0
# if n==event
#   square(n) = square(n/2)*4
# if n==odd
#   square(n) = 4*square(n//2) + 4*square(m//2)+1


def sq(n):
  if n==0:
    return 0 
  if n&1==0:
    return 4*sq(n//2)
  else:
    return 4*sq(n//2) +4*(n//2) + 1



n=13

print(sq(n))