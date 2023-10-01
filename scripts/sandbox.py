# original_bytes32 = b"12345678901234567890123456789012"  # A 32-byte value

# bytes16_casted = bytes(original_bytes32[:16])  # Typecast to bytes16

# print(bytes16_casted)
# print(len(bytes16_casted))

# key = original_bytes32[:16]
# print(key)

import os

GATE_HEX = "eE25"

os.system("clear")
gate_key = int(GATE_HEX, 16)
# gate_key = 60965
print(gate_key)

