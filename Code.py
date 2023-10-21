# -*- coding: utf-8 -*-

#-----------------算数指令-----------------
# 0x0 range - arithmetic ops.
STOP = 0X00
ADD = 0X01
MUL = 0X02
SUB = 0X03
DIV = 0X04
SDIV = 0X05
MOD = 0X06
SMOD = 0X07
ADDMOD=0X08
MULMOD = 0X09
EXP = 0X0A
SIGNEXTEND = 0X0B


#-----------------比较 位级指令-----------------
# 0x10 range - comparison ops.
LT = 0X10
GT = 0X11
SLT =0X12
SGT = 0X13
EQ = 0X14
ISZERO = 0x15

AND = 0X16
OR = 0X17
XOR = 0X18
NOT = 0X19
BYTE = 0X1A
SHL = 0X1B
SHR = 0X1C
SHA = 0X1D

#-----------------区块信息指令-----------------
# // 0x40 range - block operations.
BLOCKHASH = 0x40
COINBASE  = 0x41
TIMESTAMP = 0x42
NUMBER    = 0x43
DIFFICULTY   = 0x44
RANDOM    = 0x44 # Same as DIFFICULTY
PREVRANDAO   = 0x44 # Same as DIFFICULTY
GASLIMIT  = 0x45
CHAINID   = 0x46
SELFBALANCE  = 0x47
BASEFEE   = 0x48
BLOBHASH  = 0x49
BLOBBASEFEE  = 0x4a
 
#-----------------存储，执行 指令-----------------
# 0x50 range - 'storage' and execution
POP = 0X50
MLOAD = 0X51 
MSTORE = 0X52
MSTORE8 = 0X53
SLOAD= 0x54
SSTORE = 0x55
JUMP = 0x56
JUMPI = 0X57
PC = 0X58
MSIZE = 0x59
GAS = 0X5a
JUMPDEST = 0X5b
TLOAD = 0x5c
TSTORE = 0X5d
MCOPY = 0X5e

#-----------------PUSH 指令-----------------
PUSH0 = 0x5f
PUSH1 = 0X60
# .....省略 2-31
PUSH32 = 0x7f


POP = 0X50


