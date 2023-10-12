from scripts.helpful_scripts import get_account
from brownie import web3, interface, whatIsTheMeaningOfLife


ETHERNAUT_INSTANCE = "0x5d8dA349A621CC0131e1617034Af526ab56E23C4"
GAS_LIMIT = 6000000

SOLVER = "0x000000000000000000000000000000000000002a"


def main():

    """update manually to first view the output"""
    # player = get_account()
    # print(f"\nSolver 'pre' is: {web3.eth.get_storage_at(ETHERNAUT_INSTANCE, 0)}\n")
    # target = interface.IMagicNum(ETHERNAUT_INSTANCE)
    # target.setSolver(SOLVER, {"from": player})
    # print(f"\nSolver 'post' is: {web3.eth.get_storage_at(ETHERNAUT_INSTANCE, 0)}\n")

    """ update via attack contract """
    player = get_account()
    attack = whatIsTheMeaningOfLife.deploy({"from": player})

    attack.attack(SOLVER, {"from": player})
