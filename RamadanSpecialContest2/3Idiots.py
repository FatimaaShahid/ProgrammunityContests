t=int(input())
count = 0
for _ in range(t):
    l = int(input()).split()
    if l.count(1)>1:
        count += 1
print(count)