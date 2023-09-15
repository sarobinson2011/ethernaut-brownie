from scripts.helpful_scripts import get_account
from brownie import web3, Attack09, convert, interface

ETHERNAUT_INSTANCE = "0xc734f6B53Ac3b11afdeE4cA1dbFee83521ED267d"


def main():

    player = get_account()
