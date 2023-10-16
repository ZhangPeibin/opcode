# -*- coding: utf-8 -*-

import Code

class EVM :
    
    def __init__(self,code):
        self.code = code  #初始化字节码， bytes 对象
        self.pc = 0  #初始化程序计数器为0
        self.stack = [] #初始化堆栈

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
            res = a // b 
            self.stack.append(res)


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
            elif op == Code.ADD:
                self.add()
            elif op == Code.SUB:
                self.sub()
            elif op == Code.MUL:
                self.mul()
            elif op == Code.DIV:
                self.div()

                                   

# code = b'\x60\x01\x5F\x50\x50'
# code = b'\x60\x03\x60\x06\x01'
code = b'\x60\x03\x60\x06\x03'
evm = EVM(code=code)
evm.run()

print(evm.stack)



