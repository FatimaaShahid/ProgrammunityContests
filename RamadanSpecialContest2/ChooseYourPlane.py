n, m = map(int, input().split())
seats = list(map(int, input().split()))

max_earn = 0
min_earn = 0

max_seats = sorted(seats, reverse=True)
min_seats = sorted(seats)

for _ in range(n):
    max_earn += max_seats[0]
    max_seats[0] -= 1
    max_seats.sort(reverse=True)

for _ in range(n):
    min_earn += min_seats[0]
    min_seats[0] -= 1
    if min_seats[0] == 0:
        min_seats.pop(0)
        
print(max_earn, min_earn)


