import os

os.system("clear")

one = bytes.fromhex("4b9f4adb5c5781dc")
# two = bytes.fromhex("0000000000000000")
two = bytes.fromhex("1111111111111111")

result = bytes([a ^ b for a, b in zip(one, two)])

print(f"result in bytes = {result}")

print(f"\nresult in hex = {result.hex()}")
print(f"\nGATEKEY = {two.hex()}\n")

# require(
#               uint64(bytes8(keccak256(abi.encodePacked(msg.sender))))
#                  XOR
#               uint64(_gateKey)
#                   =
#               type(uint64).max

# uint64 gateKey = uint64(bytes8(keccak256(abi.encodePacked(address(this)))));
#
# gateKey = gateKey ^ type(uint64).max;
#
