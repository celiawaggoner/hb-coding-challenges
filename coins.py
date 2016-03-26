
DIME = 10
PENNY = 1

def add_coins(coins_left, total, results):
    """Find the amount of each combination of coins"""

    #establish base case if all coins have been added
    if coins_left == 0:
        results.add(total)
        return 

    add_coins(coins_left - 1, total + DIME, results)
    add_coins(coins_left - 1, total + PENNY, results)


def coins(num_coins):
    """Find change from combinations of `num_coins` of dimes and pennies.

    This should return a set of the unique amounts of change possible.
    """

    results = set()

    add_coins(coins_left=num_coins, total=0, results=results)

    return results
