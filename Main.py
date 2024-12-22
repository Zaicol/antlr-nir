from antlr4 import *
from AssemblyLexer import AssemblyLexer
from AssemblyParser import AssemblyParser
from LabelCollector import LabelCollector
from CodeGenerator import CodeGenerator

# java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor Assembly.g4

program = """
start: 
MOV R0, 5
ADD R0, 10
JMP end
SUB R1, 3
end:
MOV R1, 1
JMP start
INC R0
JMP 2
"""

program = "\n".join([line for line in program.splitlines() if line.strip()]) + '\n'

# Создание потока входных данных
input_stream = InputStream(program)

# Создаем лексер и парсер
lexer = AssemblyLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = AssemblyParser(token_stream)

# Парсим программу и создаем дерево разбора
tree = parser.program()
print("Дерево разбора создано:", tree.toStringTree(recog=parser))

# Проверка на наличие ошибок
if parser.getNumberOfSyntaxErrors() > 0:
    print("Syntax errors found in the code.")
else:
    print("No syntax errors found.")

print("\n==================\n")

# Первый проход: сбор меток
label_collector = LabelCollector()
label_collector.visit(tree)
labels = label_collector.get_labels()
print("Найденные метки и их адреса:", labels)

print("\n==================\n")

# Второй проход: генерация машинного кода
code_generator = CodeGenerator(labels)
code_generator.visit(tree)
machine_code = code_generator.get_machine_code()
print("Сгенерированный машинный код:", machine_code)

# Таблица
program_lines = [line.strip() for line in program.splitlines() if line.strip()]
program_lines = list(filter(lambda line: ':' not in line, program_lines))

address = 0
output = "\nАдрес    Машинный код       Ассемблер\n"
output += "-" * 40 + "\n"

assembler_i = 0
machine_code_i = 0


def mchex():
    global machine_code_i
    machine_code_i += 1
    return f"{machine_code[machine_code_i - 1]:02X} "


while machine_code_i < len(machine_code):
    addr_str = f"0x{address:02X}"

    mc_str = mchex() + mchex() + mchex()

    asm_str = program_lines[assembler_i] if assembler_i < len(program_lines) else ""
    assembler_i += 1

    output += f"{addr_str:8} {mc_str:18} {asm_str}\n"
    address += len(mc_str.split())

print(output)
