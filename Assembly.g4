grammar Assembly;

program: (line? NL)* EOF;

line
    : instruction          # instructionLine
    | label                       # labelLine
    ;

label: ID ':';

instruction
    : MOV register ',' value     # moveInstruction
    | ADD register ',' value     # addInstruction
    | SUB register ',' value     # subInstruction
    | INC register               # incInstruction
    | JMP ID                     # jumpInstruction
    | JMP value                  # jumpValueInstruction
    ;

value: INT;
register: 'R0' | 'R1' | 'R2' | 'R3';

MOV: 'MOV';
ADD: 'ADD';
SUB: 'SUB';
JMP: 'JMP';

ID: [a-z][a-z0-9_]*;
INT: [0-9]+;
NL: '\r'? '\n';

WS: [ \t]+ -> skip;
COMMENT: ';' .*? -> skip;

INC : 'INC';