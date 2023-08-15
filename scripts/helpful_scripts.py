from brownie import accounts, config, network

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "mainnet-fork", "ganache"]


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if id:
        return accounts[id]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])
