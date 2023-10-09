#
# delegatecall explanation
#
# A calls B, sends 100 wei
#                then:  B deleagatecall C
#
# A  --->  B  --->  C
#                   msg.sender = A
#                   msg.value = 100 wei
#                   execute code on B's state variables
#                   use ETH in B
