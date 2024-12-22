from AssemblyVisitor import AssemblyVisitor
from AssemblyParser import AssemblyParser
from CodeDict import *


class CodeGenerator(AssemblyVisitor):
    def __init__(self, labels):
        self.labels = labels          # Метки и их адреса
        self.machine_code = []        # Байтовый код программы

    def visitMoveInstruction(self, ctx: AssemblyParser.MoveInstructionContext):
        reg = self.visit(ctx.register())
        value = int(ctx.value().getText())
        self.machine_code.append(instructions['MOV'])  # Код операции MOV
        self.machine_code.append(reg)
        self.machine_code.append(value)
        return self.visitChildren(ctx)

    def visitAddInstruction(self, ctx: AssemblyParser.AddInstructionContext):
        reg = self.visit(ctx.register())
        value = int(ctx.value().getText())
        self.machine_code.append(instructions['ADD'])
        self.machine_code.append(reg)
        self.machine_code.append(value)
        return self.visitChildren(ctx)

    def visitSubInstruction(self, ctx: AssemblyParser.SubInstructionContext):
        reg = self.visit(ctx.register())
        value = int(ctx.value().getText())
        self.machine_code.append(instructions['SUB'])
        self.machine_code.append(reg)
        self.machine_code.append(value)
        return self.visitChildren(ctx)

    def visitJumpInstruction(self, ctx: AssemblyParser.JumpInstructionContext):
        label_name = ctx.ID().getText()
        if label_name in self.labels:
            target_address = self.labels[label_name]
            print(f"Resolving jump to label '{label_name}' at address {target_address}")
            self.machine_code.append(instructions['JMP'])
            self.machine_code.append(target_address * 3)
            self.machine_code.append(0x00)
        else:
            raise ValueError(f"Undefined label: {label_name}")
        return self.visitChildren(ctx)

    def visitJumpValueInstruction(self, ctx: AssemblyParser.JumpInstructionContext):
        target_address = int(ctx.value().getText())
        print(f"Resolving jump at address {target_address}")
        self.machine_code.append(instructions['JMP'])
        self.machine_code.append(target_address * 3)
        self.machine_code.append(0x00)
        return self.visitChildren(ctx)

    def visitIncInstruction(self, ctx: AssemblyParser.JumpInstructionContext):
        reg = self.visit(ctx.register())
        value = 0x01
        self.machine_code.append(instructions['ADD'])
        self.machine_code.append(reg)
        self.machine_code.append(value)
        return self.visitChildren(ctx)

    def visitRegister(self, ctx: AssemblyParser.RegisterContext):
        ret = registers.get(ctx.getText(), None)
        if ret is None:
            raise ValueError(f"Unknown register: {ctx.getText()}")

        return ret

    def get_machine_code(self):
        return self.machine_code
