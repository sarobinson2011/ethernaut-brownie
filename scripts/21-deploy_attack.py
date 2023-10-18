from scripts.helpful_scripts import get_account
from brownie import web3, interface, convert
from eth_utils import keccak


ETHERNAUT_INSTANCE = "0x4be13f805226d0e5d3e5069c4518e38FE574e0a8"
GAS_LIMIT = 6000000


def main():

    player = get_account()
