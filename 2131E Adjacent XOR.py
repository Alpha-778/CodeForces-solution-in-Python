def solve_case():
    n = int(input().strip())
    arr_a = []
    arr_b = []
    temp_a = input().strip().split()
    for idx in range(n):
        arr_a.append(int(temp_a[idx]))
    temp_b = input().strip().split()
    for idx in range(n):
        arr_b.append(int(temp_b[idx]))
    if arr_a[n - 1] != arr_b[n - 1]:
        print("NO")
        return
    pos = n - 2
    while pos >= 0:
        condition_met = False
        if arr_b[pos] == arr_a[pos]:
            condition_met = True
        elif arr_b[pos] == (arr_a[pos] ^ arr_a[pos + 1]):
            condition_met = True
        elif arr_b[pos] == (arr_a[pos] ^ arr_b[pos + 1]):
            condition_met = True
        if not condition_met:
            print("NO")
            return
        pos -= 1
    print("YES")
def main():
    t_input = int(input().strip())
    current_case = 0
    while current_case < t_input:
        solve_case()
        current_case += 1
if __name__ == "__main__":
    main()