# Octopus Update

Keep updating the original [Octopus](https://github.com/FuzzingLabs/octopus) (archived on Mar 6, 2024), the static analysis tool for smart contracts.

## Goals

- Bug fixing.
- Updating to support new versions of smart contracts.
- Adding new features.

## EOSIO Update

### Bug Fixing

1. Fixed the `--onlyfunc` option in graph generation.

   Fixed the problem that Octopus cannot generate CFG for individual function using `--onlyfunc` option.

2. Fixed the `return` instruction handler.

   The `return` instruction has no argument when there is no variable on the stack, which indicates that the function has no return value.

### New Features

1. Enable printing the indices of local and global variables in the graphs.
2. Enable printing the offsets of memory instructions in the graphs.

## EVM Update

### Opcodes Update

Adding new opcodes to support new versions of Solidity.

Reference: [https://www.evm.codes](https://www.evm.codes)

#### All supported opcodes

New opcodes are marked in **bold**:

|      | 0    | 1    | 2    | 3    | 4    | 5      | 6      | 7      | 8      | 9      | A      | B      | C      | D      | E      | F      |
| ---- | ---- | ---- | ---- | ---- | ---- | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| 0    | 00   | 01   | 02   | 03   | 04   | 05     | 06     | 07     | 08     | 09     | 0a     | 0b     |        |        |        |        |
| 1    | 10   | 11   | 12   | 13   | 14   | 15     | 16     | 17     | 18     | 19     | 1a     | **1B** | **1C** | **1D** |        |        |
| 2    | 20   |      |      |      |      |        |        |        |        |        |        |        |        |        |        |        |
| 3    | 30   | 31   | 32   | 33   | 34   | 35     | 36     | 37     | 38     | 39     | 3a     | 3b     | 3c     | 3d     | 3e     | **3F** |
| 4    | 40   | 41   | 42   | 43   | 44   | 45     | **46** | **47** | **48** | **49** | **4A** |        |        |        |        |        |
| 5    | 50   | 51   | 52   | 53   | 54   | 55     | 56     | 57     | 58     | 59     | 5a     | 5b     | **5C** | **5D** | **5E** | **5F** |
| 6    | 60   | 61   | 62   | 63   | 64   | 65     | 66     | 67     | 68     | 69     | 6a     | 6b     | 6c     | 6d     | 6e     | 6f     |
| 7    | 70   | 71   | 72   | 73   | 74   | 75     | 76     | 77     | 78     | 79     | 7a     | 7b     | 7c     | 7d     | 7e     | 7f     |
| 8    | 80   | 81   | 82   | 83   | 84   | 85     | 86     | 87     | 88     | 89     | 8a     | 8b     | 8c     | 8d     | 8e     | 8f     |
| 9    | 90   | 91   | 92   | 93   | 94   | 95     | 96     | 97     | 98     | 99     | 9a     | 9b     | 9c     | 9d     | 9e     | 9f     |
| A    | a0   | a1   | a2   | a3   | a4   |        |        |        |        |        |        |        |        |        |        |        |
| B    |      |      |      |      |      |        |        |        |        |        |        |        |        |        |        |        |
| C    |      |      |      |      |      |        |        |        |        |        |        |        |        |        |        |        |
| D    |      |      |      |      |      |        |        |        |        |        |        |        |        |        |        |        |
| E    |      |      |      |      |      |        |        |        |        |        |        |        |        |        |        |        |
| F    | f0   | f1   | f2   | f3   | f4   | **f5** |        |        |        |        | fa     |        |        | fd     | fe     | ff     |

#### Details of new opcodes

| #    | Name        | In   | Out  | Gas  | Description                                                  |
| ---- | ----------- | ---- | ---- | ---- | ------------------------------------------------------------ |
| 1b   | SHL         | 2    | 1    | 3    | Left shift operation                                         |
| 1c   | SHR         | 2    | 1    | 3    | Logical right shift operation                                |
| 1d   | SAR         | 2    | 1    | 3    | Arithmetic (signed) right shift operation                    |
| 3f   | EXTCODEHASH | 1    | 1    | 100  | Get hash of an account’s code                                |
| 46   | CHAINID     | 0    | 1    | 2    | Get the chain ID                                             |
| 47   | SELFBALANCE | 0    | 1    | 5    | Get balance of currently executing account                   |
| 48   | BASEFEE     | 0    | 1    | 2    | Get the base fee                                             |
| 49   | BLOBHASH    | 1    | 1    | 3    | Get versioned hashes                                         |
| 4a   | BLOBBASEFEE | 0    | 1    | 2    | Returns the value of the blob base-fee of the current block  |
| 5c   | TLOAD       | 1    | 1    | 100  | Load word from transient storage                             |
| 5d   | TSTORE      | 2    | 0    | 100  | Save word to transient storage                               |
| 5e   | MCOPY       | 3    | 0    | 3    | Copy memory areas                                            |
| 5f   | PUSH0       | 0    | 1    | 2    | Place value 0 on stack                                       |
| f5   | CREATE2     | 4    | 1    | 3200 | Create a new account with associated code at a predictable address |

### New Features

1. Added `assembler.py`, converting opcode string to binary. (WIP)

2. Enable printing the invalid IDs for disassembling.

3. Added option `-fl` or `--flag`. Use `-fl full` with `-d` to print the offset of instructions for disassembling. 

   Example: `python3 octopus_eth_evm.py -f <filename> -d -fl full`.
