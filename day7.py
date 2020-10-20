# 2438
T = int(input())

res = ''
for i in range(T):
  res = res + "*"
  print(res)

# 2439
T = int(input())
for i in reversed(range(T)):
  res = ' '*i + "*"*(T-i)
  print(res)

# 10871
N, X = input().split()
A = input().split()
N = int(N)
X = int(X)
A = list(map(int,A))

for i in A:
  if i < X:
    print(i, end = " ")