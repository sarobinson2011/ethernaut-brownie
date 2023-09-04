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
        -->     #ToDo
                        ...


