a, b = map(int, input().split())
fashionable_days = min(a, b)
remaining_red = a - fashionable_days
remaining_blue = b - fashionable_days
same_color_days = max(remaining_red, remaining_blue) // 2
print(fashionable_days, same_color_days)
