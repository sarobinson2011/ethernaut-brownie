from scripts.helpful_scripts import get_account
from brownie import web3, Attack11

ETHERNAUT_INSTANCE = "0x454145f33FD63Bbb1932B9006f125800f155C577"


def main():

    player = get_account()
