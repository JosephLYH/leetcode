num_cases = int(input())

for _ in range(num_cases):
    count = 0

    num_people, num_steps, step_size, h = map(int, input().split())
    heights = list(map(int, input().split()))

    max_diff = step_size * (num_steps - 1)
    for height in heights:
        diff = abs(height - h)
        if diff > max_diff:
            pass
        elif height != h and diff % step_size == 0:
            count += 1

    print(count)
