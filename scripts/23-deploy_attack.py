from scripts.helpful_scripts import get_account
from brownie import web3, interface, convert, DexTwo
from eth_utils import keccak


ETHERNAUT_INSTANCE = "0xdA3ecB48DFeEB21B4b2B177d64d6dfB2B8FE884e"

TOKEN1 = "0xC05734547415687cF19482183D58a2E173f2Ebd6"
TOKEN2 = "0x3021528D0f836c13278CD2eD990893008724B5F9"

GAS_LIMIT = 12000000


def main():
    player = get_account()
    target = interface.IDexTwo(ETHERNAUT_INSTANCE)


""" 
        Audit notes

    1. function swap() has been modified, from Dex (one)
        
    1a. the following require statement has been removed:

        require((from == token1 && to == token2) || (from == token2 && to == token1), "Invalid tokens");

    2.  


"""
