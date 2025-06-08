c = int(input("Enter the base value of c: "))
amount = int(input("Enter the amount to make change: "))

denominations = []
for i in range(100):
    if c ** i > amount:
        break
    denominations.append(c ** i)

denominations.sort(reverse=True)

def make_change(amount):
    coins_used = []
    for coin in denominations:
        while amount >= coin:
            coins_used.append(coin)
            amount -= coin
    return coins_used

coins_used = make_change(amount)

print("Coins used:", coins_used)
print("Number of coins used:", len(coins_used))
