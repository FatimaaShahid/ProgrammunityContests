

spi = "314159265358979323846264338327"

t = int(input())
for _ in range(t):
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] == spi[i]:
            count += 1
        else:
            break
    print(count)