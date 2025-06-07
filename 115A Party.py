def main():
    ans = 0
    n = int(input())
    a = [0] * (n + 10)
    for i in range(1, n + 1):
        a[i] = int(input())
    for i in range(1, n + 1):
        c = 0
        x = a[i]
        while x != -1:
            x = a[x]
            c += 1
        ans = max(ans, c)
    print(ans + 1)

if __name__ == "__main__":
    main()