from scripts.helpful_scripts import get_account
from brownie import Attack05

# new instance of Level 05 - Token
ETHERNAUT_INSTANCE = "0x5169932Cd522b4d625dfFE5639EE821EdE2C87c6"


def main():

    player = get_account()
    attacker_contract = Attack05.deploy(ETHERNAUT_INSTANCE, {"from": player})

    print(f"attacker contract: {attacker_contract}")
