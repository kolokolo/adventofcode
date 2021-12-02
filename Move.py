def move(direction, movement, current_position):
    new_position = current_position
    x = current_position[0]
    y = current_position[1]
    if direction == 'down':
        new_position = (x, y + movement)
    elif direction == 'up':
        new_position = (x, y - movement)
    elif direction == 'forward':
        new_position = (x + movement, y)
    return new_position


def move_with_aim(direction, movement, current_position_with_aim):
    new_position = current_position_with_aim
    x = current_position_with_aim[0]
    y = current_position_with_aim[1]
    aim = current_position_with_aim[2]
    if direction == 'down':
        new_position = (x, y, aim + movement)
    elif direction == 'up':
        new_position = (x, y, aim - movement)
    elif direction == 'forward':
        new_position = (x + movement, y + aim * movement, aim)
    return new_position


position = (0, 0, 0)
with open('movements.txt', 'r') as f:
    for line in f.readlines():
        tokens = line.split()
        position = move_with_aim(tokens[0], int(tokens[1]), position)
print(str(position[0] * position[1]))
