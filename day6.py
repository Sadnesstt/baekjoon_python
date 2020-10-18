#1. 2742
x = int(input())
for i in reversed(range(1, x+1)):
  print(i)

#2. 11021
T = int(input())
res = []
for i in range(T):
  A, B = input().split()
  A = int(A)
  B = int(B)
  res.append(A + B)

for i in range(1, T+1):
  print("Case #%d: %d" %(i, res[i-1]))

#3. 11022
T = int(input())

for i in range(T):
  A, B = map(int, input().split())
  ans = A + B
  print('Case #%d: %d + %d = %d'%(i+1, A, B, ans))