import sys
data = sys.stdin.read().split()
index = 0
try:
    t = int(data[index])
    index += 1
except:
    sys.exit()
for _ in range(t):
    try:
        n = int(data[index])
        index += 1
    except:
        break
    a_values = []
    b_values = []
    count_a = 0
    while count_a < n and index < len(data):
        a_values.append(int(data[index]))
        index += 1
        count_a += 1
    count_b = 0
    while count_b < n and index < len(data):
        b_values.append(int(data[index]))
        index += 1
        count_b += 1
    total_positive_difference = 0
    position_index = 0
    while position_index < n:
        if a_values[position_index] > b_values[position_index]:
            difference_value = a_values[position_index] - b_values[position_index]
            total_positive_difference += difference_value
        position_index += 1
    result_value = total_positive_difference + 1
    sys.stdout.write(str(result_value) + "\n")