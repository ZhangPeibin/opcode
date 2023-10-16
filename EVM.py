class EVM :
    
    def __init__(self,code) -> None:
        self.code = code  #初始化字节码， bytes 对象
        self.pc = 0  #初始化程序计数器为0
        self.stack = [] #初始化堆栈

    