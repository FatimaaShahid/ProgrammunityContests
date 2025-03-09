t = int(input())

for _ in range(t):
    a, b, c, x, y = map(int, input().split())

    dogs_needed = max(0, x - a)
    cats_needed = max(0, y - b)

    if dogs_needed + cats_needed <= c:
        print("YES")
    else:
        print("NO")
