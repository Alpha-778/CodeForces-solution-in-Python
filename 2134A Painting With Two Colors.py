def check_condition(n, a, b, x, L, R):
    l1 = x
    r1 = x + a - 1
    l2 = n - x - a + 2
    r2 = n - x + 1
    if l1 > l2:
        temp1, temp2 = l1, r1
        l1, r1 = l2, r2
        l2, r2 = temp1, temp2
    if r1 < l2:
        if l1 >= L and r1 <= R and l2 >= L and r2 <= R:
            return True
        else:
            return False
    else:
        valid = True
        if l1 <= l2 - 1:
            if not (l1 >= L and l2 - 1 <= R):
                valid = False
        if r1 + 1 <= r2:
            if not (r1 + 1 >= L and r2 <= R):
                valid = False
        return valid
def main():
    import sys
    input_data = sys.stdin.read().split()
    index = 0
    t = int(input_data[index])
    index += 1
    results = []
    for _ in range(t):
        n = int(input_data[index]); index += 1
        a = int(input_data[index]); index += 1
        b = int(input_data[index]); index += 1
        if (n - b) % 2 != 0:
            results.append("NO")
            continue
        y = (n - b + 2) // 2
        L = y
        R = y + b - 1
        if (n - a) % 2 == 0:
            results.append("YES")
            continue
        s = set()
        s.add(1)
        s.add(max(1, n - a + 1))
        v = []
        v.append(L)
        v.append(L - (a - 1))
        v.append(R)
        v.append(R - (a - 1))
        v.append(n - L + 1)
        v.append(n - R + 1)
        v.append(n - a - L + 2)
        v.append(n - a - R + 2)
        v.append((n - a + 2) // 2)
        v.append((n - a + 3) // 2)
        for z in v:
            for d in range(-2, 3):
                s.add(z + d)
        found = False
        xmin = 1
        xmax = n - a + 1
        for x in s:
            if x < xmin or x > xmax:
                continue
            if check_condition(n, a, b, x, L, R):
                found = True
                break
        if found:
            results.append("YES")
        else:
            results.append("NO")
    sys.stdout.write("\n".join(results))
if __name__ == "__main__":
    main()