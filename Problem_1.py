def coinCount(coins, amount):
    #creating infinite coins for each type
    coinArry = [float('inf')] * (amount + 1)
    coinArry[0] = 0 

    #fill the array
    for coin in coins:
        for x in range(coin, amount + 1):
            #check if the current coin lowers the amount needed
            coinArry[x] = min(coinArry[x], coinArry[x - coin] +1)

    # return result or -1 if amount cannot be made up by any combination
    return coinArry[amount] if coinArry[amount] != float('inf') else -1

coins1 = [1,2,5]
amount1 = 11
print("Fewest Coins:", coinCount(coins1, amount1))

coins2 = [2]
amount2 = 3
print("Fewest Coins:", coinCount(coins2, amount2))

coins3 = [1]
amount3 = 0
print("Fewest Coins:", coinCount(coins3, amount3))