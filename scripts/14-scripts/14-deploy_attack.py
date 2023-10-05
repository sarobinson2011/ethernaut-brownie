from scripts.helpful_scripts import get_account
from brownie import web3, interface, Attack14


ETHERNAUT_INSTANCE = "0xc47e9de2c5a85084f777f94C926585ea49490E1a"
PLAYER = "0xF8f8269488f73fab3935555FCDdD6035699deE25"
GAS_LIMIT = 6000000

# GATEKEY = "0x 0000 0000 0000 0000"
# GATEKEY = "1111111111111111"
GATEKEY = "5a8e5bca4d4690cd"


def main():

    player = get_account()
    Attack14.deploy(
        ETHERNAUT_INSTANCE,
        {"from": player, "gas_limit": GAS_LIMIT, "allow_revert": True},
    )


# Gate One: deploy proxy contract (conflict with Gate Two) <-- PROBLEM_1


# Gate Two: Require that the 'codesize' (in bytes) of the code at the call address
#           is equal to zero.  So caller needs to have zero code size
#
#   --> unless the call is made from the constructor of a smart contract  <-- SOLVED_1


# Gate Three:
#
# uint64(bytes8(keccak256(abi.encodePacked(msg.sender))))  XOR  uint64(_gateKey)
#   =  type(uint64).max
#
#   -->  see 14-calculate_keccak.py and 14-calculate_gatekey.py
