# Roman to integer
s = input()

d = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

ans = 0

for i in range(len(s)):
    if i + 1 < len(s) and d[s[i]] < d[s[i + 1]]:
        ans -= d[s[i]]
    else:
        ans += d[s[i]]

print(ans)
# Plus one
digits = list(map(int, input().split()))

num = 0

for digit in digits:
    num = num * 10 + digit

num = num + 1

result = []

for digit in str(num):
    result.append(int(digit))

print(result)
#Add binary
a = input()
b = input()

num1 = int(a, 2)
num2 = int(b, 2)

result = num1 + num2

print(bin(result)[2:])
# sqrt(x)
n = int(input())

i = 0

while (i + 1) * (i + 1) <= n:
    i += 1

print(i)
# happy number
n = int(input())

while n != 1 and n != 4:
    total = 0

    while n > 0:
        digit = n % 10
        total += digit * digit
        n = n // 10

    n = total
 
if n == 1:
    print(True)
else:
    print(False)
