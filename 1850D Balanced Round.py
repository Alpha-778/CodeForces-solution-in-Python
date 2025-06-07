def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    arr.sort()
    
    curr = 1
    total = 0
    
    for i in range(n - 1):
        if abs(arr[i] - arr[i + 1]) <= k:
            curr += 1
        else:
            total = max(total, curr)
            curr = 1
    
    total = max(total, curr)
    print(n - total)

def main():
    T = int(input())
    for _ in range(T):
        solve()

if __name__ == "__main__":
    main()
