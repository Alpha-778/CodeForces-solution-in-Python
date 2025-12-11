import sys
from collections import deque

def does_pattern_hold(recent_elements, value_to_compare):
    if len(recent_elements) < 4:
        return False
    first_element = recent_elements[0]
    second_element = recent_elements[1]
    third_element = recent_elements[2]
    fourth_element = recent_elements[3]
    if first_element < second_element and second_element < third_element and third_element < fourth_element and fourth_element < value_to_compare:
        return True
    if first_element > second_element and second_element > third_element and third_element > fourth_element and fourth_element > value_to_compare:
        return True
    return False

def evaluate_choice(left_index, right_index, recent_elements, data_list):
    if left_index > right_index:
        return False
    if left_index == right_index:
        return does_pattern_hold(recent_elements, data_list[left_index])
    left_value_ok = does_pattern_hold(recent_elements, data_list[left_index])
    right_value_ok = does_pattern_hold(recent_elements, data_list[right_index])
    return left_value_ok and right_value_ok

def process_single_case():
    input_line = sys.stdin.readline().strip()
    while input_line == "":
        input_line = sys.stdin.readline().strip()
    element_count = int(input_line)
    data_items = []
    while len(data_items) < element_count:
        parts = sys.stdin.readline().strip().split()
        for part in parts:
            if len(data_items) < element_count:
                data_items.append(int(part))
    recent_window = deque()
    output_chars = []
    left_pointer = 0
    right_pointer = element_count - 1
    while left_pointer <= right_pointer:
        left_value = data_items[left_pointer]
        right_value = data_items[right_pointer]
        can_take_left = does_pattern_hold(recent_window, left_value)
        can_take_right = does_pattern_hold(recent_window, right_value)
        chosen_char = None
        if can_take_left:
            chosen_char = 'R'
        elif can_take_right:
            chosen_char = 'L'
        else:
            chosen_char = 'L'
            if left_pointer < right_pointer:
                temp_window_for_left = deque(recent_window)
                temp_window_for_left.append(left_value)
                if len(temp_window_for_left) > 4:
                    temp_window_for_left.popleft()
                left_feasible = evaluate_choice(left_pointer + 1, right_pointer, temp_window_for_left, data_items)
                temp_window_for_right = deque(recent_window)
                temp_window_for_right.append(right_value)
                if len(temp_window_for_right) > 4:
                    temp_window_for_right.popleft()
                right_feasible = evaluate_choice(left_pointer, right_pointer - 1, temp_window_for_right, data_items)
                if left_feasible and not right_feasible:
                    chosen_char = 'R'
        output_chars.append(chosen_char)
        if chosen_char == 'L':
            picked_value = left_value
            left_pointer += 1
        else:
            picked_value = right_value
            right_pointer -= 1
        recent_window.append(picked_value)
        if len(recent_window) > 4:
            recent_window.popleft()
    sys.stdout.write("".join(output_chars) + "\n")
def main():
    raw = sys.stdin.readline().strip()
    while raw == "":
        raw = sys.stdin.readline().strip()
    test_cases = int(raw)
    for _ in range(test_cases):
        process_single_case()
if __name__ == "__main__":
    main()