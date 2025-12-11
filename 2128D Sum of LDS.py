import sys
def run_the_program():
    input_data = sys.stdin.read().split()
    input_index = 0
    def read_integer():
        nonlocal input_index
        val = int(input_data[input_index])
        input_index += 1
        return val
    number_of_test_cases = read_integer()
    output_lines = []
    for _ in range(number_of_test_cases):
        number_n = read_integer()
        permutation_array = [0] * (number_n + 2)
        decreasing_length_array = [1] * (number_n + 2)
        for index_variable in range(1, number_n + 1):
            permutation_array[index_variable] = read_integer()
        decreasing_length_array[number_n] = 1
        variable_i = number_n - 1
        while variable_i >= 1:
            if permutation_array[variable_i] > permutation_array[variable_i + 1]:
                decreasing_length_array[variable_i] = decreasing_length_array[variable_i + 1] + 1
            else:
                decreasing_length_array[variable_i] = 1
            variable_i = variable_i - 1
        final_answer_accumulator = 0
        another_variable_i = 1
        while another_variable_i <= number_n:
            current_k_value = decreasing_length_array[another_variable_i]
            summation_of_head_terms = current_k_value * (current_k_value + 1) // 2
            right_tail_possible_count = number_n - (another_variable_i + current_k_value - 1)
            if right_tail_possible_count < 0:
                right_tail_possible_count = 0
            final_answer_accumulator = final_answer_accumulator + summation_of_head_terms + current_k_value * right_tail_possible_count
            another_variable_i = another_variable_i + 1
        output_lines.append(str(final_answer_accumulator))
    sys.stdout.write("\n".join(output_lines) + "\n")
run_the_program()