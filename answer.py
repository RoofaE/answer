def is_safe(levels):
    differences = []
    for i in range(len(levels) - 1):
        diff = levels[i + 1] - levels[i]
        differences.append(diff)

    all_increasing = True
    for d in differences:
        if d < 1 or d > 3:
            all_increasing = False

    all_decreasing = True
    for d in differences:
        if d < -3 or d > -1:
            all_decreasing = False

    return all_increasing or all_decreasing


reports = []

with open("input.txt") as f:
    for line in f:
        numbers = list(map(int, line.split()))
        reports.append(numbers)

safe_count = 0

for report in reports:
    if is_safe(report):
        safe_count += 1

print(safe_count)