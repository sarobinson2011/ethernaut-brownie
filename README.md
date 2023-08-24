# Ethernaut Level Solutions (using Brownie)

### Levels split into individual folders, under contracts...


- 03-Coin Flip
                -->     solved

- 04-Telephone
                -->     SOLVED
                                Solution creates an instance of the Attack04 contract, passing the address of the target Telephone contract to its constructor. Then, when you call the attack function on the Attack04 contract, it triggers the changeOwner function on the Telephone contract and changes its ownership to the attacker's address. Demonstrating how you can use a proxy contract in order to exploit vulnerabilities in other smart contracts.

- 05-Token
                -->     #ToDo



