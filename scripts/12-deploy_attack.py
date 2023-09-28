from scripts.helpful_scripts import get_account
from brownie import web3, Attack12

ETHERNAUT_INSTANCE = ""
GAS_LIMIT = 6000000


def main():

    player = get_account()
