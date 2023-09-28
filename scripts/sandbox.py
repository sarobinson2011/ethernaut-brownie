original_bytes32 = b"12345678901234567890123456789012"  # A 32-byte value

bytes16_casted = bytes(original_bytes32[:16])  # Typecast to bytes16

a = bytes16_casted
print(a)
print(len(a))

# so    -->

key = bytes(original_bytes32[:16])
