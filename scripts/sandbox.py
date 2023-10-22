"""
        Audit notes:

        1. Dex contract
            - storage slot 0, 1, 2 -> contain addresses
        2. SwappableToken contract
            - we can ignore this as the approve method is included
              in the Dex contract (for ease)
        3. Function swap() is where the token transfer happens
       
        4. Swap price calculation
        
            - (amount * 'to' price) / ('from' price)
                so: swap price == amount * (token ratio)
    
        5. Swap process ->

            - xyz
                - abc

                
        Q. How do you approve a transaction of an ERC20?
            
            - approve the contract to spend your tokens

    """

# we want a swap_amount > 100


def main():

    # Initialise variables
    ETH_pool_balance = 100
    WBTC_pool_balance = 100
    ETH_player = 10
    WBTC_player = 10
    amount_to_swap = 10

    # get the swap "price/amount"
    _swap = swap(ETH_player, WBTC_player, amount_to_swap)
    # update pool balances
    ETH_pool_balance -= _swap
    WBTC_pool_balance += _swap
    ETH_player -= _swap
    WBTC_player += _swap
    print_balances(ETH_pool_balance, WBTC_pool_balance, ETH_player, WBTC_player)
    # amount_to_swap =


def swap(balance_1, balance_2, amount):
    swap_amount = amount * balance_1 / balance_2
    return swap_amount


def print_balances(eth_pool, wbtc_pool, eth_player, wbtc_player):
    print(f"ETH-pool balance: {eth_pool}")
    print(f"WBTC-pool balance: {wbtc_pool}")
    print(f"ETH-player balance: {eth_player}")
    print(f"WBTC-player balance: {wbtc_player}")


# toggle from
# if from == token1:
#     from = token2
# else:
#     from = token1

# while token1_balance != 0 and token2_balance != 0:
#     pass
