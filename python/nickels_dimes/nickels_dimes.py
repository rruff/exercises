#!/usr/bin/env python3
#
# A pile of coins contains only nickels and dimes.
# Given the total amount of dollars and cents, and the total number of coins, determine
# the number of nickels and the number of dimes.

def assert_count_correct(dollars, cents, nickels, dimes):
    assert ((dollars * 100) + cents) == ((nickels * 5) + (dimes * 10))

def count_nickels_and_dimes(dollars, cents, total_coins):
    """ Returns a tuple containing the the number of nickels and the number of dimes.
    
    Parameters
    dollars : int, required 
        The number of dollars
    cents : int, required
        The number of cents
    total_coins : int, required
        The total number of coins

    Returns
    tuple
        A tuple containing the number of nickels and the number of dimes
    """
    
    dimes = dollars * 10
    nickels = 0

    # If the pile of coins contains only nickels and dimes, we can assume
    # the total amount of money is evenly divisible by 5.
    if cents % 10 == 5:
        nickels += 1
    dimes += int(cents / 10)
    coin_count = dimes + nickels

    if coin_count == total_coins:
        assert_count_correct(dollars, cents, nickels, dimes)
        return (nickels, dimes)

    if coin_count > total_coins:
        # At this point the majority of the coins are dimes. If we've already exceeded the provided
        # number of coins, subtracting dimes and adding nickels will only increase the count even more.
        raise ValueError(f'Not enough coins to make ${dollars}.{cents} using only nickels and dimes.')
    
    while coin_count < total_coins:
        dimes -= 1
        nickels += 2
        coin_count = dimes + nickels

    assert_count_correct(dollars, cents, nickels, dimes)
    return (nickels, dimes)

if __name__ == '__main__':
    amount = input("Enter an amount of money in dollars and cents: $")
    coins = input("Enter the total number of coins: ")
    
    dollars, cents = amount.split('.')
    nickels, dimes = count_nickels_and_dimes(int(dollars), int(cents), int(coins))
    print(f"{nickels=}, {dimes=}")
