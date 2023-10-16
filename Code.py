# -*- coding: utf-8 -*-


#-----------------堆栈指令-----------------
PUSH0 = 0x5f
PUSH1 = 0X60
# .....省略 2-31
PUSH32 = 0x7f


POP = 0X50

#-----------------算数指令-----------------

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
