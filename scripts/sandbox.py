from scripts.helpful_scripts import get_account
from brownie import web3, Attack07
from web3 import Web3

# PLAYER address is "0xF8f8269488f73fab3935555FCDdD6035699deE25"

ETHERNAUT_INSTANCE = "0x6f50CaAf6E4AD72C66E0e60A61eEF58Db2018447"
BALANCE = web3.eth.getBalance(ETHERNAUT_INSTANCE)


def main():

    # player = get_account()
    print(f"Balance = {BALANCE}")
