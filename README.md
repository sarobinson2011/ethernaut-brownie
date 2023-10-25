# Ethernaut Level Solutions (using Brownie)

### Levels split into individual folders, under contracts...

### A more detailed write-up is viewable at my blog: 
##### https://highandhazardous.blogspot.com/ (#DevDiary)


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
                SOLVED

        This challenge involves building a short contract, directly using no more than 10 EVM opcodes.  In other words, we are going to need to write some assembly code.

        I initially wrote a simple contract, using no assembly, that simply returns 42 (2a):

        contract Attack18 {
                function attack() external pure returns (uint) {
                        return 42;
                }
        }

        I deployed this contract using Remix and used the debugger to observe the opcodes used per operation (and corresponding the stack values).  The number of opcodes used well exceeded the 10 opcode limit prescribed by the challenge.

        Having done some research, I found the following example code here:

                https://solidity-by-example.org/app/simple-bytecode-contract/
        
        contract Factory {
                event Log(address addr);

                // Deploys a contract that always returns 42
                function deploy() external {
                        bytes memory bytecode = hex"69602a60005260206000f3600052600a6016f3";
                        address addr;
                        assembly {
                        // create(value, offset, size)
                        addr := create(0, add(bytecode, 0x20), 0x13)
                        }
                        require(addr != address(0));

                        emit Log(addr);
                }
        }

        My solution was to use the above code in order to create a smart contract, using bytecodes, that returns value 42-base10 (2a-base16). 

        This code I deployed in the constructor of my Attack18 contract, since (until the contract is deployed) code executed from a constructor has extcodesize = 0.

        This level was tricky in that the solution requires a good level of understanding of how the EVM operates, specifically the low-level operations.

        Level complete!

- 19-Alien Codex
        
        -->
                SOLVED

        This challenge is simple to explain - take ownership of AlienCodex to win!

        I initially attempted to find a potential vulnerability in Ownable-05.sol, thinking there could be a way to exploit it.  This proved unsuccessful, the Ownable contract is tight.

        The key to beating the level lies in how array storage works in Ethereum.

        Alien Codex has 2 storage (state) variables: 

        - bool public contact;      <--  1 byte of a 32 byte storage slot
        - bytes32[] public codex;   <--  a whole 32 byte storage slot, per entry

        The AlienCodex contract inherits from the Ownable contract, therefore the state
        varibables declared in Ownable are also stored in the AlienCodex storage. 
        So Ownable has one storage variable:

        - address private _owner;   <--  20 bytes of a whole 32 byte storage slot 

        This is also stored in the AlienCodex storage, along with contact and codex.

        In Solidity, when contract #1 inherits from contract #2, the inherited state variables (from the contract two) are stored at the beginning of contract #1, occupying storage slots from 0 onward. Contract #1's own state variables are stored after the inherited state variables.

        If the variable type is dynamic e.g. dynamic array, mapping, then the values are stored at addresses based on the keccak hash of the slot:

        - keccak256(slot#) + (index * elementSize)  -->  for arrays
        - keccak256(key, slot#)                     -->  for mappings

        So in order to attack this level and win, the following steps are needed:

        # Process
     
        1. check (call) owner
        2. call makeContact()
        3. call retract()
    
    
        Note_1: calling retract() on the empty codex[] array causes
                an underflow:  codex[] --> codex[2^256-1]
                which effectively gives us write access to all of the storage
                slots in the AlienCodex contract.
    
        Note_2: the retract function breaks the "Checks, Effects, Interactions" rule


        4. calculate position 'i'  --> arguement passed to revise()
        5. call revise(i, player_address)
        6. check (call) owner
    
                the starting position of the codex[] array element 'i' is:
    
                i = keccak256(1)    <--  since codex starts at slot 1
        
                slot i            - codex[0]
                slot i+1          - codex[1]
                slot i+2          - codex[2]
                slot i+3          - codex[3]
                ................................
                ................................
                slot i+(2^256)-1  - codex[(2^256)-1]
        
                the one unknown in the process is now the value of 'i' (uint256)

        First element of our array (which is storage slot 1) should be located at:
                
        -->     first_position = convert.to_uint(keccak(convert.to_bytes(1)))
        
        2 ** 256 max storage pointer for the dynamic array
        
        -->     zero_position = 2**256 - first_position

        Finally, we call:

        -->     target.revise(zero_position, player.address, {"from": player})

        
        Level complete!


        This level exploits the fact that the EVM doesn't validate an array's ABI-encoded length vs its actual payload.

        It aLso exploits the arithmetic underflow of array length, by expanding the array's bounds to the entire storage area of 2^256. The user is then able to modify all contract storage.

- 20-Denial
        
        -->
                SOLVED

        This level presents us with a contract called Denial, that has a constant public address storage variable, called owner:

        - address public constant owner = address(0xA9E);
    
        If you can deny the owner from withdrawing funds when they call 
        withdraw(), whilst the contract still has funds, and the transaction is of 1M gas or less... you will win this level.

        Note 1:
        The transaction limit of 1M gas or less" means we can't do anything gas intensive.

        Note 2:
        A re-entrancy attack won't work since the the withdraw amount is 1% of the current contract balance.  This means that you'd need infinite withdraws to get to zero:

        - uint amountToSend = address(this).balance / 100;

        Once becoming the partner by calling setWithdrawPartner() with the address
        of my attack contract, from within the constructor, the contract is able to exploit the use of the message call, from Denial.

        The withdraw() function does not follow the 'checks-effects-interactions' 
        pattern (in order to avoid reentrancy attacks), this is where the
        vulnerability lie, specifically in the message call. 

        The receive payable fallback is trigged when the call is made with the 
        incoming ether, inside the receive() function we use a low level assembly
        function called invalid().  This triggers an "invalid instruction" exception to be thrown, and cause the current transaction to revert.
        When this happens the "gas limit" is completely used up.  The Denial
        contract uses the message call without specifiying a gas limit, thus the 
        effective gas limit is maximum - which uses up all the gas, meaning the 
        owner never gets any withdawls.  We win!

        Mitigation against this vulnerability:

        use the call boolean result to confirm a successful transaction:
        
        - (bool result, ) = partner.call{value:amountToSend}("");
        - require(result);

        this would have cause my attack to fail on revert.

        Level complete!

- 21-Shop
        
        -->
                SOLVED

        This challenge is similar to level 11 'Elevator', which taught us to not trust the
        logic of external contracts.

        Since the Shop expects to be called from a Buyer:

        interface Buyer {
                function price() external view returns (uint);
        }       
        
        We can deploy an attack contract that contains the price() function, returning a 
        uint value.  The price() function is modified as 'view' so we can't change any 
        state variables, but we can employ conditional logic to vary our return value.

        The attack is fairly simple, we have to exploit this code, to buy for < 100 :

        if (_buyer.price() >= price && !isSold) {
                isSold = true;
                price = _buyer.price();
        }
        
        By writing our own attack code within the price() function, as follows:

        function price() external view returns (uint){
                if (target.isSold()) {
                // second iteration - we win!
                return 0;
                } 
                // first iteration
                return 100;
        }

        we can buy the item for 0 (or any uint value < 100). The attack is in 2 stages:

        1a. call attack() first time
        1b. at this stage isSold == false
        1c. price() returns 100
        1d. isSold == true, _buyer.price() is updated to == 100

        2a. call attack() second time
        2b. at this stage isSold == true, _buyer.price() == 100
        2c. now --> _buyer.price() returns 0
        2d. price is still == 100, so...
        2e. isSold() is still == true
        2f. price is updated to == 0

        Hence on the 2nd iteration of our attack we are able to pay a price of 0.

        Note: As with level 11 'Elevator', this challenge teaches us that:

        1. Contracts can manipulate data seen by other contracts in any way they want.
        2. It's unsafe to change the state based on external & untrusted contracts logic.

        Level complete!

- 22-Dex
        
        -->
                SOLVED

        The goal of this level is to steal all of one of 2 different tokens, balance of
        each is 100 to start, whilst the player balance of each token is 10 of each token.

        The method of theft needs to be price manipulation, and we beat the level if we 
        manage to drain all of at least 1 of the 2 tokens, thus allowing the contract to 
        report a bad price.

        At first glance this contract was a little intimidating, but upon closer inspection
        the picture was fairly simple.  
        
        The price calculation for the swap is a *single-source*, *integer* calculation, this in 
        combination with the low liquidity in the Dex contract means we can easily manipulate
        the swap price (and hence the number of tokens received) by swapping back and forth.

        Solidity does not support floating point numbers, hence integer division can cause 
        rounding errors.

        By evaluating the getSwapPrice() function in the Dex contract, it becomes obvious that 
        we can manipulate the swap price calculation in order to unbalance the pool, and in 
        turn drain the funds.

        Essentially, what we need to do is start swapping backwards and forwards between the 2 
        tokens.  Since the swap price calculation is inefficient we can drain all funds from a
        pool in this way.

        In  order to beat the challenge I first attempted a smart contract attack solution, but 
        soon realised I could do it with Python (Brownie) alone.

        See 22-simulate_dex.py and 22-deploy_attack for details.

        Here's the Ethernaut 'level complete' spiel:

        "The integer math portion aside, getting prices or any sort of data from any single source is a massive attack vector in smart contracts.
        
        You can clearly see from this example, that someone with a lot of capital could manipulate the price in one fell swoop, and cause any applications relying on it to use the the wrong price.
        
        The exchange itself is decentralized, but the price of the asset is centralized, since it comes from 1 dex. This is why we need oracles. Oracles are ways to get data into and out of smart contracts. We should be getting our data from multiple independent decentralized sources, otherwise we can run this risk."

        Level complete!

- 23-Dex Two
        
        -->
                ToDo

        ....      


        