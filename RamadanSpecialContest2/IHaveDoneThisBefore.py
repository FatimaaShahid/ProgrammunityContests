n = int(input())
people = list(map(int, input().split()))

count_25 = 0
count_50 = 0

for cash in people:
    if cash == 25:
        count_25 += 1
    elif cash == 50:
        if count_25 > 0:
            count_25 -= 1
            count_50 += 1
        else:
            print("NO")
            exit()
    elif cash == 100:
        if count_50 > 0 and count_25 > 0:
            count_50 -= 1
            count_25 -= 1
        elif count_25 >= 3:
            count_25 -= 3
        else:
            print("NO")
            exit()

print("YES")

    
