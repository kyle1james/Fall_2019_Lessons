# This problem was asked by Square.
# 
# In front of you is a row of N coins, with values v1, v1, ..., vn.
# 
# You are asked to play the following game. You and an opponent take 
# turns choosing either the first or last coin from the row, removing 
# it from the row, and receiving the value of the coin.
# 
# Write a program that returns the maximum amount of money you can win 
# with certainty, if you move first, assuming your opponent plays optimally.

coins =  [10, 24, 5, 9]

def max_play(coins, value):
    if len(coins) == 1:
        return value + coins
    elif len(coins) == 2:
        return value + max(coins)
    else:
        return value + max(
        coins[0] +  min(max_play(coins[2:], value), max_play(coins[1:-1], value)),
        coins[-1] + min(max_play(coins[:-2], value), max_play(coins[1:-1], value))
        
        )

print(max_play(coins,0))
    