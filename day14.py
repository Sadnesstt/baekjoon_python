# 11720
T = int(input())
nums = input()
res = 0
for i in range(T):
    num = int(nums[i])
    res += num
print(res)

# 10809
# type1
import string
alphabet = string.ascii_lowercase
words = input()
res = []
for char in alphabet:
    res.append(words.find(char))
print(*res, sep=" ")

# # type2
words = input()
print(*map(words.find,map(chr, range(97, 123))), sep=" ")

# 2675
T = int(input())
res = []
for i in range(T):
    R, S = input().split()
    R = int(R)
    P = ''
    for char in S:
        P += R * char
    print(P)

