#1056

num = int(input())
hansu = 0

for n in range(1, num+1):
  if n <= 99:
    hansu += 1
  
  else:
    num_list = list(map(int, str(n)))
    if num_list[1]-num_list[0] == num_list[2] - num_list[1]:
      hansu += 1
print(hansu)


# 11654
print(ord(input()))


# 11720
num_len = int(input())
num = input()
num_list = list(map(int, num))
print(sum(num_list))
