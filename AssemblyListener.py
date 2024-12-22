# Generated from Assembly.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AssemblyParser import AssemblyParser
else:
    from AssemblyParser import AssemblyParser

# This class defines a complete listener for a parse tree produced by AssemblyParser.
class AssemblyListener(ParseTreeListener):

    # Enter a parse tree produced by AssemblyParser#program.
    def enterProgram(self, ctx:AssemblyParser.ProgramContext):
        pass

    # Exit a parse tree produced by AssemblyParser#program.
    def exitProgram(self, ctx:AssemblyParser.ProgramContext):
        pass


    # Enter a parse tree produced by AssemblyParser#instructionLine.
    def enterInstructionLine(self, ctx:AssemblyParser.InstructionLineContext):
        pass

    # Exit a parse tree produced by AssemblyParser#instructionLine.
    def exitInstructionLine(self, ctx:AssemblyParser.InstructionLineContext):
        pass


    # Enter a parse tree produced by AssemblyParser#labelLine.
    def enterLabelLine(self, ctx:AssemblyParser.LabelLineContext):
        pass

    # Exit a parse tree produced by AssemblyParser#labelLine.
    def exitLabelLine(self, ctx:AssemblyParser.LabelLineContext):
        pass


    # Enter a parse tree produced by AssemblyParser#label.
    def enterLabel(self, ctx:AssemblyParser.LabelContext):
        pass

    # Exit a parse tree produced by AssemblyParser#label.
    def exitLabel(self, ctx:AssemblyParser.LabelContext):
        pass


    # Enter a parse tree produced by AssemblyParser#moveInstruction.
    def enterMoveInstruction(self, ctx:AssemblyParser.MoveInstructionContext):
        pass

    # Exit a parse tree produced by AssemblyParser#moveInstruction.
    def exitMoveInstruction(self, ctx:AssemblyParser.MoveInstructionContext):
        pass


    # Enter a parse tree produced by AssemblyParser#addInstruction.
    def enterAddInstruction(self, ctx:AssemblyParser.AddInstructionContext):
        pass

    # Exit a parse tree produced by AssemblyParser#addInstruction.
    def exitAddInstruction(self, ctx:AssemblyParser.AddInstructionContext):
        pass


    # Enter a parse tree produced by AssemblyParser#subInstruction.
    def enterSubInstruction(self, ctx:AssemblyParser.SubInstructionContext):
        pass

    # Exit a parse tree produced by AssemblyParser#subInstruction.
    def exitSubInstruction(self, ctx:AssemblyParser.SubInstructionContext):
        pass


    # Enter a parse tree produced by AssemblyParser#incInstruction.
    def enterIncInstruction(self, ctx:AssemblyParser.IncInstructionContext):
        pass

    # Exit a parse tree produced by AssemblyParser#incInstruction.
    def exitIncInstruction(self, ctx:AssemblyParser.IncInstructionContext):
        pass


    # Enter a parse tree produced by AssemblyParser#jumpInstruction.
    def enterJumpInstruction(self, ctx:AssemblyParser.JumpInstructionContext):
        pass

    # Exit a parse tree produced by AssemblyParser#jumpInstruction.
    def exitJumpInstruction(self, ctx:AssemblyParser.JumpInstructionContext):
        pass


    # Enter a parse tree produced by AssemblyParser#jumpValueInstruction.
    def enterJumpValueInstruction(self, ctx:AssemblyParser.JumpValueInstructionContext):
        pass

    # Exit a parse tree produced by AssemblyParser#jumpValueInstruction.
    def exitJumpValueInstruction(self, ctx:AssemblyParser.JumpValueInstructionContext):
        pass


    # Enter a parse tree produced by AssemblyParser#value.
    def enterValue(self, ctx:AssemblyParser.ValueContext):
        pass

    # Exit a parse tree produced by AssemblyParser#value.
    def exitValue(self, ctx:AssemblyParser.ValueContext):
        pass


    # Enter a parse tree produced by AssemblyParser#register.
    def enterRegister(self, ctx:AssemblyParser.RegisterContext):
        pass

    # Exit a parse tree produced by AssemblyParser#register.
    def exitRegister(self, ctx:AssemblyParser.RegisterContext):
        pass



del AssemblyParser