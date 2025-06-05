n, t = map(int, input().split())
a = list(map(int, input().split()))
max_books = 0
current_sum = 0
start = 0
for end in range(n):
    current_sum += a[end]
    while current_sum > t:
        current_sum -= a[start]
        start += 1
    max_books = max(max_books, end - start + 1)
print(max_books)