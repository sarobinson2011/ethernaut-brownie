""" Python script to perform bitwise AND '&' operation on 2 hex vales """

first16 = bytes.fromhex("F8f8269488f73fab")
mask = bytes.fromhex("FFFFFFFF0000FFFF")

# Convert bytes to integers
first16_int = int.from_bytes(first16, byteorder="big")
mask_int = int.from_bytes(mask, byteorder="big")

# Perform bitwise AND operation
result_int = first16_int & mask_int

# Convert the result back to bytes
gate_key = result_int.to_bytes((result_int.bit_length()) // 8, byteorder="big")

print(gate_key.hex())
