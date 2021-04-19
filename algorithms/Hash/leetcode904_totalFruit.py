
def totalFruit(tree):
    picked = {}
    start = 0
    maxlen = 0
    for i, fruit in enumerate(tree):
        if fruit not in picked:
            picked[fruit] = 1
        else:
            picked[fruit] += 1

        if len(picked) <= 2:
            maxlen = max(maxlen, i - start + 1)
        else:
            while True:
                picked[tree[start]] -= 1
                if picked[tree[start]] == 0:
                    del picked[tree[start]]
                    break
                start += 1
            start += 1

    return maxlen


tree = [1, 2, 1]
print(totalFruit(tree))

tree = [0, 1, 2, 2]
print(totalFruit(tree))

tree = [1, 2, 3, 2, 2]
print(totalFruit(tree))

tree = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
print(totalFruit(tree))
