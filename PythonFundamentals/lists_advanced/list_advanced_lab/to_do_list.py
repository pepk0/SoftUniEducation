def sort_list(tasks: dict) -> list:
    return [tasks[task] for task in sorted(tasks)]


to_do_list = {}
while True:
    input_task = input()
    if input_task == "End":
        break
    else:
        priority, task = input_task.split("-")
        priority = int(priority)
        to_do_list[priority] = task

result = sort_list(to_do_list)
print(result)
