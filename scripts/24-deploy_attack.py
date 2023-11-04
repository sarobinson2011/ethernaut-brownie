from scripts.helpful_scripts import get_account
from brownie import web3, interface, convert, Attack24
from eth_utils import keccak

ETHERNAUT_INSTANCE = "0xd206fd0618e91Da883D764c6d891d67591881dbb"

GAS_LIMIT = 12000000


def main():
    player = get_account()
    target = interface.IPuzzleWallet(ETHERNAUT_INSTANCE)
    attack = Attack24.deploy({"from": player})
