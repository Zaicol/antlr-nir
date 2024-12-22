# Generated from Assembly.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AssemblyParser import AssemblyParser
else:
    from AssemblyParser import AssemblyParser

# This class defines a complete generic visitor for a parse tree produced by AssemblyParser.

class AssemblyVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AssemblyParser#program.
    def visitProgram(self, ctx:AssemblyParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssemblyParser#instructionLine.
    def visitInstructionLine(self, ctx:AssemblyParser.InstructionLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssemblyParser#labelLine.
    def visitLabelLine(self, ctx:AssemblyParser.LabelLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssemblyParser#label.
    def visitLabel(self, ctx:AssemblyParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssemblyParser#moveInstruction.
    def visitMoveInstruction(self, ctx:AssemblyParser.MoveInstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssemblyParser#addInstruction.
    def visitAddInstruction(self, ctx:AssemblyParser.AddInstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssemblyParser#subInstruction.
    def visitSubInstruction(self, ctx:AssemblyParser.SubInstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssemblyParser#incInstruction.
    def visitIncInstruction(self, ctx:AssemblyParser.IncInstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssemblyParser#jumpInstruction.
    def visitJumpInstruction(self, ctx:AssemblyParser.JumpInstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssemblyParser#jumpValueInstruction.
    def visitJumpValueInstruction(self, ctx:AssemblyParser.JumpValueInstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssemblyParser#value.
    def visitValue(self, ctx:AssemblyParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AssemblyParser#register.
    def visitRegister(self, ctx:AssemblyParser.RegisterContext):
        return self.visitChildren(ctx)



del AssemblyParser