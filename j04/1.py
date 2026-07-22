def solve(s):
    result = []

    for char in s:
        if char == '=':
            if result:
                result.pop()
        else:
            result.append(char)

    for _ in range(len(result)):
        print(result[_], end="")

word = input().strip()
solve(word)
