def fill_the_box(*args) -> str:
    from collections import deque

    cube_size = 1
    line = deque(args)
    element = ""

    for _ in range(3):
        cube_size *= line.popleft()

    while element != "Finish":
        element = line.popleft()

        if element == "Finish":
            continue
        elif cube_size - element <= 0:
            left_over = element - cube_size
            line.appendleft(left_over)
            break
        else:
            cube_size -= element
    else:
        return (f"There is free space in the box. You could put "
                f"{cube_size} more cubes.")

    return (f"No more free space! You have "
            f"{sum((el for el in line if str != type(el)))} more cubes.")
