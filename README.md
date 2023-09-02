# Ethernaut Level Solutions (using Brownie)

### Levels split into individual folders, under contracts...


- 03-Coin Flip
                -->     SOLVED

- 04-Telephone
                -->     SOLVED
                                Solution creates an instance of the Attack04 contract, passing the address of the target Telephone contract to its constructor. Then, when you call the attack function on the Attack04 contract, it triggers the changeOwner function on the Telephone contract and changes its ownership to the attacker's address. Demonstrating how you can use a proxy contract in order to exploit vulnerabilities in other smart contracts.

- 05-Token
                -->     #ToDo - in Brownie
                
                                Steps:
                                --> check 'await contract.balanceOf(player)' == 20 (in browser)
                                --> call transfer(_to, _value) as follows:
                                    --> contract.transfer('another address', 20 + 1)
                                --> check that call 'await contract.balanceOf(player)' == LOTS!



