import sys
def compute_days_until_possible_escape(length_of_corridor, initial_position, corridor_representation):
    very_large_number = 10 ** 9
    distance_from_left_wall = very_large_number
    distance_from_right_wall = very_large_number
    index_for_leftward_scan = initial_position - 1
    while index_for_leftward_scan > 0:
        character_to_the_left = corridor_representation[index_for_leftward_scan - 1]
        if character_to_the_left == '#':
            distance_from_left_wall = initial_position - index_for_leftward_scan
            break
        index_for_leftward_scan -= 1
    index_for_rightward_scan = initial_position
    while index_for_rightward_scan < length_of_corridor:
        character_to_the_right = corridor_representation[index_for_rightward_scan]
        if character_to_the_right == '#':
            distance_from_right_wall = index_for_rightward_scan + 1 - initial_position
            break
        index_for_rightward_scan += 1
    if distance_from_left_wall == very_large_number or distance_from_right_wall == very_large_number:
        return 1
    value_one = 2 * distance_from_left_wall + 1
    value_two = 2 * distance_from_right_wall + 1
    value_three = distance_from_left_wall + distance_from_right_wall + 1
    minimum_days_required = min(value_one, value_two, value_three)
    return minimum_days_required
def handle_multiple_test_cases():
    total_number_of_test_cases = int(sys.stdin.readline())
    for individual_case_index in range(total_number_of_test_cases):
        raw_input_line = sys.stdin.readline()
        space_separated_values = raw_input_line.strip().split()
        corridor_length = int(space_separated_values[0])
        mani_initial_position = int(space_separated_values[1])
        current_corridor_status = sys.stdin.readline().strip()
        result_for_current_case = compute_days_until_possible_escape(corridor_length, mani_initial_position, current_corridor_status)
        print(result_for_current_case)
if __name__ == '__main__':
    handle_multiple_test_cases()