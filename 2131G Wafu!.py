MOD = 1000000007
def power_modulo(base_value, exponent_value):
    result_value = 1
    base_value %= MOD
    current_exponent = exponent_value
    current_base = base_value
    while current_exponent > 0:
        if current_exponent & 1:
            result_value = (result_value * current_base) % MOD
        current_base = (current_base * current_base) % MOD
        current_exponent >>= 1
    return result_value
def main():
    import sys
    input_data = sys.stdin.read().split()
    iterator_position = 0
    if iterator_position >= len(input_data):
        return
    total_cases = int(input_data[iterator_position])
    iterator_position += 1
    for _ in range(total_cases):
        n_value = int(input_data[iterator_position])
        iterator_position += 1
        k_value = int(input_data[iterator_position])
        iterator_position += 1
        sequence_values = []
        for _ in range(n_value):
            sequence_values.append(int(input_data[iterator_position]))
            iterator_position += 1
        sequence_values.sort()
        remaining_k = k_value
        answer_value = 1
        index_position = 0
        while index_position < n_value and remaining_k > 0:
            current_x = sequence_values[index_position]
            if current_x - 1 >= 63:
                capacity_value = remaining_k
            else:
                shifted_val = 1 << (current_x - 1)
                if shifted_val > remaining_k:
                    capacity_value = remaining_k
                else:
                    capacity_value = shifted_val
            total_take = capacity_value
            if total_take == 0:
                index_position += 1
                continue
            count_x = 1 if total_take >= 1 else 0
            total_consumed = count_x
            if total_take >= 2:
                temp_value = total_take - 1
                max_power_bit = 63 - (temp_value.bit_length() - 1)
                max_y_val = min(current_x - 1, (temp_value.bit_length()))
                y_val = 2
                while y_val <= max_y_val:
                    part1 = temp_value >> (y_val - 1)
                    part2 = temp_value >> y_val
                    count_y = part1 - part2 if part1 >= part2 else 0
                    if count_y > 0:
                        answer_value = (answer_value * power_modulo(y_val, count_y)) % MOD
                        total_consumed += count_y
                    y_val += 1
            remaining_part = total_take - total_consumed
            if count_x > 0:
                answer_value = (answer_value * (current_x % MOD)) % MOD
            remaining_k -= total_take
            index_position += 1
        print(answer_value % MOD)
if __name__ == "__main__":
    main()