from scripts.helpful_scripts import get_account
from brownie import Attack05

ETHERNAUT_INSTANCE = "0x2E5f4De64770d3A1B2740Ac71254929717C43c24"


def main():

    player = get_account()

    attacker_contract = Attack05.deploy(ETHERNAUT_INSTANCE, {"from": player})

    print(f"attacker contract: {attacker_contract}")
