#
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
