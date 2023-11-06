from scripts.helpful_scripts import get_account
from brownie import web3, interface, convert, Attack24
from eth_utils import keccak

ETHERNAUT_INSTANCE = "0x05fBa7fcfA03f0b632Dc393e1fb8AE03943A4860"

GAS_LIMIT = 12000000


def main():
    player = get_account()
    target = interface.IPuzzleWallet(ETHERNAUT_INSTANCE)
    # attack = Attack24.deploy({"from": player})


 