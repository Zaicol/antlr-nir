# Generated from Assembly.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,16,58,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,3,
        0,14,8,0,1,0,5,0,17,8,0,10,0,12,0,20,9,0,1,0,1,0,1,1,1,1,3,1,26,
        8,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,52,8,3,1,4,1,4,1,5,1,5,1,
        5,0,0,6,0,2,4,6,8,10,0,1,1,0,3,6,59,0,18,1,0,0,0,2,25,1,0,0,0,4,
        27,1,0,0,0,6,51,1,0,0,0,8,53,1,0,0,0,10,55,1,0,0,0,12,14,3,2,1,0,
        13,12,1,0,0,0,13,14,1,0,0,0,14,15,1,0,0,0,15,17,5,13,0,0,16,13,1,
        0,0,0,17,20,1,0,0,0,18,16,1,0,0,0,18,19,1,0,0,0,19,21,1,0,0,0,20,
        18,1,0,0,0,21,22,5,0,0,1,22,1,1,0,0,0,23,26,3,6,3,0,24,26,3,4,2,
        0,25,23,1,0,0,0,25,24,1,0,0,0,26,3,1,0,0,0,27,28,5,11,0,0,28,29,
        5,1,0,0,29,5,1,0,0,0,30,31,5,7,0,0,31,32,3,10,5,0,32,33,5,2,0,0,
        33,34,3,8,4,0,34,52,1,0,0,0,35,36,5,8,0,0,36,37,3,10,5,0,37,38,5,
        2,0,0,38,39,3,8,4,0,39,52,1,0,0,0,40,41,5,9,0,0,41,42,3,10,5,0,42,
        43,5,2,0,0,43,44,3,8,4,0,44,52,1,0,0,0,45,46,5,16,0,0,46,52,3,10,
        5,0,47,48,5,10,0,0,48,52,5,11,0,0,49,50,5,10,0,0,50,52,3,8,4,0,51,
        30,1,0,0,0,51,35,1,0,0,0,51,40,1,0,0,0,51,45,1,0,0,0,51,47,1,0,0,
        0,51,49,1,0,0,0,52,7,1,0,0,0,53,54,5,12,0,0,54,9,1,0,0,0,55,56,7,
        0,0,0,56,11,1,0,0,0,4,13,18,25,51
    ]

class AssemblyParser ( Parser ):

    grammarFileName = "Assembly.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "','", "'R0'", "'R1'", "'R2'", 
                     "'R3'", "'MOV'", "'ADD'", "'SUB'", "'JMP'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'INC'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "MOV", "ADD", 
                      "SUB", "JMP", "ID", "INT", "NL", "WS", "COMMENT", 
                      "INC" ]

    RULE_program = 0
    RULE_line = 1
    RULE_label = 2
    RULE_instruction = 3
    RULE_value = 4
    RULE_register = 5

    ruleNames =  [ "program", "line", "label", "instruction", "value", "register" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    MOV=7
    ADD=8
    SUB=9
    JMP=10
    ID=11
    INT=12
    NL=13
    WS=14
    COMMENT=15
    INC=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(AssemblyParser.EOF, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(AssemblyParser.NL)
            else:
                return self.getToken(AssemblyParser.NL, i)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AssemblyParser.LineContext)
            else:
                return self.getTypedRuleContext(AssemblyParser.LineContext,i)


        def getRuleIndex(self):
            return AssemblyParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = AssemblyParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 77696) != 0):
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 69504) != 0):
                    self.state = 12
                    self.line()


                self.state = 15
                self.match(AssemblyParser.NL)
                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 21
            self.match(AssemblyParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AssemblyParser.RULE_line

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class InstructionLineContext(LineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssemblyParser.LineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def instruction(self):
            return self.getTypedRuleContext(AssemblyParser.InstructionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstructionLine" ):
                listener.enterInstructionLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstructionLine" ):
                listener.exitInstructionLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstructionLine" ):
                return visitor.visitInstructionLine(self)
            else:
                return visitor.visitChildren(self)


    class LabelLineContext(LineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssemblyParser.LineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def label(self):
            return self.getTypedRuleContext(AssemblyParser.LabelContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabelLine" ):
                listener.enterLabelLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabelLine" ):
                listener.exitLabelLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabelLine" ):
                return visitor.visitLabelLine(self)
            else:
                return visitor.visitChildren(self)



    def line(self):

        localctx = AssemblyParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        try:
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 8, 9, 10, 16]:
                localctx = AssemblyParser.InstructionLineContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.instruction()
                pass
            elif token in [11]:
                localctx = AssemblyParser.LabelLineContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.label()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AssemblyParser.ID, 0)

        def getRuleIndex(self):
            return AssemblyParser.RULE_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel" ):
                listener.enterLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel" ):
                listener.exitLabel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel" ):
                return visitor.visitLabel(self)
            else:
                return visitor.visitChildren(self)




    def label(self):

        localctx = AssemblyParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(AssemblyParser.ID)
            self.state = 28
            self.match(AssemblyParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AssemblyParser.RULE_instruction

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AddInstructionContext(InstructionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssemblyParser.InstructionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ADD(self):
            return self.getToken(AssemblyParser.ADD, 0)
        def register(self):
            return self.getTypedRuleContext(AssemblyParser.RegisterContext,0)

        def value(self):
            return self.getTypedRuleContext(AssemblyParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddInstruction" ):
                listener.enterAddInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddInstruction" ):
                listener.exitAddInstruction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddInstruction" ):
                return visitor.visitAddInstruction(self)
            else:
                return visitor.visitChildren(self)


    class JumpValueInstructionContext(InstructionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssemblyParser.InstructionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def JMP(self):
            return self.getToken(AssemblyParser.JMP, 0)
        def value(self):
            return self.getTypedRuleContext(AssemblyParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJumpValueInstruction" ):
                listener.enterJumpValueInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJumpValueInstruction" ):
                listener.exitJumpValueInstruction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJumpValueInstruction" ):
                return visitor.visitJumpValueInstruction(self)
            else:
                return visitor.visitChildren(self)


    class MoveInstructionContext(InstructionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssemblyParser.InstructionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MOV(self):
            return self.getToken(AssemblyParser.MOV, 0)
        def register(self):
            return self.getTypedRuleContext(AssemblyParser.RegisterContext,0)

        def value(self):
            return self.getTypedRuleContext(AssemblyParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMoveInstruction" ):
                listener.enterMoveInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMoveInstruction" ):
                listener.exitMoveInstruction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMoveInstruction" ):
                return visitor.visitMoveInstruction(self)
            else:
                return visitor.visitChildren(self)


    class SubInstructionContext(InstructionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssemblyParser.InstructionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SUB(self):
            return self.getToken(AssemblyParser.SUB, 0)
        def register(self):
            return self.getTypedRuleContext(AssemblyParser.RegisterContext,0)

        def value(self):
            return self.getTypedRuleContext(AssemblyParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubInstruction" ):
                listener.enterSubInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubInstruction" ):
                listener.exitSubInstruction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubInstruction" ):
                return visitor.visitSubInstruction(self)
            else:
                return visitor.visitChildren(self)


    class IncInstructionContext(InstructionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssemblyParser.InstructionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INC(self):
            return self.getToken(AssemblyParser.INC, 0)
        def register(self):
            return self.getTypedRuleContext(AssemblyParser.RegisterContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncInstruction" ):
                listener.enterIncInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncInstruction" ):
                listener.exitIncInstruction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIncInstruction" ):
                return visitor.visitIncInstruction(self)
            else:
                return visitor.visitChildren(self)


    class JumpInstructionContext(InstructionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AssemblyParser.InstructionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def JMP(self):
            return self.getToken(AssemblyParser.JMP, 0)
        def ID(self):
            return self.getToken(AssemblyParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJumpInstruction" ):
                listener.enterJumpInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJumpInstruction" ):
                listener.exitJumpInstruction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJumpInstruction" ):
                return visitor.visitJumpInstruction(self)
            else:
                return visitor.visitChildren(self)



    def instruction(self):

        localctx = AssemblyParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_instruction)
        try:
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = AssemblyParser.MoveInstructionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.match(AssemblyParser.MOV)
                self.state = 31
                self.register()
                self.state = 32
                self.match(AssemblyParser.T__1)
                self.state = 33
                self.value()
                pass

            elif la_ == 2:
                localctx = AssemblyParser.AddInstructionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.match(AssemblyParser.ADD)
                self.state = 36
                self.register()
                self.state = 37
                self.match(AssemblyParser.T__1)
                self.state = 38
                self.value()
                pass

            elif la_ == 3:
                localctx = AssemblyParser.SubInstructionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 40
                self.match(AssemblyParser.SUB)
                self.state = 41
                self.register()
                self.state = 42
                self.match(AssemblyParser.T__1)
                self.state = 43
                self.value()
                pass

            elif la_ == 4:
                localctx = AssemblyParser.IncInstructionContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 45
                self.match(AssemblyParser.INC)
                self.state = 46
                self.register()
                pass

            elif la_ == 5:
                localctx = AssemblyParser.JumpInstructionContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 47
                self.match(AssemblyParser.JMP)
                self.state = 48
                self.match(AssemblyParser.ID)
                pass

            elif la_ == 6:
                localctx = AssemblyParser.JumpValueInstructionContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 49
                self.match(AssemblyParser.JMP)
                self.state = 50
                self.value()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(AssemblyParser.INT, 0)

        def getRuleIndex(self):
            return AssemblyParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = AssemblyParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(AssemblyParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RegisterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AssemblyParser.RULE_register

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegister" ):
                listener.enterRegister(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegister" ):
                listener.exitRegister(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegister" ):
                return visitor.visitRegister(self)
            else:
                return visitor.visitChildren(self)




    def register(self):

        localctx = AssemblyParser.RegisterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_register)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 120) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





