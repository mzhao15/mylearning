def numRescueBoats(people, limit):
    people.sort()
    print(people)
    i = 0
    j = len(people)-1
    ans = 0
    while people[j] == limit:
        ans += 1
        j -= 1
    while i <= j:
        if people[i] + people[j] <= limit:
            ans += 1
            i += 1
            j -= 1
        else:
            j -= 1
            ans += 1
    return ans


people = [3, 5, 3, 4]
limit = 5
print(numRescueBoats(people, limit))

people = [3, 2, 2, 1]
limit = 3
print(numRescueBoats(people, limit))
