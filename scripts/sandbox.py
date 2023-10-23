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
    toggle = True

    for i in range(2):

        """
        you're swapping between:

        a) the player account (which contains 2 different tokens) ,and

        b) the pool (which contains 2 different tokens)

        """

        if toggle:
            A = ETH_pool_balance
            B = WBTC_pool_balance
            amount_to_swap = ETH_player
        else:
            A = WBTC_pool_balance
            B = ETH_pool_balance
            amount_to_swap = ETH_player

        # get the swap "price/amount"
        swap_amount = swap(A, B, amount_to_swap)

        # update pool balances
        ETH_pool_balance -= swap_amount
        WBTC_pool_balance += swap_amount
        ETH_player -= swap_amount
        WBTC_player += swap_amount

        print_balances(
            ETH_pool_balance, WBTC_pool_balance, ETH_player, WBTC_player, toggle
        )

        toggle = not toggle

        # if ETH_player == 0:
        #     amount_to_swap = WBTC_player
        # elif WBTC_player == 0:
        #     amount_to_swap = ETH_player


def swap(balance_1, balance_2, amount):
    swap_amount = amount * balance_1 / balance_2
    return swap_amount


def print_balances(eth_pool, wbtc_pool, eth_player, wbtc_player, toggle):
    print(f"\ntoggle = {toggle}")
    print(f"ETH-pool balance: {eth_pool}")
    print(f"WBTC-pool balance: {wbtc_pool}")
    print(f"ETH-player balance: {eth_player}")
    print(f"WBTC-player balance: {wbtc_player}\n")


# toggle from
# if from == token1:
#     from = token2
# else:
#     from = token1

# while token1_balance != 0 and token2_balance != 0:
#     pass
