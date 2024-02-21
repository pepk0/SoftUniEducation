head_one = input()
article = input()
print(f"<h1>\n    {head_one}\n</h1>",
      f"<article>\n    {article}\n</article>", sep="\n")

while True:
    comment = input()
    if comment == "end of comments":
        break
    print(f"<div>\n    {comment}\n</div>")
