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


"""

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

        We can however perform indirect calls, so if we pass multicall a data array that contains 
        calls to multicall.  So multicall will call multicall 30 times, and each individual call within
        that will call deposit() once.  Thus we get 30 deposits in a single deposit() call.

        This unbalances the contract accounting logic and we are able to drain the contract balance.
        

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






 