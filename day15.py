# 1157
import string
word = input().upper()
counter = {}
alphabet = string.ascii_uppercase
counter = {chr : 0 for chr in alphabet}
for i in word:
    counter[i] += 1
highest = max(counter.values())
freq = [k for k, v in counter.items() if v == highest]

if len(freq) == 1:
    print(*freq)
else:
    print('?')

# 1152
words = input().strip().split()
print(len(words))

#2908
A, B = input().split()
A_reversed = int(A[::-1])
B_reversed = int(B[::-1])
if A_reversed > B_reversed:
    print(A_reversed)
else:
    print(B_reversed)
