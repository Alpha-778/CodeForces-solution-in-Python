import sys
def read_line():
    return sys.stdin.readline()
def solve_test_case(elements):
    present_values = set()
    for number in elements:
        if number != -1:
            present_values.add(number)
    count_present = len(present_values)
    if count_present == 0:
        return True
    if count_present > 1:
        return False
    single_value = None
    for item in present_values:
        single_value = item
        break
    if single_value is not None and single_value >= 1:
        return True
    return False
def process():
    number_of_tests_line = read_line()
    if number_of_tests_line:
        total_cases = int(number_of_tests_line.strip())
        current_case = 0
        while current_case < total_cases:
            length_line = read_line()
            if not length_line:
                break
            size = int(length_line.strip())
            array_line = read_line()
            if not array_line:
                break
            sequence = list(map(int, array_line.strip().split()))
            result = solve_test_case(sequence)
            if result:
                print("YES")
            else:
                print("NO")
            current_case += 1
if __name__ == "__main__":
    process()