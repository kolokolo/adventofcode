def count_increases(items):
    prev = None
    count = 0
    for item in items:
        if prev is None:
            prev = item
        else:
            if item > prev:
                count = count + 1
            prev = item
    return count


def count_increases_window(items, window_size):
    if window_size == 1:
        return count_increases(items)
    window_sum = []
    for i in range(0, len(items)):
        window = 0
        if i + window_size <= len(items):
            for y in range(0, window_size):
                window = window + items[i + y]
            window_sum.append(window)
    return count_increases(window_sum)


readings = []
with open('readings.txt', 'r') as f:
    for line in f.readlines():
        readings.append(int(line))
print(count_increases_window(readings, 1))
print(count_increases_window(readings, 3))
