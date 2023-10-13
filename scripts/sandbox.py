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

    Argument Encoding

    The fifth byte onwards contain the encoded arguments.  This encoding is also used 
    in other places e.g. the return values and also event arguments are encoded in the
    same way, without the four bytes specifying the function.

    Types
    
    https://docs.soliditylang.org/en/v0.8.21/abi-spec.html#types

    
    Mapping Solidity to ABI types

    Solidity supports all types listed in the link above (other than tuples).  Also some
    Solidity types are not supported by the ABI.  The following mappings show Solidity
    types that are not part of the ABI <--> the ABI types they map to:

        Solidity            |    ABI
        --------------------|------------------------------
        address payable     |    address
        contract            |    address
        enum                |    uint8
        struct              |    tuple
                            |                    
        user defined types  |    it's underlying value type          
        ----------------------------------------------------
    
        
    Encoding Specification 

    https://docs.soliditylang.org/en/v0.8.21/abi-spec.html#design-criteria-for-the-encoding

"""
