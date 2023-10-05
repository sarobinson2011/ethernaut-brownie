from web3 import Web3

# Initialize a Web3 instance (you need to connect to an Ethereum node)
w3 = Web3(
    Web3.HTTPProvider("https://mainnet.infura.io/v3/3248eacd73a6414483cd73d32e31a3b4")
)  # Replace with your Ethereum node URL
msg_sender_address = "0xF8f8269488f73fab3935555FCDdD6035699deE25"

# Encode the address using web3.py
encoded_address = w3.solidityKeccak(["address"], [msg_sender_address])
print(f"\nKeccak-256 hash: {encoded_address.hex()}")

# Convert the Keccak-256 hash to bytes
hash_bytes = bytes.fromhex(
    encoded_address.hex()[2:]
)  # Remove the '0x' prefix and convert to bytes

# Take the first 8 bytes (64 bits)
bytes8_value = hash_bytes[:8]

print(f"\nbytes8 value: {bytes8_value.hex()}\n")
# == "0x4b9f4adb5c5781dc"

""" 
    XOR function
    
    A  |  B  |  Q
    -------------
    0  |  0  |  0
    0  |  1  |  1
    1  |  0  |  1  
    1  |  1  |  0

    There are no zeros in '0x4b9f4adb5c5781dc'
    therefore GateKey ==  '0x0000000000000000' 

"""
