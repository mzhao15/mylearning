def coinChange(coins, amount):
    if amount == 0:
        return 0

    DP = [0] * (amount+1)

    for num in coins:
        if num <= amount:
            DP[num] = 1

    for i in range(1, amount+1):
        min_cur = float('inf')
        for num in coins:
            if i - num >= 0:
                if DP[i-num] + 1 < min_cur:
                    min_cur = DP[i-num] + 1
        DP[i] = min_cur
    # print(DP)
    return DP[-1] if DP[-1] != float('inf') else -1


coins = [1, 2, 5]
amount = 11
print(coinChange(coins, amount))

coins = [2]
amount = 3
print(coinChange(coins, amount))

coins = [1]
amount = 0
print(coinChange(coins, amount))

coins = [1]
amount = 1
print(coinChange(coins, amount))

coins = [1]
amount = 2
print(coinChange(coins, amount))
