# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13")
        buf.write("\'\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\4\6\4\25\n\4\r\4\16\4\26\3\5\6\5\32")
        buf.write("\n\5\r\5\16\5\33\3\6\7\6\37\n\6\f\6\16\6\"\13\6\3\6\5")
        buf.write("\6%\n\6\3\6\2\2\7\2\4\6\b\n\2\3\4\2\3\4\n\13\2%\2\f\3")
        buf.write("\2\2\2\4\16\3\2\2\2\6\24\3\2\2\2\b\31\3\2\2\2\n \3\2\2")
        buf.write("\2\f\r\7\2\2\3\r\3\3\2\2\2\16\17\5\6\4\2\17\20\7\3\2\2")
        buf.write("\20\21\5\b\5\2\21\22\5\n\6\2\22\5\3\2\2\2\23\25\7\n\2")
        buf.write("\2\24\23\3\2\2\2\25\26\3\2\2\2\26\24\3\2\2\2\26\27\3\2")
        buf.write("\2\2\27\7\3\2\2\2\30\32\7\n\2\2\31\30\3\2\2\2\32\33\3")
        buf.write("\2\2\2\33\31\3\2\2\2\33\34\3\2\2\2\34\t\3\2\2\2\35\37")
        buf.write("\t\2\2\2\36\35\3\2\2\2\37\"\3\2\2\2 \36\3\2\2\2 !\3\2")
        buf.write("\2\2!$\3\2\2\2\" \3\2\2\2#%\7\3\2\2$#\3\2\2\2$%\3\2\2")
        buf.write("\2%\13\3\2\2\2\6\26\33 $")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "'_'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "IDENTIFIER", 
                      "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "LETTER", "DIGIT" ]

    RULE_program = 0
    RULE_bkNetID = 1
    RULE_ten = 2
    RULE_ho = 3
    RULE_chuoiTuChon = 4

    ruleNames =  [ "program", "bkNetID", "ten", "ho", "chuoiTuChon" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    IDENTIFIER=3
    WS=4
    ERROR_CHAR=5
    UNCLOSE_STRING=6
    ILLEGAL_ESCAPE=7
    LETTER=8
    DIGIT=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BkNetIDContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.t = None # TenContext
            self.h = None # HoContext
            self.ct = None # ChuoiTuChonContext

        def ten(self):
            return self.getTypedRuleContext(BKOOLParser.TenContext,0)


        def ho(self):
            return self.getTypedRuleContext(BKOOLParser.HoContext,0)


        def chuoiTuChon(self):
            return self.getTypedRuleContext(BKOOLParser.ChuoiTuChonContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_bkNetID

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBkNetID" ):
                return visitor.visitBkNetID(self)
            else:
                return visitor.visitChildren(self)




    def bkNetID(self):

        localctx = BKOOLParser.BkNetIDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_bkNetID)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            localctx.t = self.ten()
            self.state = 13
            self.match(BKOOLParser.T__0)
            self.state = 14
            localctx.h = self.ho()
            self.state = 15
            localctx.ct = self.chuoiTuChon()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TenContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LETTER(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.LETTER)
            else:
                return self.getToken(BKOOLParser.LETTER, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_ten

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTen" ):
                return visitor.visitTen(self)
            else:
                return visitor.visitChildren(self)




    def ten(self):

        localctx = BKOOLParser.TenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_ten)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 17
                self.match(BKOOLParser.LETTER)
                self.state = 20 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKOOLParser.LETTER):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LETTER(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.LETTER)
            else:
                return self.getToken(BKOOLParser.LETTER, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_ho

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHo" ):
                return visitor.visitHo(self)
            else:
                return visitor.visitChildren(self)




    def ho(self):

        localctx = BKOOLParser.HoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ho)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 22
                    self.match(BKOOLParser.LETTER)

                else:
                    raise NoViableAltException(self)
                self.state = 25 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChuoiTuChonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LETTER(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.LETTER)
            else:
                return self.getToken(BKOOLParser.LETTER, i)

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.DIGIT)
            else:
                return self.getToken(BKOOLParser.DIGIT, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_chuoiTuChon

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChuoiTuChon" ):
                return visitor.visitChuoiTuChon(self)
            else:
                return visitor.visitChildren(self)




    def chuoiTuChon(self):

        localctx = BKOOLParser.ChuoiTuChonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_chuoiTuChon)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 27
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.T__0) | (1 << BKOOLParser.T__1) | (1 << BKOOLParser.LETTER) | (1 << BKOOLParser.DIGIT))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 32
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.T__0:
                self.state = 33
                self.match(BKOOLParser.T__0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





