import sys
input_reader = sys.stdin.readline
maximum_elements = 5005
binary_indexed_tree = [0] * maximum_elements
number_of_elements = 0
def update_tree(position, value_to_add):
    current_position = position
    while current_position <= number_of_elements:
        binary_indexed_tree[current_position] += value_to_add
        current_position += (current_position & -current_position)
def prefix_sum_query(position):
    cumulative_sum = 0
    index = position
    while index > 0:
        cumulative_sum += binary_indexed_tree[index]
        index -= (index & -index)
    return cumulative_sum
def solve_each_test_case():
    global number_of_elements
    number_of_elements = int(input_reader())
    element_array = [0] + list(map(int, input_reader().split()))
    left_contributions = [0] * (number_of_elements + 1)
    right_contributions = [0] * (number_of_elements + 1)
    total_inversions = 0
    for index in range(1, number_of_elements + 1):
        binary_indexed_tree[index] = 0
    for forward_index in range(1, number_of_elements + 1):
        current_element = element_array[forward_index]
        left_contributions[forward_index] = prefix_sum_query(number_of_elements) - prefix_sum_query(current_element)
        total_inversions += left_contributions[forward_index]
        update_tree(current_element, 1)
    for index in range(1, number_of_elements + 1):
        binary_indexed_tree[index] = 0
    for backward_index in range(number_of_elements, 0, -1):
        current_element = element_array[backward_index]
        right_contributions[backward_index] = prefix_sum_query(number_of_elements) - prefix_sum_query(current_element)
        update_tree(current_element, 1)
    minimum_possible_value = total_inversions
    for index in range(1, number_of_elements + 1):
        contribution_difference = right_contributions[index] - left_contributions[index]
        if contribution_difference < 0:
            minimum_possible_value += contribution_difference
    print(minimum_possible_value)
def run_program():
    total_test_cases = int(input_reader())
    while total_test_cases > 0:
        solve_each_test_case()
        total_test_cases -= 1
run_program()