# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#bkNetID.
    def visitBkNetID(self, ctx:BKOOLParser.BkNetIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#ten.
    def visitTen(self, ctx:BKOOLParser.TenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#ho.
    def visitHo(self, ctx:BKOOLParser.HoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#chuoiTuChon.
    def visitChuoiTuChon(self, ctx:BKOOLParser.ChuoiTuChonContext):
        return self.visitChildren(ctx)



del BKOOLParser