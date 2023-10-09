from scripts.helpful_scripts import get_account
from brownie import web3, interface, Attack16


ETHERNAUT_INSTANCE = "0xA75368BA443F90EF8B554696e59a60B5695DeE30"
GAS_LIMIT = 600000


def main():

    player = get_account()

    attack = Attack16.deploy({"from": player})
