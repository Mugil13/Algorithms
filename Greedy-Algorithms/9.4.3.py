def min_coins(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [-1] * (amount + 1)  

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i] > dp[i - coin] + 1:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin  

    if dp[amount] == float('inf'):
        return dp[amount], []  

    used_coins = []
    current_amount = amount
    while current_amount > 0:
        used_coins.append(coin_used[current_amount])
        current_amount -= coin_used[current_amount]

    return dp[amount], used_coins

coins = [1]

denominations_length = int(input("Enter the number of coins (1 is already included): "))

for i in range(denominations_length):
    denomination = int(input("Enter the coin denomination: "))
    coins.append(denomination)

print("\n")
amount = int(input("Enter the amount to make change: "))
min_num_coins, coins_used = min_coins(coins, amount)
print("Minimum number of coins required:", min_num_coins)
print("List of coins used:", coins_used)
