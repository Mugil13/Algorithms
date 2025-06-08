denominations = [25, 10, 5, 1]

def make_change(amount):
    coins_used = []
    for coin in denominations:
        while amount >= coin:
            coins_used.append(coin)
            amount -= coin
    return coins_used

amount = int(input("Enter the amount to make change: "))

print("Coins used:", make_change(amount))
print("Number of coins used: ", len(make_change(amount)))
