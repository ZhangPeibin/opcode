# -*- coding: utf-8 -*-

import Code

class EVM :
    
    def __init__(self,code):
        self.code = code  #初始化字节码， bytes 对象
        self.pc = 0  #初始化程序计数器为0
        self.stack = [] #初始化堆栈
        self.memory = bytearray() #初始化内存
        self.storage = {}
        self.validJumDest = {} 
        self.findValidJumpDestinations()
    
    def findValidJumpDestinations(self):
        pc = 0 
        while pc < len(self.code):
            op = self.code[pc]
            if op == Code.JUMPDEST:
                self.validJumDest[pc] = True
            elif op >= Code.PUSH1 and op <= Code.PUSH32:
                pc += op- Code.PUSH1 +1
            
            pc+=1


    #获取下一个code指令
    def next_instruction(self):
        op = self.code[self.pc]
        self.pc += 1
        return op
    

    # push1 - push 32 
    def push(self,size):
        data = self.code[self.pc:self.pc+size]
        value = int.from_bytes(data,'big')
        self.stack.append(value)
        self.pc+=1

    def pop(self):
        if len(self.stack) == 0 :
            raise Exception("Stack underflow")

        return self.stack.pop()
    
    def add(self):
        if len(self.stack) < 2:
            raise Exception("Stack underflow")
        a = self.stack.pop()
        b = self.stack.pop()
        # 防止溢出
        res = ( a + b ) % (2**256) 
        self.stack.append(res)


    def mul(self):
        if len(self.stack) < 2:
            raise Exception("Stack underflow")
        
        a = self.stack.pop()
        b = self.stack.pop()
        
        res = (a * b ) % (2**256)
        self.stack.append(res)


    def sub(self):
        if len(self.stack) < 2:
            raise Exception("Stack underflow")
        a = self.stack.pop()
        b = self.stack.pop()
        res = (a - b ) % (2**256)
        self.stack.append(res)

    def div(self):
        if len(self.stack) < 2:
            raise Exception("Stack underflow")
        a = self.stack.pop()
        b = self.stack.pop()
        if b == 0 or b > a :
            self.stack.append(0)
        elif a == b:
            self.stack.append(1)
        else:
            res = a // b % (2 *256)
            self.stack.append(res)


    def sdiv(self):
        if len(self.stack) < 2 :
            raise Exception("Stack underflow")
        a = self.stack.pop()
        b = self.stack.pop()
        res = a // b % (2**256) if b!=0 else 0
        self.stack.append(res)


    def mode(self):
        if len(self.stack) < 2:
            raise Exception("Stack underflow")
        a = self.stack.pop()
        b = self.stack.pop()
        res = a % b if b!=0 else 0
        self.stack.append(res)


    def smode(self):
        if len(self.stack) < 2:
            raise Exception("Stack underflow")
        a = self.stack.pop()
        b = self.stack.pop()
        res = a % b  if b !=0 else 0
        self.stack.append(res)

    def addmode(self):
        if len(self.stack) < 3:
            raise Exception("Stack underflow")
        a = self.stack.pop()
        b = self.stack.pop()
        c = self.stack.pop()
        res = (a + b)  % c  if c!=0 else 0
        self.stack.append(res)

    def mulmode(self):
        if len(self.stack ) < 3:
            raise Exception("stack underflow")
        a = self.stack.pop()
        b = self.stack.pop()
        c = self.stack.pop()
        res = ( a * b ) % c if c !=0 else 0
        self.stack.append(res)

    def exp(self):
        if len(self.stack ) < 2:
            raise Exception("stack underflow")
        # 指数
        a = self.stack.pop()
        # 底数
        b = self.stack.pop()
        res = pow(a,b) %(2**256)
        self.stack.append(res)

    def signextend(self):
        if len(self.stack) < 2:
            raise Exception('Stack underflow')
        b = self.stack.pop()
        x = self.stack.pop()
        if b < 32: # 如果b>=32，则不需要扩展
            sign_bit = 1 << (8 * b - 1) # b 字节的最高位（符号位）对应的掩码值，将用来检测 x 的符号位是否为1
        x = x & ((1 << (8 * b)) - 1)  # 对 x 进行掩码操作，保留 x 的前 b+1 字节的值，其余字节全部置0
        if x & sign_bit:  # 检查 x 的符号位是否为1
            x = x | ~((1 << (8 * b)) - 1)  # 将 x 的剩余部分全部置1
        self.stack.append(x)

    def lt(self):
        if len(self.stack) < 2:
            raise Exception('Stack underflow')
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append(int(a<b))

    def gt(self):
        if len(self.stack) < 2:
            raise Exception('Stack underflow')
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append(int(a>b))

    def eq(self):
        if len(self.stack) < 2:
            raise Exception('Stack underflow')
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append(int(a==b))
    
    def slt(self):
        if len(self.stack) < 2:
            raise Exception('Stack underflow')
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append(int(a<b))

    def sgt(self):
        if len(self.stack) < 2:
            raise Exception('Stack underflow')
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append(int(a>b))

    def isZero(self):
        if len(self.stack) < 1:
            raise Exception('Stack underflow')
        a = self.stack.pop()
        self.stack.append(int(a == 0))
    
    def and_op(self):
        if len(self.stack) < 2:
            raise Exception('Stack underflow')
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append( a & b )
    
    def or_op(self):
        if len(self.stack) < 2:
            raise Exception('Stack underflow')
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append( a | b )

    def xor_op(self):
        if len(self.stack) < 2:
            raise Exception('Stack underflow')
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append( a ^ b )

    def not_op(self):
        if len(self.stack) < 1:
            raise Exception('Stack underflow')
        a = self.stack.pop()
        self.stack.append( ~a % (2**256))

    def shl_op(self):
        if len(self.stack) < 1:
            raise Exception("Stack underflow")

        a = self.stack.pop()
        b = self.stack.pop()

        self.stack.append( a << b % (2*256))
    
    def shr_op(self):
        if len(self.stack) < 2:
            raise Exception("Stack underflow")

        a = self.stack.pop()
        b = self.stack.pop()

        self.stack.append( a >> b % (2*256))

    def sha_op(self):
        if len(self.stack) < 2:
            raise Exception("Stack underflow")

        a = self.stack.pop()
        b = self.stack.pop()

        self.stack.append( a >> b % (2*256))

    def byte(self):
        if len(self.stack) < 2:
            raise Exception("Stack underflow")

        n = self.stack.pop()
        v = self.stack.pop()

        if n >= 32:
            res =  0
        else:
            res = ( v // pow(256,31-n)) % 0xFF

        self.stack.append(res)
    
    def pop(self):
        if len(self.stack) < 1:
            raise Exception("Stack underflow")
        self.stack.pop()
    
    # 从stack 弹出2个数据，第一个数据是偏移量，第二个数据是value
    # 将value存放在offset偏移量的位置
    def mstore(self):
        if len(self.stack) < 2 :
            raise Exception("Stack underflow")
        offset = self.stack.pop() #偏移字节
        value = self.stack.pop() #值

        if offset + 32 > 2**64-1:
            raise Exception("invalid memory: store empty")
        
        # offset是起点.mstore每次存都是32个字节,所以后面还要加上32个字节
        while len(self.memory) < (offset + 32):
            self.memory.append(0)
        v = value.to_bytes(32,'big')
        self.memory[offset:offset+32] = v
         

    def mstore8(self):
        if len(self.stack) < 2 :
            raise Exception("Stack underflow")
        offset = self.stack.pop() #偏移字节
        value = self.stack.pop() #值
        if (offset + 32 )> (2**64-1):
            raise Exception("invalid memory: store empty")
        
        while len(self.memory) < offset + 32:
            self.memory.append(0)


        self.memory[offset] = value & 0xFF
        
    def mload(self):
        if len(self.stack) < 1:
            raise Exception("Stack underflow")

        offset = self.stack.pop()

        while len(self.memory) < offset + 32:
            self.memory.append(0)
        value = int.from_bytes(self.memory[offset:offset+32],"big")
        self.stack.append(value)

    def msize(self):
        self.stack.append(len(self.memory))

    def sstore(self):
        if len(self.stack) < 2:
            raise Exception("Stack underflow")
        loc = self.stack.pop()
        val = self.stack.pop()
        self.storage[loc] = val
    
    def sload(self):
        if len(self.stack) < 1 :
            raise Exception("Stack underflow")
        loc = self.stack.pop()
        val = self.storage.get(loc,0)
        self.stack.append(val)

    def jump(self):
        if len(self.stack) < 1:
            raise Exception("Stack underflow")
        dest = self.stack.pop()
        if dest not in self.validJumDest:
            raise Exception("Invlid jump destination")
        else: self.pc = dest
    
    def jumpi(self):
        if len(self.stack ) < 2:
            raise Exception("stack underflow")
        pos = self.stack.pop()
        cond = self.stack.pop()

        if cond != 0:
            if pos not in self.validJumDest:
                raise Exception("Invalid jump destination")
            else: self.pc = pos

    #啥也不干的
    def jumpdest(self):
        pass 
        
    def run(self):
        while self.pc < len(self.code):
            op = self.next_instruction()  
            if Code.PUSH1 <= op <= Code.PUSH32:
                size = op - Code.PUSH1 +1
                self.push(size=size)
            elif op == Code.PUSH0:
                self.stack.append(0)
            elif op == Code.POP:
                self.pop()
            elif op == Code.STOP:
                print("Program has been stopped")
                break
            elif op == Code.ADD:
                self.add()
            elif op == Code.SUB:
                self.sub()
            elif op == Code.MUL:
                self.mul()
            elif op == Code.DIV:
                self.div()
            elif op == Code.SDIV:
                self.sdiv()
            elif op == Code.MOD:
                self.mode()
            elif op == Code.SMOD:
                self.smode()
            elif op == Code.ADDMOD:
                self.addmode()
            elif op == Code.MULMOD:
                self.mulmode()
            elif op == Code.EXP:
                self.exp()
            elif op == Code.SIGNEXTEND:
                self.signextend()    
            elif op == Code.LT:
                self.lt()
            elif op == Code.GT:
                self.gt()
            elif op == Code.SLT:
                self.slt()
            elif op == Code.SGT:
                self.sgt()
            elif op == Code.EQ:
                self.eq()
            elif op == Code.ISZERO:
                self.isZero()
            elif op == Code.AND:
                self.and_op()
            elif op == Code.OR:
                self.or_op()
            elif op == Code.XOR:
                self.xor_op()
            elif op == Code.NOT:
                self.not_op()
            elif op == Code.SHL:
                self.shl_op()
            elif op == Code.SHR:
                self.shr_op()
            elif op == Code.BYTE:
                self.byte()
            elif op == Code.SHA:
                self.sha_op()
            elif op == Code.POP:
                self.pop()
            elif op == Code.MSTORE:
                self.mstore()
            elif op == Code.MSTORE8:
                self.mstore8()
            elif op == Code.MLOAD:
                self.mload()
            elif op == Code.MSIZE:
                self.msize()
            elif op == Code.SLOAD:
                self.sload()
            elif op == Code.SSTORE:
                self.sstore()
            elif op == Code.JUMPDEST:
                self.jumpdest()
            elif op == Code.JUMP:
                self.jump()
            elif op == Code.JUMPI:
                self.jumpi()

            

# code = b'\x60\x02\x60\x01\x60\x01\x1b\x1b' # result is 8 
code = b'\x60\x02\x60\x20\x55\x60\x20\x54' 
evm = EVM(code=code)
evm.run()
print(evm.stack)
print(evm.storage)
