import unittest

from EVM import EVM


class TestStringMethods(unittest.TestCase):
    def testAdd(self):
        code = b'\x60\x02\x60\x04\x01'
        evm = EVM(code=code)
        evm.run()
        self.assertEqual(evm.stack[0],6)
    
    def testMul(self):
        code = b'\x60\x02\x60\x04\x02'
        evm = EVM(code=code)
        evm.run()
        self.assertEqual(evm.stack[0],8)

    def testSub(self):
        code = b'\x60\x02\x60\x04\x03'
        evm = EVM(code=code)
        evm.run()
        self.assertEqual(evm.stack[0],2)
        
    def testDiv(self):
        code = b'\x60\x03\x60\x04\x04'
        evm = EVM(code=code)
        evm.run()
        self.assertEqual(evm.stack[0],1)
    
    def testMod(self):
        code = b'\x60\x03\x60\x04\x06'
        evm = EVM(code=code)
        evm.run()
        self.assertEqual(evm.stack[0],1)

if __name__ == '__main__':
    unittest.main()


