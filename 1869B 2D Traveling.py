# def dist(r, s):
#     dx = abs(r[0] - s[0])
#     dy = abs(r[1] - s[1])
#     return dx + dy

# t = int(input())
# for _ in range(t):
#     n, k, a, b = map(int, input().split())
#     v = [tuple(map(int, input().split())) for _ in range(n)]
#     a -= 1
#     b -= 1
#     res = dist(v[a], v[b])
#     minstart = 2 * 10**15 + 7
#     mindest = 2 * 10**15 + 7
#     for p in range(k):
#         minstart = min(minstart, dist(v[a], v[p]))
#         mindest = min(mindest, dist(v[b], v[p]))
#     minfly = minstart + mindest
#     res = min(res, minfly)
#     print(res)



def main():
    t = int(input())
    for _ in range(t):
        n, k, a, b = map(int, input().split())
        set_of_coordinates = [tuple(map(int, input().split())) for _ in range(n)]

        distance = float('inf')
        distance_one = float('inf')

        starting = set_of_coordinates[a - 1]
        ending = set_of_coordinates[b - 1]

        for i in range(k):
            current = set_of_coordinates[i]
            start_dist = abs(starting[0] - current[0]) + abs(starting[1] - current[1])
            end_dist = abs(ending[0] - current[0]) + abs(ending[1] - current[1])
            distance_one = min(distance_one, start_dist)
            distance = min(distance, end_dist)

        direct_distance = abs(starting[0] - ending[0]) + abs(starting[1] - ending[1])

        if k == 0:
            print(direct_distance)
        else:
            result = min(direct_distance, distance_one + distance)
            print(result)

if __name__ == "__main__":
    main()
