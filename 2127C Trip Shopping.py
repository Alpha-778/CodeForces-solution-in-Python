def shopping_game(number_of_items, number_of_rounds, array_a, array_b):
    interval_list = []
    cumulative_distance = 0
    index = 0
    while index < number_of_items:
        value_from_a = array_a[index]
        value_from_b = array_b[index]
        lower_bound = value_from_a if value_from_a < value_from_b else value_from_b
        upper_bound = value_from_a if value_from_a > value_from_b else value_from_b
        interval_list.append((lower_bound, upper_bound))
        cumulative_distance += (upper_bound - lower_bound)
        index += 1
    sorted_intervals = sorted(interval_list, key=lambda element: element[0])
    distance_extensions = []
    current_index = 0
    while current_index < number_of_items - 1:
        first_lower, first_upper = sorted_intervals[current_index]
        second_lower, second_upper = sorted_intervals[current_index + 1]
        extension = second_lower - first_upper
        doubled_gap = extension * 2 if extension > 0 else 0
        distance_extensions.append(doubled_gap)
        current_index += 1
    merge_limit = number_of_rounds if number_of_rounds < (number_of_items - 1) else (number_of_items - 1)
    reordered_gaps = sorted(distance_extensions)
    accumulated_extension = 0
    count = 0
    while count < merge_limit:
        accumulated_extension += reordered_gaps[count]
        count += 1
    final_result = cumulative_distance + accumulated_extension
    return final_result
total_cases = int(input())
test_counter = 0
while test_counter < total_cases:
    values = input().split()
    size_n = int(values[0])
    limit_k = int(values[1])
    first_array = list(map(int, input().split()))
    second_array = list(map(int, input().split()))
    computed_answer = shopping_game(size_n, limit_k, first_array, second_array)
    print(computed_answer)
    test_counter += 1