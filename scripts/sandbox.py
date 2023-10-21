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


def swap(_balance_1, _balance_2, _amount):
    swap_amount = _amount * _balance_1 / _balance_2
    return swap_amount


def approve():
    pass


def main():

    token1_balance = 10
    token2_balance = 10
    amount = 10

    # xxx

    # toggle from
    # if from == token1:
    #     from = token2
    # else:
    #     from = token1

    while token1_balance != 0 and token2_balance != 0:
        pass
