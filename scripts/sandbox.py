# bytes    uint
#   1       8
#   2       16
#   4       32
#   8       64
#   16      128
#   20      160   <-- Ethereum address length (bytes20 <-> uint160)
#   32      256


# TX_ORIGIN = "0xF8f8269488f73fab3935555FCDdD6035699deE25"

# uint64(bytes8(keccak256(abi.encodePacked(msg.sender)))) ^ uint64(_gateKey) == type(uint64).max
#
# uint64(bytes8(keccak256(abi.encodePacked(msg.sender)))) ^ uint64(_gateKey)
#       == type(uint64).max
#       == 2^64 - 1
#       == "FFFF FFFF FFFF FFFF" in (bytes8)
#
# bytes8(keccak256(abi.encodePacked(msg.sender))) ^ gateKey == "FFFFFFFFFFFFFFFF"
#
# 0x4b9f4adb5c5781dc ^ gateKey == "FFFFFFFFFFFFFFFF"
# therefore gateKey == "0000000000000000"

import os

os.system("clear")

one = bytes.fromhex("4b9f4adb5c5781dc")
two = bytes.fromhex("0000000000000000")

result = bytes([a ^ b for a, b in zip(one, two)])
print(f"result in bytes = {result}")

print(f"\nresult in hex = {result.hex()}")
print(f"\nGATEKEY = {two.hex()}\n")
