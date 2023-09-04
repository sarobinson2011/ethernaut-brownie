from scripts.helpful_scripts import get_account
from brownie import Attack05

# new instance of Level 05 - Token
ETHERNAUT_INSTANCE = "0x292597B71806e65B2c42b773055AAe6ed09bfC57"


def main():

    player = get_account()
    attacker_contract = Attack05.deploy(ETHERNAUT_INSTANCE, {"from": player})

    print(f"attacker contract: {attacker_contract}")
