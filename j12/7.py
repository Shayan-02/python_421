with open("1.txt", "a", encoding="utf-8") as f:
    f.write("\nمتن جدید")


with open("1.txt", "r+", encoding="utf-8") as g:
    print(g.read())