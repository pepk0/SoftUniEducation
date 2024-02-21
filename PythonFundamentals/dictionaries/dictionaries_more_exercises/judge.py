def add_submission_information(user: str, contest: str, points: int, 
                               results: dict, ranking: dict) -> None:
    if contest not in results:
        results[contest] = {}
    if user not in ranking:
        ranking[user] = 0
    if user not in results[contest]:
        results[contest][user] = 0
    if results[contest][user] <= points:
        difference = abs(points - results[contest][user])
        ranking[user] += difference
        results[contest][user] = points


judge_results = {}
individual_results = {}
sorting_key = lambda x: (-x[1], x[0])

while True:
    contest_submission = input().split(" -> ")
    if len(contest_submission) <= 1:
        break
    username, contest, points = contest_submission
    add_submission_information(username, contest, int(points),
                               judge_results, individual_results)

for contest, results in judge_results.items():
    print(f"{contest}: {len(results.values())} participants")
    for position, (name, points) in enumerate(sorted(results.items(), 
                                             key=sorting_key), 1):
        print(f"{position}. {name} <::> {points}")
print("Individual standings:")
for position, (name, points) in enumerate(sorted(individual_results.items(), 
                                         key=sorting_key), 1):
    print(f"{position}. {name} -> {points}")
