from scripts.helpful_scripts import get_account
from brownie import web3, interface, convert, DexTwo
from eth_utils import keccak


ETHERNAUT_INSTANCE = "0x058e398CDDc4D1756B5A5BE52F6D9f1c7F0a3D61"

GAS_LIMIT = 12000000


def main():
    player = get_account()
