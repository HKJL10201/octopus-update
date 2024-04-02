# based on Manticore project: https://github.com/trailofbits/manticore
# extract from http://gavwood.com/paper.pdf

_table = {
    # opcode:(mnemonic, immediate_operand_size, pops, pushes, gas, description)
    0x00: ('STOP', 0, 0, 0, 0, 'Halts execution.'),
    0x01: ('ADD', 0, 2, 1, 3, 'Addition operation.'),
    0x02: ('MUL', 0, 2, 1, 5, 'Multiplication operation.'),
    0x03: ('SUB', 0, 2, 1, 3, 'Subtraction operation.'),
    0x04: ('DIV', 0, 2, 1, 5, 'Integer division operation.'),
    0x05: ('SDIV', 0, 2, 1, 5, 'Signed integer division operation (truncated).'),
    0x06: ('MOD', 0, 2, 1, 5, 'Modulo remainder operation.'),
    0x07: ('SMOD', 0, 2, 1, 5, 'Signed modulo remainder operation.'),
    0x08: ('ADDMOD', 0, 3, 1, 8, 'Modulo addition operation.'),
    0x09: ('MULMOD', 0, 3, 1, 8, 'Modulo multiplication operation.'),
    0x0a: ('EXP', 0, 2, 1, 10, 'Exponential operation.'),
    0x0b: ('SIGNEXTEND', 0, 2, 1, 5, "Extend length of two's complement signed integer."),
    0x10: ('LT', 0, 2, 1, 3, 'Less-than comparision.'),
    0x11: ('GT', 0, 2, 1, 3, 'Greater-than comparision.'),
    0x12: ('SLT', 0, 2, 1, 3, 'Signed less-than comparision.'),
    0x13: ('SGT', 0, 2, 1, 3, 'Signed greater-than comparision.'),
    0x14: ('EQ', 0, 2, 1, 3, 'Equality comparision.'),
    0x15: ('ISZERO', 0, 1, 1, 3, 'Simple not operator.'),
    0x16: ('AND', 0, 2, 1, 3, 'Bitwise AND operation.'),
    0x17: ('OR', 0, 2, 1, 3, 'Bitwise OR operation.'),
    0x18: ('XOR', 0, 2, 1, 3, 'Bitwise XOR operation.'),
    0x19: ('NOT', 0, 1, 1, 3, 'Bitwise NOT operation.'),
    0x1a: ('BYTE', 0, 2, 1, 3, 'Retrieve single byte from word.'),
    0x1b: ('SHL', 0, 2, 1, 3, 'Left shift operation'), # new
    0x1c: ('SHR', 0, 2, 1, 3, 'Logical right shift operation'), # new
    0x1d: ('SAR', 0, 2, 1, 3, 'Arithmetic (signed) right shift operation'), # new
    0x20: ('SHA3', 0, 2, 1, 30, 'Compute Keccak-256 hash.'),  # SHA3
    0x30: ('ADDRESS', 0, 0, 1, 2, 'Get address of currently executing account.'),
    0x31: ('BALANCE', 0, 1, 1, 20, 'Get balance of the given account.'),
    0x32: ('ORIGIN', 0, 0, 1, 2, 'Get execution origination address.'),
    0x33: ('CALLER', 0, 0, 1, 2, 'Get caller address.'),
    0x34: ('CALLVALUE', 0, 0, 1, 2, 'Get deposited value by the instruction/transaction responsible for this execution.'),
    0x35: ('CALLDATALOAD', 0, 1, 1, 3, 'Get input data of current environment.'),
    0x36: ('CALLDATASIZE', 0, 0, 1, 2, 'Get size of input data in current environment.'),
    0x37: ('CALLDATACOPY', 0, 3, 0, 3, 'Copy input data in current environment to memory.'),
    0x38: ('CODESIZE', 0, 0, 1, 2, 'Get size of code running in current environment.'),
    0x39: ('CODECOPY', 0, 3, 0, 3, 'Copy code running in current environment to memory.'),
    0x3a: ('GASPRICE', 0, 0, 1, 2, 'Get price of gas in current environment.'),
    0x3b: ('EXTCODESIZE', 0, 1, 1, 20, "Get size of an account's code."),
    0x3c: ('EXTCODECOPY', 0, 4, 0, 20, "Copy an account's code to memory."),
    0x3d: ('RETURNDATASIZE', 0, 0, 1, 2, "get size of return data buffer"),
    0x3e: ('RETURNDATACOPY', 0, 3, 0, 3, "copy return data in current environment to memory"),
    0x3f: ('EXTCODEHASH', 0, 1, 1, 100, "Get hash of an account's code"), # new
    0x40: ('BLOCKHASH', 0, 1, 1, 20, 'Get the hash of one of the 256 most recent complete blocks.'),
    0x41: ('COINBASE', 0, 0, 1, 2, "Get the block's beneficiary address."),
    0x42: ('TIMESTAMP', 0, 0, 1, 2, "Get the block's timestamp."),
    0x43: ('NUMBER', 0, 0, 1, 2, "Get the block's number."),
    0x44: ('DIFFICULTY', 0, 0, 1, 2, "Get the block's difficulty."),
    0x45: ('GASLIMIT', 0, 0, 1, 2, "Get the block's gas limit."),
    0x46: ('CHAINID', 0, 0, 1, 2, "Get the chain ID"), # new
    0x47: ('SELFBALANCE', 0, 0, 1, 5, "Get balance of currently executing account"), # new
    0x48: ('BASEFEE', 0, 0, 1, 2, "Get the base fee"), # new
    0x49: ('BLOBHASH', 0, 1, 1, 3, "Get versioned hashes"), # new
    0x4a: ('BLOBBASEFEE', 0, 0, 1, 2, "Returns the value of the blob base-fee of the current block"), # new
    0x50: ('POP', 0, 1, 0, 2, 'Remove item from stack.'),
    0x51: ('MLOAD', 0, 1, 1, 3, 'Load word from memory.'),
    0x52: ('MSTORE', 0, 2, 0, 3, 'Save word to memory.'),
    0x53: ('MSTORE8', 0, 2, 0, 3, 'Save byte to memory.'),
    0x54: ('SLOAD', 0, 1, 1, 50, 'Load word from storage.'),
    0x55: ('SSTORE', 0, 2, 0, 0, 'Save word to storage.'),
    0x56: ('JUMP', 0, 1, 0, 8, 'Alter the program counter.'),
    0x57: ('JUMPI', 0, 2, 0, 10, 'Conditionally alter the program counter.'),
    0x58: ('PC', 0, 0, 1, 2, 'Get the value of the program counter prior to the increment.'), # update name to match emulator.py
    0x59: ('MSIZE', 0, 0, 1, 2, 'Get the size of active memory in bytes.'),
    0x5a: ('GAS', 0, 0, 1, 2, 'Get the amount of available gas, including the corresponding reduction the amount of available gas.'),
    0x5b: ('JUMPDEST', 0, 0, 0, 1, 'Mark a valid destination for jumps.'),
    0x5c: ('TLOAD', 0, 1, 1, 100, 'Load word from transient storage'), # new
    0x5d: ('TSTORE', 0, 2, 0, 100, 'Save word to transient storage'), # new
    0x5e: ('MCOPY', 0, 3, 0, 3, 'Copy memory areas'), # new
    0x5f: ('PUSH0', 0, 0, 1, 2, 'Place value 0 on stack'), # new
    0x60: ('PUSH1', 1, 0, 1, 3, 'Place 1 byte item on stack.'), # update gas
    0x61: ('PUSH2', 2, 0, 1, 3, 'Place 2-byte item on stack.'), # update gas
    0x62: ('PUSH3', 3, 0, 1, 3, 'Place 3-byte item on stack.'), # update gas
    0x63: ('PUSH4', 4, 0, 1, 3, 'Place 4-byte item on stack.'), # update gas
    0x64: ('PUSH5', 5, 0, 1, 3, 'Place 5-byte item on stack.'), # update gas
    0x65: ('PUSH6', 6, 0, 1, 3, 'Place 6-byte item on stack.'), # update gas
    0x66: ('PUSH7', 7, 0, 1, 3, 'Place 7-byte item on stack.'), # update gas
    0x67: ('PUSH8', 8, 0, 1, 3, 'Place 8-byte item on stack.'), # update gas
    0x68: ('PUSH9', 9, 0, 1, 3, 'Place 9-byte item on stack.'), # update gas
    0x69: ('PUSH10', 10, 0, 1, 3, 'Place 10-byte item on stack.'), # update gas
    0x6a: ('PUSH11', 11, 0, 1, 3, 'Place 11-byte item on stack.'), # update gas
    0x6b: ('PUSH12', 12, 0, 1, 3, 'Place 12-byte item on stack.'), # update gas
    0x6c: ('PUSH13', 13, 0, 1, 3, 'Place 13-byte item on stack.'), # update gas
    0x6d: ('PUSH14', 14, 0, 1, 3, 'Place 14-byte item on stack.'), # update gas
    0x6e: ('PUSH15', 15, 0, 1, 3, 'Place 15-byte item on stack.'), # update gas
    0x6f: ('PUSH16', 16, 0, 1, 3, 'Place 16-byte item on stack.'), # update gas
    0x70: ('PUSH17', 17, 0, 1, 3, 'Place 17-byte item on stack.'), # update gas
    0x71: ('PUSH18', 18, 0, 1, 3, 'Place 18-byte item on stack.'), # update gas
    0x72: ('PUSH19', 19, 0, 1, 3, 'Place 19-byte item on stack.'), # update gas
    0x73: ('PUSH20', 20, 0, 1, 3, 'Place 20-byte item on stack.'), # update gas
    0x74: ('PUSH21', 21, 0, 1, 3, 'Place 21-byte item on stack.'), # update gas
    0x75: ('PUSH22', 22, 0, 1, 3, 'Place 22-byte item on stack.'), # update gas
    0x76: ('PUSH23', 23, 0, 1, 3, 'Place 23-byte item on stack.'), # update gas
    0x77: ('PUSH24', 24, 0, 1, 3, 'Place 24-byte item on stack.'), # update gas
    0x78: ('PUSH25', 25, 0, 1, 3, 'Place 25-byte item on stack.'), # update gas
    0x79: ('PUSH26', 26, 0, 1, 3, 'Place 26-byte item on stack.'), # update gas
    0x7a: ('PUSH27', 27, 0, 1, 3, 'Place 27-byte item on stack.'), # update gas
    0x7b: ('PUSH28', 28, 0, 1, 3, 'Place 28-byte item on stack.'), # update gas
    0x7c: ('PUSH29', 29, 0, 1, 3, 'Place 29-byte item on stack.'), # update gas
    0x7d: ('PUSH30', 30, 0, 1, 3, 'Place 30-byte item on stack.'), # update gas
    0x7e: ('PUSH31', 31, 0, 1, 3, 'Place 31-byte item on stack.'), # update gas
    0x7f: ('PUSH32', 32, 0, 1, 3, 'Place 32-byte (full word) item on stack.'), # update gas
    0x80: ('DUP1', 0, 1, 2, 3, 'Duplicate 1st stack item.'),
    0x81: ('DUP2', 0, 2, 3, 3, 'Duplicate 2nd stack item.'),
    0x82: ('DUP3', 0, 3, 4, 3, 'Duplicate 3rd stack item.'),
    0x83: ('DUP4', 0, 4, 5, 3, 'Duplicate 4th stack item.'),
    0x84: ('DUP5', 0, 5, 6, 3, 'Duplicate 5th stack item.'),
    0x85: ('DUP6', 0, 6, 7, 3, 'Duplicate 6th stack item.'),
    0x86: ('DUP7', 0, 7, 8, 3, 'Duplicate 7th stack item.'),
    0x87: ('DUP8', 0, 8, 9, 3, 'Duplicate 8th stack item.'),
    0x88: ('DUP9', 0, 9, 10, 3, 'Duplicate 9th stack item.'),
    0x89: ('DUP10', 0, 10, 11, 3, 'Duplicate 10th stack item.'),
    0x8a: ('DUP11', 0, 11, 12, 3, 'Duplicate 11th stack item.'),
    0x8b: ('DUP12', 0, 12, 13, 3, 'Duplicate 12th stack item.'),
    0x8c: ('DUP13', 0, 13, 14, 3, 'Duplicate 13th stack item.'),
    0x8d: ('DUP14', 0, 14, 15, 3, 'Duplicate 14th stack item.'),
    0x8e: ('DUP15', 0, 15, 16, 3, 'Duplicate 15th stack item.'),
    0x8f: ('DUP16', 0, 16, 17, 3, 'Duplicate 16th stack item.'),
    0x90: ('SWAP1', 0, 2, 2, 3, 'Exchange 1st and 2nd stack items.'),
    0x91: ('SWAP2', 0, 3, 3, 3, 'Exchange 1st and 3rd stack items.'),
    0x92: ('SWAP3', 0, 4, 4, 3, 'Exchange 1st and 4th stack items.'),
    0x93: ('SWAP4', 0, 5, 5, 3, 'Exchange 1st and 5th stack items.'),
    0x94: ('SWAP5', 0, 6, 6, 3, 'Exchange 1st and 6th stack items.'),
    0x95: ('SWAP6', 0, 7, 7, 3, 'Exchange 1st and 7th stack items.'),
    0x96: ('SWAP7', 0, 8, 8, 3, 'Exchange 1st and 8th stack items.'),
    0x97: ('SWAP8', 0, 9, 9, 3, 'Exchange 1st and 9th stack items.'),
    0x98: ('SWAP9', 0, 10, 10, 3, 'Exchange 1st and 10th stack items.'),
    0x99: ('SWAP10', 0, 11, 11, 3, 'Exchange 1st and 11th stack items.'),
    0x9a: ('SWAP11', 0, 12, 12, 3, 'Exchange 1st and 12th stack items.'),
    0x9b: ('SWAP12', 0, 13, 13, 3, 'Exchange 1st and 13th stack items.'),
    0x9c: ('SWAP13', 0, 14, 14, 3, 'Exchange 1st and 14th stack items.'),
    0x9d: ('SWAP14', 0, 15, 15, 3, 'Exchange 1st and 15th stack items.'),
    0x9e: ('SWAP15', 0, 16, 16, 3, 'Exchange 1st and 16th stack items.'),
    0x9f: ('SWAP16', 0, 17, 17, 3, 'Exchange 1st and 17th stack items.'),
    0xa0: ('LOG0', 0, 2, 0, 375, 'Append log record with no topics.'),
    0xa1: ('LOG1', 0, 3, 0, 750, 'Append log record with one topic.'),
    0xa2: ('LOG2', 0, 4, 0, 1125, 'Append log record with two topics.'),
    0xa3: ('LOG3', 0, 5, 0, 1500, 'Append log record with three topics.'),
    0xa4: ('LOG4', 0, 6, 0, 1875, 'Append log record with four topics.'),
    0xf0: ('CREATE', 0, 3, 1, 32000, 'Create a new account with associated code.'),
    0xf1: ('CALL', 0, 7, 1, 40, 'Message-call into an account.'),
    0xf2: ('CALLCODE', 0, 7, 1, 40, "Message-call into this account with alternative account's code."),
    0xf3: ('RETURN', 0, 2, 0, 0, 'Halt execution returning output data.'),
    0xf4: ('DELEGATECALL', 0, 6, 1, 40, "like CALLCODE but keeps caller's value and sender"),
    0xf5: ('CREATE2', 0, 4, 1, 32000, 'Create a new account with associated code at a predictable address'), # new
    0xfa: ('STATICCALL', 0, 6, 1, 40, 'like CALL but disallow state modifications'),
    0xfb: ('CREATE2', 0, 4, 1, 32000, 'create new account with associated code at address `sha3(sender + salt + sha3(init code)) % 2**160`'),
    0xfd: ('REVERT', 0, 2, 0, 0, 'halt execution, revert state and return output data'),
    0xfe: ('INVALID', 0, 0, 0, 0, 'old ASSERTFAIL - invalid instruction for expressing runtime errors (e.g., division-by-zero)'),
    0xff: ('SELFDESTRUCT', 0, 1, 0, 5000, 'Halt execution and register account for later deletion.')
}


class EVM(object):
    """Bytecode for Ethereum VM."""

    def __init__(self):
        self.table = _table
        self.reverse_table = self._get_reverse_table()

    def _get_reverse_table(self):
        """Build an internal table used in the assembler."""
        reverse_table = {}
        for (opcode, (mnemonic, immediate_operand_size,
                      pops, pushes, gas, description)) in _table.items():
            reverse_table[mnemonic] = opcode, mnemonic, immediate_operand_size, \
                pops, pushes, gas, description
        return reverse_table
