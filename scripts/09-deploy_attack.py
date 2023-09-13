from scripts.helpful_scripts import get_account
from brownie import web3, interface, convert

ETHERNAUT_INSTANCE = "0x36A486BAe1988F4aCB1F9ab5e0606A7A9f635C4f"
PRIZE = 30000000


def main():

    player = get_account()
    print(f"Player = {player}")
