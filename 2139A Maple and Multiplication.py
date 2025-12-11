number_of_test_cases = int(input())
for case_index in range(number_of_test_cases):
    first_value, second_value = map(int, input().split())
    if first_value == second_value:
        print(0)
    else:
        if first_value > second_value:
            larger_value = first_value
            smaller_value = second_value
        else:
            larger_value = second_value
            smaller_value = first_value
        remainder_result = larger_value % smaller_value
        if remainder_result == 0:
            print(1)
        else:
            print(2)