from scripts.helpful_scripts import get_account
from brownie import web3, interface, convert, Attack22
from eth_utils import keccak


ETHERNAUT_INSTANCE = "0x54B33296970E87bde1504FB91E441008aB69347c"
GAS_LIMIT = 6000000


def main():

    player = get_account()
    target = interface.IDex(ETHERNAUT_INSTANCE)

    token_1 = target.token1({"from": player})
    token_2 = target.token2({"from": player})
    print(f"\ntoken_1 {token_1}, token_2 {token_2}\n")

    # attack = attack.deploy(ETHERNAUT_INSTANCE, {"from": player})

    """
        Audit notes:

        1. xxx
        2. yyy

    """
