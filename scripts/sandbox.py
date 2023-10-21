"""
        Audit notes:

        1. Dex contract
            - storage slot 0, 1, 2 -> contain addresses
        2. SwappableToken contract
            - we can ignore this as the approve method is included
              in the Dex contract (for ease)
        3. Function swap() is where the token transfer happens
       
        4. Swap price calculation
        
            - (amount * 'to' price) / ('from' price)
                so: swap price == amount * (token ratio)
    
        5. Swap process ->

            - xyz
                - abc

                
        Q. How do you approve a transaction of an ERC20?
            
            - approve the contract to spend your tokens

    """

# we want a swap_amount > 100


def main():

    TOKEN1_AMOUNT = 10
    TOKEN2_AMOUNT = 10
    AMOUNT = 10

    swap_amount = AMOUNT * TOKEN1_AMOUNT / TOKEN2_AMOUNT

    print(f"\nSwap amount = {swap_amount}\n")


# toggle from
# if from == token1:
#     from = token2
# else:
#     from = token1
