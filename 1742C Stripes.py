def main():
    N = 8
    t = int(input())
    for _ in range(t):
        n=input()
        v = [input().strip() for _ in range(N)]
        ans = '.'
        for row in range(N):
            if all(cell == 'R' for cell in v[row]):
                ans = 'R'
                break
        if ans == '.':
            for col in range(N):
                if all(v[row][col] == 'B' for row in range(N)):
                    ans = 'B'
                    break
        print(ans)

if __name__ == "__main__":
    main()