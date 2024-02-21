import re


def extract_title(text: str) -> str:
    pattern = r"<title>(.*)<\/title>"
    title = re.search(pattern, text).group(1)  # type: ignore
    title = re.sub(r"\\n|\\t", "", title)
    title = re.sub(r"<[^>]*>", "", title)
    return title


def extract_content(text: str) -> str:
    match_pattern = r"<body>(.*)</body>"
    content = re.search(match_pattern, text).group(1)  # type: ignore
    content = re.sub(r"\\n|\\t", "", content)
    content = re.sub(r"<[^>]*>", "", content)
    return content


html_dom = input()
print(f"Title: {extract_title(html_dom)}")
print(f"Content: {extract_content(html_dom)}")
