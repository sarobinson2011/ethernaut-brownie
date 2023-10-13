""" 
                    *** Contract ABI specification ***

Application Binary Interface (ABI) - standard interface for contract interaction

- data is encoded, according to it's type

- assumes that
    
    1. interface functions are strongly typed, known at compilation time, and static.
    2. all contracts have the the interface definitions of other contracts they call.
    3. DOES NOT cover contracts whose interface is dynamic or known only at run-time. 


    Function Selector

    The first 4 bytes of the call data for a function call specifies the function to
    be called. In big endian notation, it is the first 4 bytes of the keccak-256 hash 
    of the signature of the function.  The 'signature' is the function name with the 
    parenthesised list of parameter types.  Paramter types are split by a single comma,
    with no spaces. The return type is NOT part of this signature.

    
    

"""
