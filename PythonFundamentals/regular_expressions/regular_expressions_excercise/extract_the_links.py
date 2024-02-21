import re


def extract_links(text: str):
    pattern = r"w{3}\.[A-Za-z0-9-]+(\.[a-z]+)+"
    link = re.search(pattern, text)
    if link:
        return link.group()
    return None


while True:
    input_text = input()
    if not input_text:
        break
    link = extract_links(input_text)
    if link:
        print(link)
