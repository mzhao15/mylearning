def reformatNumber(number):
    size = 0
    numbers = []
    for ch in number:
        if ch != '-' and ch != ' ':
            numbers.append(ch)
            size += 1

    if len(numbers) == 3:
        return ''.join(numbers)

    if len(numbers) == 4:
        return ''.join(numbers[:2] + ['-'] + numbers[2:])

    d, resid = size//3, size % 3

    if resid == 1:
        resid = 4
        d -= 1

    k = 1
    ans = []
    while k <= d:
        ans += numbers[3*(k-1):3*k]
        ans += ['-']
        k += 1

    if resid == 4:
        ans += numbers[3*d:3*d+2]
        ans += ['-']
        ans += numbers[3*d+2:]
    elif resid == 0:
        ans.pop()
    else:
        ans += numbers[3*d:]

    return ''.join(ans)


number = "1-23-45 6"
print(reformatNumber(number))

number = "123 4-567"
print(reformatNumber(number))

number = "123 4-5678"
print(reformatNumber(number))

number = "12"
print(reformatNumber(number))

number = "1234"
print(reformatNumber(number))
