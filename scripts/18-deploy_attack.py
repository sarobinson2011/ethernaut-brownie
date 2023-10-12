from scripts.helpful_scripts import get_account
from brownie import web3, interface, Attack18


ETHERNAUT_INSTANCE = "0xc62350eC49Fa6B04415CF7973cD773f989D8d76d"
GAS_LIMIT = 6000000


def main():

    """update manually to first view the output"""
    # player = get_account()
    # print(f"\nSolver 'pre' is: {web3.eth.get_storage_at(ETHERNAUT_INSTANCE, 0)}\n")
    # target = interface.IMagicNum(ETHERNAUT_INSTANCE)
    # target.setSolver(SOLVER, {"from": player})
    # print(f"\nSolver 'post' is: {web3.eth.get_storage_at(ETHERNAUT_INSTANCE, 0)}\n")

    """ update via attack contract """
    player = get_account()
    attack = Attack18.deploy(ETHERNAUT_INSTANCE, {"from": player})
