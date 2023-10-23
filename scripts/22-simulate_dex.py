# it takes 5 swaps to get to:
#   ETH-pool balance: 43
#   WBTC-pool balance: 156
#   ETH-player balance: 0
#   WBTC-player balance: 86
#
# swap 6 will drain the remains of the ETH-pool balance,
# resulting in a "bad" price to be returned


def main():

    # Initialise variables
    ETH_pool_balance = 100
    WBTC_pool_balance = 100
    ETH_player = 10
    WBTC_player = 10
    amount_to_swap = 10
    swap_amount = 10
    toggle = True
    i = 0

    print_balances(
        ETH_pool_balance, WBTC_pool_balance, ETH_player, WBTC_player, toggle, i
    )

    for i in range(6):
        if toggle:
            A = ETH_pool_balance
            B = WBTC_pool_balance
            amount_to_swap = ETH_player
        else:
            A = WBTC_pool_balance
            B = ETH_pool_balance
            amount_to_swap = WBTC_player

        # get the swap "price/amount"
        swap_amount = swap(A, B, amount_to_swap)

        # update pool balances
        if toggle:
            ETH_pool_balance -= swap_amount
            WBTC_pool_balance += swap_amount
            ETH_player -= amount_to_swap
            WBTC_player += swap_amount
        else:
            WBTC_pool_balance -= swap_amount
            ETH_pool_balance += swap_amount
            WBTC_player -= amount_to_swap
            ETH_player += swap_amount

        print_balances(
            ETH_pool_balance, WBTC_pool_balance, ETH_player, WBTC_player, toggle, i
        )

        toggle = not toggle


def swap(balance_1, balance_2, amount):
    swap_amount = amount * balance_1 / balance_2
    return swap_amount


def print_balances(eth_pool, wbtc_pool, eth_player, wbtc_player, toggle, i):
    print(f"\nIteration: {i}")
    print(f"toggle = {toggle}")
    print(f"ETH-pool balance: {int(eth_pool)}")
    print(f"WBTC-pool balance: {int(wbtc_pool)}")
    print(f"ETH-player balance: {int(eth_player)}")
    print(f"WBTC-player balance: {int(wbtc_player)}\n")
