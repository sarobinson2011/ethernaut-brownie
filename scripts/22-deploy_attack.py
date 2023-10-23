from scripts.helpful_scripts import get_account
from brownie import web3, interface, convert, Attack22
from eth_utils import keccak


ETHERNAUT_INSTANCE = "0x54B33296970E87bde1504FB91E441008aB69347c"
TOKEN1 = "0x0cDbf0cb813020505f2C2C57187a3CB1249C34ad"
TOKEN2 = "0x3dE9BcAA4027ca200c22b159f70b683714Cd45F0"
AMOUNT = 5

GAS_LIMIT = 6000000


def main():

    player = get_account()
    target = interface.IDex(ETHERNAUT_INSTANCE)

    token_1 = target.token1({"from": player})
    token_2 = target.token2({"from": player})
    print(f"\ntoken_1 {token_1}, token_2 {token_2}\n")

    balance_1 = target.balanceOf(TOKEN1, ETHERNAUT_INSTANCE)
    balance_2 = target.balanceOf(TOKEN2, ETHERNAUT_INSTANCE)
    print(
        f"\nbalance of token_1 = {balance_1}\
            \nbalance of token_2 = {balance_2}\n"
    )

    swap_price = target.getSwapPrice(TOKEN1, TOKEN2, AMOUNT)
    print(f"\nSwap price (1 to 2) amount: {AMOUNT} = {swap_price}\n")


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

            - see 22-simulate_dex.py (this models the swap process)
                       
"""
