import sys
user_input = sys.stdin.readline
constant_modulo = 998244353

def generate_combinatorial_table(limit_value, modulus_value):
    two_dimensional_array = [[0 for _ in range(limit_value + 1)] for _ in range(limit_value + 1)]
    for outer_index in range(limit_value + 1):
        two_dimensional_array[outer_index][0] = 1
        for inner_index in range(1, outer_index + 1):
            two_dimensional_array[outer_index][inner_index] = (two_dimensional_array[outer_index - 1][inner_index - 1] + two_dimensional_array[outer_index - 1][inner_index]) % modulus_value
    return two_dimensional_array

def calculate_total_permutation_variants(input_sequence):
    total_elements = len(input_sequence) - 1
    storage_matrix = [[0 for _ in range(total_elements + 2)] for _ in range(total_elements + 2)]
    precomputed_combinations = generate_combinatorial_table(total_elements, constant_modulo)
    for initial_index in range(1, total_elements + 2):
        storage_matrix[initial_index][initial_index - 1] = 1
    for current_interval_size in range(1, total_elements + 1):
        for current_start in range(1, total_elements - current_interval_size + 2):
            current_end = current_start + current_interval_size - 1
            intermediate_result = 0
            for proposed_middle in range(current_start, current_end + 1):
                computed_requirement = 0
                if proposed_middle > current_start:
                    computed_requirement += 1
                if proposed_middle < current_end:
                    computed_requirement += 1
                if input_sequence[proposed_middle] != -1 and input_sequence[proposed_middle] != computed_requirement:
                    continue
                total_left_count = proposed_middle - current_start
                total_right_count = current_end - proposed_middle
                valid_left_configurations = storage_matrix[current_start][proposed_middle - 1]
                valid_right_configurations = storage_matrix[proposed_middle + 1][current_end]
                number_of_selections = precomputed_combinations[total_left_count + total_right_count][total_left_count]
                current_contribution = number_of_selections * valid_left_configurations % constant_modulo
                current_contribution = current_contribution * valid_right_configurations % constant_modulo
                intermediate_result = (intermediate_result + current_contribution) % constant_modulo
            storage_matrix[current_start][current_end] = intermediate_result
    return storage_matrix[1][total_elements]

test_case_quantity = int(user_input())
for test_case_index in range(test_case_quantity):
    sequence_length = int(user_input())
    raw_sequence_data = list(map(int, user_input().split()))
    usable_sequence = [-1] + raw_sequence_data
    result_output = calculate_total_permutation_variants(usable_sequence)
    print(result_output)