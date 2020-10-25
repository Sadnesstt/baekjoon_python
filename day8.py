# 10952.
A = -1
B = -1
while A != 0 and B != 0:
 A, B = input().split()
 A = int(A)
 B = int(B)
 res = A + B
 if res != 0:
   print(res)
 else:
   break

# 10951
while True:
 try:
   A, B = map(int, input().split())
   print(A + B )
 except:
   break

# 1110
N = init = int(input())
cyl = 0

while True:
  ten = N // 10
  one = N % 10
  total = ten + one
  cyl += 1

  N = one * 10 + total % 10

  if N == init:
    break

print(cyl)