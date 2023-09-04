# Ethernaut Level Solutions (using Brownie)

### Levels split into individual folders, under contracts...


- 03-Coin Flip
        -->     SOLVED

- 04-Telephone
        -->     SOLVED
                        Solution creates an instance of the Attack04 contract, passing the address of the target Telephone contract to its constructor. Then, when you call the attack function on the Attack04 contract, it triggers the changeOwner function on the Telephone contract and changes its ownership to the attacker's address. Demonstrating how you can use a proxy contract in order to exploit vulnerabilities in other smart contracts.

- 05-Token
        -->     SOLVED
                
                        Solution sets up an interface, in order to interact with the Token contract, then simply calls transfer - to a random address, for 21 tokens. This causes the 0.6.0 solidity code to underflow a uint256.  This balance then gets sent to msg.sender (in the original contract).

- 06-Delegation
        -->     #ToDo
                        ...


