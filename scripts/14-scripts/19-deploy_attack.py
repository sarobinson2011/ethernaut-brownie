from scripts.helpful_scripts import get_account
from brownie import web3, interface, Attack19


ETHERNAUT_INSTANCE = "0xc62350eC49Fa6B04415CF7973cD773f989D8d76d"
GAS_LIMIT = 6000000


def main():

    player = get_account()
