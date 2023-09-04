from scripts.helpful_scripts import get_account
from brownie import interface, TokenInterface

# new instance of Level 05 - Token
ETHERNAUT_INSTANCE = "0x292597B71806e65B2c42b773055AAe6ed09bfC57"
PLAYER = "0xF8f8269488f73fab3935555FCDdD6035699deE25"
RANDOM_ADDRESS = "0x3826539Cbd8d68DCF119e80B994557B4278CeC9f"


def main():

    acc = get_account()
    token = interface.TokenInterface

    # call transfer: (_to = random address, _value = 21, from acc)
    tx = token.transfer(RANDOM_ADDRESS, 21, {"from": acc})
    tx.wait(1)

    # call balanceOf(PLAYER) - view function, so no state change
    print(f"New balance of PLAYER account = {token.balanceOf(PLAYER)}")
