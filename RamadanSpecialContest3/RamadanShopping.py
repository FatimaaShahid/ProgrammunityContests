n = int(input())
t = list(map(int, input().split()))

t.sort()
count = 0
waiting_time = 0

for time in t:
    if time >= waiting_time:
        count += 1
        waiting_time += time

print(count)
