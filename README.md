# Ethernaut Level Solutions (using Brownie)

### Levels split into individual folders, under contracts...


- 03-Coin Flip
        -->     SOLVED
        
        Solution lies in the fact that a blockchain is a deterministic data structure, and as such there is no way of generating a random number with sufficient entropy, that cannot be gamed.
        So, we simply copy and paste the code that creates the "random result" into an attack contract.
        Run this (which happens concurrently with the original contract - it's a blockchain remember!), with a require "correct result" statement.
        Then we simply keep flipping the coin until we have 10 wins.

- 04-Telephone
        -->     SOLVED

        Solution creates an instance of the Attack04 contract.
        Passes the Telephone contract to it's Constructor.
        When you then call attack on the Attack04 contract, it triggers changeOwner().
        This shows how you use a proxy contract to attack a deployed contract.


- 05-Token
        -->     SOLVED

        Solution sets up an interface, in order to interact with the Token contract.
        Then calls transfer to a random address, for 21 tokens. 
        This causes the 0.6.0 solidity code to underflow a uint256.  
        Balance then gets sent to msg.sender (in the original contract).

- 06-Delegation
        -->     SOLVED

        Solution uses the transfer method to interact with contract Delegate.
        The data passed to Delegate is the 'function selector' for the pwn() function.
        This is the first 5 bytes from keccak256 hash of "pwn()".
        Fallback is called, which uses delegatecall to effectively call the pwn() function.
        Thus ownership is transferred to 'msg.sender' from 'Delegation'.

- 07-Force
        -->     SOLVED

        Solution uses the selfdestruct in-built function to 'force transfer' funds over.
        A proxy contract Attack07 is deployed with a payable constructor && the receive function.
        Attack07 can be loaded with funds using either the constructor or receive method.
        The function 'attack' calls selfdestruct, with the Force contract address an argument.
        Selfdestruct force-sends all funds in the contract to the Force contract address.
        Attack07 then destroys itself, as per the selfdestruct() functionality.
                
- 08-Vault
        -->     SOLVED  

        Solution exploits the inability of deterministic blockchains to store security sensitive date, such as passwords.
        Password is easily obtained via:

        - password = web3.eth.get_storage_at(ETHERNAUT_INSTANCE, 1).
        
        - Where ETHERNAUT_INSTANCE is the contract address
        - '1' is the memory storage slot - run this with 0, 1, 2 see what happens ;-0
        
        Then simply use the vault interface to interact and call unlock(password) to win.

- 09-King
        -->
                SOLVED

        Solution exploits the fact it is not possible to 'catch a revert' that occurs in an *external* contract when using the transfer() function.
        When the transfer function encounters a revert in the recipient contract, it also reverts the entire transaction that called it, including the receive() function.
        Assumption is that the developers assumed all "players" would be EOAs.
        Soultion is to use the call() function, which does have the ability to handle reverts and errors.
        See "transaction diagram" (check naming convention) for more details.

- 10-Re-entrancy
        -->
                SOLVED

        Solution is simple to describe, but proved a little more tricky to implement in practice.
        Fully working Solidity and Brownie (Python) code is publicly available in GitHub repo.

        The security flaw in the lies in the withdraw(uint _amount) function, that transfers funds
        BEFORE subtracting the transfer from the account balance. 
        After checking that the account has funds to withdraw, a low-level call  is made to msg.sender, 
        to transfer the funds.
        
        I guess the code was written assuming calls from EOAs, but if the call is made from a proxy contract
        we can then include a receive() function, receive() then simply calls withdraw(uint _amount) again.
        In this way we can reduce the balance to zero before 'balances[msg.sender] -= _amount' gets 
        executed.
        
        This level was designed to explain the re-entrancy attack that famously drained the Ethereum DAO, otherwise known colloquially as "The DAO Hack".





