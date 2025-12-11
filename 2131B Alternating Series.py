def process_case(count):
    total_numbers = count
    output_values = []
    if total_numbers % 2 != 0:
        index = 0
        while index < total_numbers:
            if index % 2 == 0:
                output_values.append(-1)
            else:
                output_values.append(3)
            index += 1
    else:
        if total_numbers == 2:
            output_values.append(-1)
            output_values.append(2)
        else:
            index = 0
            while index < total_numbers - 2:
                if index % 2 == 0:
                    output_values.append(-1)
                else:
                    output_values.append(3)
                index += 1
            output_values.append(-1)
            output_values.append(2)
    print(" ".join(str(num) for num in output_values))
def main():
    import sys
    data_stream = sys.stdin.read().strip().split()
    position = 0
    test_cases = int(data_stream[position])
    position += 1
    for _ in range(test_cases):
        n_value = int(data_stream[position])
        position += 1
        process_case(n_value)
if __name__ == "__main__":
    main()