from bidict import bidict

instructions = {
    "MOV": 0x01,
    "ADD": 0x02,
    "SUB": 0x03,
    "JMP": 0x04,
}
registers = {
    "R0": 0x01,
    "R1": 0x02,
    "R2": 0x03
}

bi_instructions = bidict(instructions).inverse
bi_registers = bidict(registers).inverse
