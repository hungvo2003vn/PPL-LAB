# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\t")
        buf.write("\62\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\3\3\3\3\4\3\4\7\4")
        buf.write("\34\n\4\f\4\16\4\37\13\4\3\5\3\5\3\6\3\6\3\7\6\7&\n\7")
        buf.write("\r\7\16\7\'\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\n\3\n\2\2\13")
        buf.write("\3\3\5\4\7\5\t\2\13\2\r\6\17\7\21\b\23\t\3\2\6\3\2c|\4")
        buf.write("\2\62;c|\3\2\62;\5\2\13\f\17\17\"\"\2\61\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3")
        buf.write("\2\2\2\2\23\3\2\2\2\3\25\3\2\2\2\5\27\3\2\2\2\7\31\3\2")
        buf.write("\2\2\t \3\2\2\2\13\"\3\2\2\2\r%\3\2\2\2\17+\3\2\2\2\21")
        buf.write(".\3\2\2\2\23\60\3\2\2\2\25\26\7\60\2\2\26\4\3\2\2\2\27")
        buf.write("\30\7a\2\2\30\6\3\2\2\2\31\35\t\2\2\2\32\34\t\3\2\2\33")
        buf.write("\32\3\2\2\2\34\37\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2")
        buf.write("\36\b\3\2\2\2\37\35\3\2\2\2 !\t\2\2\2!\n\3\2\2\2\"#\t")
        buf.write("\4\2\2#\f\3\2\2\2$&\t\5\2\2%$\3\2\2\2&\'\3\2\2\2\'%\3")
        buf.write("\2\2\2\'(\3\2\2\2()\3\2\2\2)*\b\7\2\2*\16\3\2\2\2+,\13")
        buf.write("\2\2\2,-\b\b\3\2-\20\3\2\2\2./\13\2\2\2/\22\3\2\2\2\60")
        buf.write("\61\13\2\2\2\61\24\3\2\2\2\5\2\35\'\4\b\2\2\3\b\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    IDENTIFIER = 3
    WS = 4
    ERROR_CHAR = 5
    UNCLOSE_STRING = 6
    ILLEGAL_ESCAPE = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'.'", "'_'" ]

    symbolicNames = [ "<INVALID>",
            "IDENTIFIER", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "IDENTIFIER", "LETTER", "DIGIT", "WS", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[6] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


