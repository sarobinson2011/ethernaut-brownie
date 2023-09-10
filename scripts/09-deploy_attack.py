from scripts.helpful_scripts import get_account
from brownie import web3, interface, convert

ETHERNAUT_INSTANCE = "0x6397B7130662EEa63eBfD9fAfE82Fd053C1a21Bb"


def main():

    player = get_account()
    print(f"Player = {player}")
