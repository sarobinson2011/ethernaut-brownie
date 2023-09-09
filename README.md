# Ethernaut Level Solutions (using Brownie)

### Levels split into individual folders, under contracts...


- 03-Coin Flip
        -->     SOLVED

- 04-Telephone
        -->     SOLVED
                
                        Solution creates an instance of the Attack04 contract.
                        Passes the Telephone contract to it's Constructor.
                        When you then call attack on the Attack04 contract, it triggers changeOwner.
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
        -->     #ToDo
                        Unlock the vault to pass the level


