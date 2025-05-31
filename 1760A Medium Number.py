t=int(input())
rec=[list(map(int,input().split())) for i in range(t)]
for _ in range(t):
    a, b, c = rec[_]
    nums = [a, b, c]
    nums.sort()
    print(nums[1])