"""
        Audit notes:

        1. Dex contract
            - storage slot 0, 1, 2 -> contain addresses

        2. SwappableToken contract
            - we can ignore this as the approve method is included
              in the Dex contract (for ease)

        3. Function swap() is where the token transfer happens

        Q. How is the price of the token calculated?
            - getSwapPrice() calculates the token price
            - ...
            - ...
        
        Q. How does the swap method work?
    
        Q. How do you approve a transaction of an ERC20?
    
        Q. What does "At Address" do?


        address to, address from, amount uint

        to.balanceOf(address(this))


    """
