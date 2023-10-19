from scripts.helpful_scripts import get_account
from brownie import web3, interface, convert, Attack21
from eth_utils import keccak


ETHERNAUT_INSTANCE = "0x4be13f805226d0e5d3e5069c4518e38FE574e0a8"
GAS_LIMIT = 6000000


def main():

    player = get_account()
    # target = interface.IShop(ETHERNAUT_INSTANCE)
    attack = Attack21.deploy({"from": player})
    attack.attack({"from": player})


""" 
    Audit notes:

    - Shop expects to be called from a Buyer
        -- use the price() function to launch the attack?
    
    - make the following == True to win:
        -- (_buyer.price() >= price && !isSold) 

    - where _buyer.price() calls the price() function in Attack21

    - issue: price() has the view modifier ???

"""
