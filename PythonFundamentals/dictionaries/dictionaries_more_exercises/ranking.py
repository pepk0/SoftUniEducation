def validate_contest(contest: str, password: str, username: str, points: int,
                     results: dict, credentials: dict):
    if contest in credentials and password in credentials.values():
        if username not in results:
            results[username] = {}
        if contest not in results[username]:
            results[username][contest] = 0
        if results[username][contest] <= points:
            results[username][contest] = points


def find_best_candidate(contest: dict) -> str:
    best_result = 0
    best_candidate = ""
    for candidate, results in contest.items():
        current_result = sum(results.values())
        if current_result >= best_result:
            best_candidate, best_result = candidate, current_result
    return f"Best candidate is {best_candidate} with total {best_result} points."


contest_credentials = {}
contest_results = {}
while True:
    contest_information = input().split(":")
    if contest_information[0] == "end of contests":
        break
    contest_name, contest_password = contest_information
    contest_credentials[contest_name] = contest_password

while 1:
    contest_submissions = input().split("=>")
    if contest_submissions[0] == "end of submissions":
        break
    contest_name, contest_password, username, points = contest_submissions
    validate_contest(contest_name, contest_password,
                     username, int(points), contest_results, contest_credentials)

print(find_best_candidate(contest_results))
print("Ranking:")
for user, results in sorted(contest_results.items(), key=lambda x: x[0]):
    print(f"{user}")
    for contest_name, points in sorted(results.items(), key=lambda x: -x[1]):
        print(f"#  {contest_name} -> {points}")
