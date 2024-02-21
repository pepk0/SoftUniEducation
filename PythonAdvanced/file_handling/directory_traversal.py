import os


def scan_directories(path: str, items: list = []) -> list:

    for item in os.listdir(path):
        # doesn't work for all files, will crash for files like LICENSE
        if len(item.split(".")) <= 1:  
            scan_directories(os.path.join(path, item), items)
        else:
            items.append(item)

    return items


def count_items(files: list) -> str:
    files_dict = {}
    output_text = ""

    for file in files:
        file_name, extension = file.split(".")
        if extension not in files_dict:
            files_dict[extension] = []
        files_dict[extension].append(file_name)

    for extension, items in sorted(files_dict.items()):
        output_text += f"{extension}\n"
        for item in sorted(items):
            output_text += f"- - - {item}.{extension}\n"

    return output_text


def report(text: str) -> None:

    with open("report.txt", "w") as report_file:
        report_file.write(text)


def main() -> None:

    items = scan_directories(os.getcwd())
    report(count_items(items))


if __name__ == "__main__":
    main()
