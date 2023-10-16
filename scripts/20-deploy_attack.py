from scripts.helpful_scripts import get_account
from brownie import web3, interface, convert
from eth_utils import keccak


ETHERNAUT_INSTANCE = "0xa5827B90Fd50E8ccCDA14385aaB7966d2F66d5D9"
GAS_LIMIT = 6000000


def main():

    player = get_account()
