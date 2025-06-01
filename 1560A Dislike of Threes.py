def generate_liked_numbers(limit):
    liked = []
    num = 1
    while len(liked) < limit:
        if num % 3 != 0 and num % 10 != 3:
            liked.append(num)
        num += 1
    return liked

t = int(input())
ks = [int(input()) for _ in range(t)]
liked_numbers = generate_liked_numbers(1000)
for k in ks:
    print(liked_numbers[k-1])