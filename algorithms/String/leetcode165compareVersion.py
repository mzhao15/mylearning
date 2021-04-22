def compareVersion2(version1, version2):

    v1 = version1.split('.')
    v2 = version2.split('.')

    maxlen = max(len(v1), len(v2))

    v1 = v1 + [0] * (maxlen - len(v1))
    v2 = v2 + [0] * (maxlen - len(v2))

    for i in range(maxlen):
        if int(v1[i]) > int(v2[i]):
            return 1
        elif int(v1[i]) < int(v2[i]):
            return -1
    return 0


def compareVersion(version1, version2):
    # not correct. some corner cases not handled

    n1 = len(version1)
    n2 = len(version2)

    if n1 == 0 and n2 == 0:
        return 0
    elif n1 == 0 and n2 != 0:
        return -1
    elif n1 != 0 and n2 == 0:
        print(1)
        return 1

    i = 0
    j = 0

    while i < n1 and version1[i] == '0':
        i += 1
    while j < n2 and version2[j] == '0':
        j += 1

    if i == n1 or version1[i] == '.':
        v1 = 0
    else:
        v1num = ''
        while i < n1 and version1[i] != '.':
            v1num += version1[i]
            i += 1
        v1 = int(v1num)

    if j == n2 or version2[j] == '.':
        v2 = 0
    else:
        v2num = ''
        while j < n2 and version2[j] != '.':
            v2num += version2[j]
            j += 1
        v2 = int(v2num)

    if v1 < v2:
        return -1
    elif v1 > v2:
        return 1
    else:
        # print(version1[i+1:], version2[j+1:])
        return compareVersion(version1[i+1:], version2[j+1:])


version1 = "1.01"
version2 = "1.001"
print(compareVersion(version1, version2))

version1 = "1.0"
version2 = "1.0.0"
print(compareVersion(version1, version2))

version1 = "0.1"
version2 = "1.1"
print(compareVersion(version1, version2))

version1 = "1.0.1"
version2 = "1"
print(compareVersion(version1, version2))

version1 = "7.5.2.4"
version2 = "7.5.3"
print(compareVersion(version1, version2))
