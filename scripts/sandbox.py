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
