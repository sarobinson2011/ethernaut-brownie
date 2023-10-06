import os

os.system("clear")


""" 
    uint64 gateKey = uint64(
    bytes8(keccak256(abi.encodePacked(address(this))))
    );
    gateKey = gateKey ^ type(uint64).max;

"""

one = bytes.fromhex("4b9f4adb5c5781dc")
two = bytes.fromhex("FFFFFFFFFFFFFFFF")

result = bytes([a ^ b for a, b in zip(one, two)])

print(f"result in bytes = {result}")

print(f"\nresult in hex = {result.hex()}")
print(f"\nGATEKEY = {two.hex()}\n")

# require(
#     uint64(bytes8(keccak256(abi.encodePacked(msg.sender))))
#         XOR
#     uint64(_gateKey)
#          =
#     type(uint64).max

# <><><><>
# where msg.sender has to be a call from a smart contract constructor
# <><><><>

# uint64 gateKey = uint64(bytes8(keccak256(abi.encodePacked(address(this)))));
#
# gateKey = gateKey ^ type(uint64).max;
#
