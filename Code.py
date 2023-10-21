# -*- coding: utf-8 -*-

#-----------------算数指令-----------------
# 0x0 range - arithmetic ops.
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

#-----------------存储，执行 指令-----------------
# 0x50 range - 'storage' and execution
POP = 0X50
MLOAD = 0X51 
MSTORE = 0X52
MSTORE8 = 0X53
SLOAD= 0x54
SSTORE = 0x55
MSIZE = 0x59


#-----------------PUSH 指令-----------------
PUSH0 = 0x5f
PUSH1 = 0X60
# .....省略 2-31
PUSH32 = 0x7f


POP = 0X50


