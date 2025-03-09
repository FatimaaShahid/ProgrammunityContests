def min_distance(a, b, x, y):
    direct = abs(a - b)
    via_teleport_1 = abs(a - x) + abs(y - b)
    via_teleport_2 = abs(a - y) + abs(x - b)
    return min(direct, via_teleport_1, via_teleport_2)


a, b, x, y = map(int, input().split())

print(min_distance(a, b, x, y))
