from scripts.helpful_scripts import get_account
from brownie import web3, network, interface, convert, Attack24, PuzzleWallet, PuzzleProxy, Contract
from eth_utils import keccak

GAS_LIMIT = 6000000


def main():

    # initalise player, target etc.    
    player = get_account()

