# 3052
divid = []
for i in range(10):
  nums = int(input())
  divid.append(nums % 42)

print(len(set(divid)))

#1546
N = int(input())
score = list(map(int, input().split()))
max_score = max(score)
score = [(x/max_score) * 100 for x in score]
print(sum(score)/N)

# 8958
T = int(input())

for i in range(T):
  score = 0
  cnt = 0
  ans = input()
  for j in range(len(ans)):
    if ans[j] == 'O':
      cnt += 1
      score += cnt
    else:
      cnt = 0
  print(score)