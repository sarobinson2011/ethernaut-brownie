import os

os.system("clear")

one = bytes.fromhex("4b9f4adb5c5781dc")
two = bytes.fromhex("0000000000000000")

result = bytes([a ^ b for a, b in zip(one, two)])

print(f"result in bytes = {result}")

print(f"\nresult in hex = {result.hex()}")
print(f"\nGATEKEY = {two.hex()}\n")
