def process_test_cases():
    z = int(input())
    for _ in range(z):
        values = input().split()
        number_count = int(values[0])
        desired_total = int(values[1])
        elements = list(map(int, input().split()))
        calculated_sum = 0
        counter_zero = 0
        counter_one = 0
        counter_two = 0
        for index in range(number_count):
            value = elements[index]
            calculated_sum = calculated_sum + value
            if value == 0:
                counter_zero = counter_zero + 1
            elif value == 1:
                counter_one = counter_one + 1
            elif value == 2:
                counter_two = counter_two + 1
        remaining = desired_total - calculated_sum
        if remaining < 0 or remaining == 1:
            first_entry = True
            for i in range(counter_zero):
                if not first_entry:
                    print(" ", end="")
                print("0", end="")
                first_entry = False
            for j in range(counter_two):
                if not first_entry:
                    print(" ", end="")
                print("2", end="")
                first_entry = False
            for k in range(counter_one):
                if not first_entry:
                    print(" ", end="")
                print("1", end="")
                first_entry = False
            print()
        else:
            print("-1")
process_test_cases()