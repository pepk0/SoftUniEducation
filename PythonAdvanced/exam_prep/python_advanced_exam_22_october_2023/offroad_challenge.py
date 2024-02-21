from collections import deque

fuels = deque([int(el) for el in input().split()])
consumption_index = deque([int(el) for el in input().split()])
altitudes = deque([int(el) for el in input().split()])

cur_altitude = 1
altitude_reached = []
total_altitudes = len(altitudes)

while fuels and consumption_index:
    fuel = fuels.pop()
    consumption = consumption_index.popleft()
    altitude = altitudes.popleft()

    result = fuel - consumption

    if result >= altitude:
        altitude_reached.append(f"Altitude {cur_altitude}")
        print(f"John has reached: Altitude {len(altitude_reached)}")
        cur_altitude += 1
    else:
        altitudes.appendleft(altitude)
        print(f"John did not reach: Altitude {cur_altitude}")
        break

if len(altitude_reached) == total_altitudes:
    print("John has reached all the altitudes and managed to reach the top!")
else:
    print("John failed to reach the top.")
    if altitude_reached:
        print("Reached altitudes: ", end="")
        print(*altitude_reached, sep=", ")
    else:
        print("John didn't reach any altitude.")
