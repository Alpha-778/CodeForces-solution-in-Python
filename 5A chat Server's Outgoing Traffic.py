import sys

data = sys.stdin.read().splitlines()

def calculate_traffic(commands):
    users = set()
    total_traffic = 0

    for line in commands:
        if line.startswith('+'):
            users.add(line[1:])
        elif line.startswith('-'):
            users.remove(line[1:])
        else:
            sender, message = line.split(':', 1)
            total_traffic += len(message) * len(users)

    return total_traffic

print(calculate_traffic(data))
