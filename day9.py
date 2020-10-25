#10818
T = int(input())
numbers = list(map(int, input().split()))
_min = min(numbers)  
_max = max(numbers)  
print(_min, _max, sep=" ")
​

# 2562
nums = []
for i in range(9):
  nums.append(int(input()))

print(max(nums), nums.index(max(nums))+1, sep= "\n")

# 2577
A = int(input())
B = int(input())
C = int(input())
mul = str(A * B * C)  

for i in range(10):
  print(mul.count(str(i)))
