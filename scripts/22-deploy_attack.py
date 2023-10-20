from scripts.helpful_scripts import get_account
from brownie import web3, interface, convert, Attack22
from eth_utils import keccak


ETHERNAUT_INSTANCE = "0x54B33296970E87bde1504FB91E441008aB69347c"

TOKEN1 = "0x0cDbf0cb813020505f2C2C57187a3CB1249C34ad"
TOKEN2 = "0x3dE9BcAA4027ca200c22b159f70b683714Cd45F0"

GAS_LIMIT = 6000000


def main():

    player = get_account()
    target = interface.IDex(ETHERNAUT_INSTANCE)

    token_1 = target.token1({"from": player})
    token_2 = target.token2({"from": player})
    print(f"\ntoken_1 {token_1}, token_2 {token_2}\n")

    # attack = attack.deploy(ETHERNAUT_INSTANCE, {"from": player})

    balance_1 = target.balanceOf(TOKEN1, ETHERNAUT_INSTANCE)
    balance_2 = target.balanceOf(TOKEN2, ETHERNAUT_INSTANCE)
    print(
        f"\nbalance of token_1 = {balance_1}\
            \nbalance of token_2 = {balance_2}\n"
    )
