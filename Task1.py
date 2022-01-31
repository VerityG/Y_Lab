points = [(0, 2), (2, 5), (5, 2), (6, 6), (8, 3)]

total_distance = []
path = 0
n = 0
p = 0
print(points[0], end='')
while p != 5:
    result = []
    distance = []
    for j in range(len(points) - 1, 0, -1):
        stray = ((points[n][0] - points[j][0]) ** 2 + (points[n][1] - points[j][1]) ** 2) ** 0.5
        if stray != 0:
            distance.append(stray)
    result.append(min(distance))
    for j in range(len(points)):
        stray = ((points[n][0] - points[j][0]) ** 2 + (points[n][1] - points[j][1]) ** 2) ** 0.5
        if stray in result and stray != 0 and p != 4:
            path += result[0]
            print(f' -> {points[j]}[{path}]', end='')
            total_distance.append(result)
            n = j
            p += 1
        elif p == 4:
            stray = ((points[n][0] - points[0][0]) ** 2 + (points[n][1] - points[0][1]) ** 2) ** 0.5
            path += stray
            print(f' -> {points[0]}[{path}]', end='')
            print(f' = {path}')
            total_distance.append([stray])
            n = j
            p += 1

