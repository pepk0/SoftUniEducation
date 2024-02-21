number_poor_scores = int(input())
poor_scores_earned = 0
total_score = 0
total_problems_solved = 0
problem_name = ""

while problem_name != "Enough":

    problem_name = input()
    if problem_name == "Enough":
        continue
    problem_score = int(input())

    last_problem = problem_name
    total_score += problem_score
    total_problems_solved += 1

    if problem_score <= 4:
        poor_scores_earned += 1
    
    if poor_scores_earned >= number_poor_scores:
        print(f"You need a break, {poor_scores_earned} poor grades.")
        break

else:
    average_score = total_score / total_problems_solved
    print(f"Average score: {average_score:.2f}",
          f"Number of problems: {total_problems_solved}",
          f"Last problem: {last_problem}", sep="\n")