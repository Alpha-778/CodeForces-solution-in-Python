def is_lucky(num_str):
    return all(c in '47' for c in num_str)

def is_nearly_lucky(n):
    n_str = str(n)
    lucky_count = sum(1 for c in n_str if c in '47')
    return "YES" if is_lucky(str(lucky_count)) else "NO"

n = input().strip()
print(is_nearly_lucky(n))