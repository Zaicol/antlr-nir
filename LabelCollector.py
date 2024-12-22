from AssemblyVisitor import AssemblyVisitor
from AssemblyParser import AssemblyParser


class LabelCollector(AssemblyVisitor):
    def __init__(self):
        self.labels = {}  # Словарь для хранения меток и их адресов
        self.address = 0  # Текущий адрес

    def visitLabelLine(self, ctx: AssemblyParser.LabelLineContext):
        # Сохранение метки с текущим адресом
        label_name = ctx.label().ID().getText()
        self.labels[label_name] = self.address
        print(f"Label found: {label_name} at address {self.address}")
        return self.visitChildren(ctx)

    def visitInstructionLine(self, ctx: AssemblyParser.InstructionLineContext):
        print(f"\tInstruction found at address {self.address}")
        # Увеличение адреса для каждой инструкции
        self.address += 1
        return self.visitChildren(ctx)

    def get_labels(self):
        return self.labels
