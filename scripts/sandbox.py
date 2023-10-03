# bytes    uint
#   1       8
#   2       16
#   4       32
#   8       64
#   16      128
#   20      160   <-- Ethereum address length (bytes20 <-> uint160)
#   32      256

# TX_ORIGIN = "0xF8f8269488f73fab3935555FCDdD6035699deE25"

# uint64(_gateKey) = gk

# uint32(uint64(_gateKey)) == uint16(uint64(_gateKey))
# uint32(uint64(_gateKey)) != uint64(_gateKey)
# uint32(uint64(_gateKey)) == uint16(uint160(tx.origin))


# PART-1
# uint32(gk) == uint16(uint64(_gateKey)) == "0xeE25"
# # uint32('0xeE25') == "0x0000eE25"
# # uint32(gk) == "0x0000eE25"

# mask = "xxxxxxxx0000xxxx"

# PART-2
# uint32(uint64(_gateKey)) != uint64(_gateKey)
# # so:
# # "0x0000eE25"  != "xxxxxxxx0000eE25"
# # so x's cannot be zeros, but they CAN be ANYTHING else!

# mask = "FFFFFFFF0000FFFF"


# PART-3
# uint32(uint64(_gateKey)) == uint16(uint160(tx.orign))

# bits 0 to 16 (first 2 bytes) need to be same as tx.origin
# bits 16 to 32 need to be 0
