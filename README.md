# Ethernaut Level Solutions (using Brownie)

### Levels split into individual folders, under contracts...

### A more detailed write-up is viewable at my blog 
### #DevDiary: https://highandhazardous.blogspot.com/


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

        The security flaw in the lies in the withdraw(uint _amount) function, that transfers funds BEFORE subtracting the transfer from the account balance. 
        After checking that the account has funds to withdraw, a low-level call  is made to msg.sender, to transfer the funds.
        
        I guess the code was written assuming calls from EOAs, but if the call is made from a proxy contract we can then include a receive() function, receive() then simply calls withdraw(uint _amount) again. In this way we can reduce the balance to zero before 'balances[msg.sender] -= _amount' gets executed.
        
        This level was designed to explain the re-entrancy attack that famously drained the Ethereum DAO, otherwise known colloquially as "The DAO Hack".

        The official Solidity Language docs (link below) advise to use the standard 'Checks-Effects-Interactions' pattern when writing solidity functions, as follows:

        1. First perform checks e.g. who called the function, did they send enough eth etc.
        2. Second perform updates to state variables 
        3. Third (and last) execute any interactions with other contracts (known or unknown)

- 11-Elevator
        -->
                SOLVED

        This problem was a little tricky to wrap my head around, until the penny finally dropped.
        In order to solve this level all you need to do is set the state variable top == true.
        The vulnerability in the code occurs in the function isLastFloor(uint), this function has
        a visibility modifer external, and no modifier to limit ability to alter state variables.
        Hence we can attack Elevator by writing malicious functionality into the isLastFloor()
        function in our Attack11 contract.
        The goTo(uint _floor) function makes a conditional check on the negated boolean return
        value from isLastFloor(). Thus by returning a negated bool from Attack11 we can force 
        top to equal true.
        To mitigate this vulnerability, the isLastFloor() function should have the 'view' function
        modifier.  This removes the ability to change state variables, thus you cannot win.

- 12-Privacy
        -->
                SOLVED

        The solution to this level lies in the fact that data is **never** actually 'private' on-chain.
        The challenge is simple - call unlock(_key) where the _key argument needs to equal the first
        16 bytes of the bytes32[2] state variable 'data'. Data has the visibility specifier 'private'.
        However, by using the web3.eth.get_storage_at() function, passing in the contract address, 
        and the specific slot you want to view, the function returns the hex data stored at that slot. 
        
        - Note: storage slot numbering starts at index 0.
        
        There are 6 state variables (2 uint8 in a row - which could be packed together) so the data
        variable will most likely be stored at slot 4 (if uint8's are packed) or slot 5 (if not packed).
        I first printed all 6 slots to the console, and by looking at the bytes returned it was obvious that the 2 uint8 variables are not packed together. So the data variable is stored at slot 5.
        From there I simply slice the data array and pass the first 16 bytes as the key to unlock().
        
        Et voilà... contract successfully unlocked.

        Lesson learned: private variables are only private for the smart contract scope, meaning they can't be accessed or modified from other smart contracts. However, their values **can** be read freely outside the blockchain, by anyone, so they don't actually 'hide' data in that sense.

- 13-Gatekeeper One
        -->
                SOLVED

        Gatekeeper One is the first '4 star' difficulty level, and to be honest looks scary to start with.  The challenge is simple to explain - simply call enter(bytes8_gateKey) , where the value of _gateKey must satisfy 3 separate function modifiers, namely gateOne, gateTwo, and gateThree.  If all 3 are satisfied the function returns true and we achieve entry:
        
        **Gate one:** 
        
        This is simple to beat, we need to call enter() from a proxy contract, such that:
        - msg.sender (attack contract address) != tx.origin (player address)
 
        **Gate Two:**

        Gate two requires that the gas remaining i.e. gasleft() at this stage of the contract execution, is an integer multiple of 8191.
        You *could* do this via the Remix debugger, adding up the gas for each individual op code.
        But, the easier way of achieving this is via a brute for attack, in the form of a for loop.
        Full explanation of this approach is available as comments in the blog link / GitHub repository (see top of page).        

        **Gate Three:**

        Gate three is a 3-part conditional expression, that is reasonably easy to solve using a 
        bit mask patter, which is compared with the mask via a logical bit-wise AND '&' operation.
        
        Where:
                mask = "FFFF FFFF FFFF 0000 FFFF"
        giving:
                gateKey = "CDdD60350000eE25"

        Full explanation of this approach is available as comments in the blog link / GitHub repository (see top of page).

- 14-Gatekeeper Two
        -->
                SOLVED

        Gatekeeper Two is essentially level 2 of the Gatekeeper challenge. The premise is the same, call enter(), passing all gate modifiers,with the correct gateKey to win.
        As per Gatekeeper One, if all 3 are satisfied the function returns true and we achieve entry:

        **Gate One:** 
        
        This is simple to beat, we need to call enter() from a proxy contract, such that:
        - msg.sender (attack contract address) != tx.origin (player address)
 
        **Gate Two:**

        Gate Two requires that the 'codesize' (in bytes) of the code at the call address
        be equal to zero. Typically an EOA has zero code size, whereas contracts have non-zero
        code size. This is in direct opposition to Gate One requirement.
        The solution to Gate One and Gate Two is to make a low-level call is from the constructor of the attack contract - whilst a contract is initialised, via the constructor, it hasn't been fully deployed yet, thus having a code size = zero.

        **Gate Three:**

        Gate Three is similar to the GateKeeper-One third gate - this time it's a conditional
        comparison between the msg.sender address XOR'd with 64 bits of value '1'.
        I initially tried to calculate this value outside of the smart contract, using Python.
        Whilst the calculation is simple enough, I quickly realised that this is not possible since the value of msg.sender is the attack contract address - which is unknown until the contract is actually deployed - at which point we would now fail Gate Two.

        The solution is to simply re-arrange the expression, and deploy directly from the constructor, using address(this) as msg.sender, as follows:

        uint64 gateKey = uint64(bytes8(keccak256(abi.encodePacked(address(this)))));
        gateKey = gateKey ^ type(uint64).max;

        Level complete!

        Full explanation of this approach is available as comments in the blog link / GitHub repository (see top of page).

- 15-Naught Coin
        -->
                SOLVED

        The key lesson to learn from this level is that when a contract inherits from another contract, ensure that you are familiar with BOTH.  The lockTokens() modifier becomes irrelevant once you realise there is more than one method of transferring tokens from a contract, that inherits from ERC20.

        The transfer() function is subject to the lockTokens() modifier, which isn't hackable.  However, the ERC20 standard defines a second function for transferring tokens, the transferFrom() function.  Critically this function is not subject to the lockTokens() modifier, thus we are able to deploy a proxy (attack) contract which (once the Naught Coin token-contract is approved) utilises the transferFrom() to empty the Naught Coin contract.
        
- 16-Preservation
        -->
                SOLVED

        The goal of this level is simple, gain ownership of the Preservation contract instance.  In order to beat this level a thorough understanding of delegateCall() is required, specifically delegation to libraries.

        The vulnerability lies in the setTime() function:

                function setTime(uint _time) public {
                        storedTime = _time;
                }

        The LibraryContract contract has it's own state, thus we can deploy an attack contract,
        that contains:

                - identical state variables (same order) that we want, as per the target
                - a setTime(uint) function
        
        First we call setFirstTime, to set timeZone1Library to address(this), of our Attack16 contract.  We then make a second call to setFirstTime, which this time runs our malicious setTime() function with msg.sender (Attack16) as the argument. Our setTime() function then updates owner = msg.sender
        
        It is the setTime(uint) function can them be used to take ownership of the target contract, due to the library contract having it's own state.  This in combination with the delegatecall() means we can update the public state variables in the target contract.

             function setTime(uint256 _owner) external {
                owner = address(uint160(_owner));
             }  

        Calling owner() on the contract instance, from Ethernaut now returns our player address.

        This example demonstrates why the 'library' keyword should be used for building libraries, as it prevents the libraries from storing and accessing state variables.

        Level complete!

- 17-Recovery
        -->
                SOLVED

        The main lesson to learn with this level is how ethererum contract addresses are calculated deterministically, and how we can use this fact to retreive a lost contract address, in certain circumstances.

        Two methods to determine a smart contract address:


        **1st method:**

        - calculate it using the address of either the EOA or contract that created it, plus the nonce for the transaction, so (from the Ethereum yellow paper):

                address = rightmost_20_bytes(keccak(RLP(sender_address, nonce)))

        Where RLP stands for 'Recursive Length Prefix', which is the encoding method used to serialise objects in Ethereum's execution layer.

        Note: the nonce value must be correct otherwise the output will be wrong.


        **2nd method:**

        We can also simply look the missing contract address up, on Etherscan, by viewiwing the ETHERNAUT_INSTANCE contract address, and looking at the internal transactions tab - which shows 2 internal transactions relating to 'Contract Creation' for the Recovery contract (nonce 0), and Contract Creation for the SimpleToken contract (nonce 1).

        A simple comparison between the output from both methods shows that they both yield the correct answer for the SimpleToken contract address.

        Once we have the SimpleToken contract address, we simply call destroy() passing in our player address.

        Level complete!

- 18-MagicNumber
        -->
                ToDo

        This challenge ...