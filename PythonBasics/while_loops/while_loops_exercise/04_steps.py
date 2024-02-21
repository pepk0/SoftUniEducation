steps_goal = 10000
steps_taken = 0 

while steps_goal > steps_taken:

    steps_walked = input()
    if steps_walked == "Going home":
        step_walked_home = int(input())
        steps_taken += step_walked_home
        break
    
    steps_taken += int(steps_walked)

difference = abs(steps_taken - steps_goal)

if steps_taken >= steps_goal:
    print("Goal reached! Good job!",
          f"{difference} steps over the goal!", sep="\n")
else:
    print(f"{difference} more steps to reach goal.")