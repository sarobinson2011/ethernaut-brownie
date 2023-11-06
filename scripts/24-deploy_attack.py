from scripts.helpful_scripts import get_account
from brownie import web3, network, interface, convert, Attack24
from eth_utils import keccak

ETHERNAUT_INSTANCE = "0x05fBa7fcfA03f0b632Dc393e1fb8AE03943A4860"

GAS_LIMIT = 12000000


def proxy_balance():
     # current balance of PuzzleProxy
    balance = web3.eth.getBalance(ETHERNAUT_INSTANCE)
    balance_eth = web3.fromWei(balance, "ether")
    print(f"\nbalance in wei = {balance}\nbalance in ether = {balance_eth}\n")


def main():
    player = get_account()
    target = interface.IPuzzleWallet(ETHERNAUT_INSTANCE)
    # attack = Attack24.deploy({"from": player})
    proxy_balance()
   


"""
    Notes:

    storage slot 0 has a collision - pendingAdmin and owner share the same slot

    1. set pendingAdmin by calling --> proposeNewAdmin(player)

    2. now: owner == address(player)

    3. call addToWhiteList(player)

    4. player is now 'white listed'

    5.  --> next we need to empty the contract balance to zero 

    6. 

"""






 