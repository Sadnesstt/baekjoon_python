#4344.
T = int(input())
for i in range(T):
   case = list(map(int, input().split()))
   C = case[0]
   case = case[1:]
   avg = sum(case)/C
   case2 = [1 if x > avg else 0 for x in case]
   stat = (sum(case2)/C) * 100
   print(format(round(stat, 3), '.3f')+'%')

#15596.
def solve(a):
  a = [x for x in a if type(x)==int]
  return(sum(a))

#4673.
res = []
for i in range(1, 10001):
  if i < 10:
    num = i + i
    res.append(num)
  elif i < 100:
    num = i + i//10 + i % 10
    res.append(num)
  elif i < 1000:
    num = i  + i//100+ (i%100)//10 + (i%100)%10
    res.append(num)
  elif i < 10000:
    num = i + i//1000 + (i%1000)//100 + ((i%1000)%100)//10 + ((i%1000)%100)%10
    if num < 10000:
      res.append(num)

nums = list(range(1, 10000))
ans = list(set(nums) - set(res))
for self_num in sorted(ans):
  print(self_num)
