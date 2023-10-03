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


#            160  128  64   32   16

# mask = "0x---- ---- ---- ---- ----"


# -> PART-1
# uint32(gk) == uint16(gk)

# # mask = "0x---- ---- ---- 0000 ----"

# ->-> PART-2
# uint32(gk) != gk

# # mask = "0x---- ---- FFFF 0000 ----"


# ->->-> PART-3
# uint32(gk) == uint16(uint160(tx.orign))

# # mask = "0x---- ---- FFFF 0000 eE25"

# For bytes 13 to 20 we can simply pad with F:
# # mask = "0xFFFF FFFF FFFF 0000 eE25"
