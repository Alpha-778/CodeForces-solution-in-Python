def is_beautiful(year):
    return len(set(str(year))) == 4

def next_beautiful_year(y):
    y += 1
    while not is_beautiful(y):
        y += 1
    return y

y = int(input())
print(next_beautiful_year(y))
