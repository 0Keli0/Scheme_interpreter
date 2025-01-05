# Generated from ./interpreter_utils/scheme.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .schemeParser import schemeParser
else:
    from schemeParser import schemeParser

# This class defines a complete generic visitor for a parse tree produced by schemeParser.

class schemeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by schemeParser#root.
    def visitRoot(self, ctx:schemeParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#exprs.
    def visitExprs(self, ctx:schemeParser.ExprsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#expr_S.
    def visitExpr_S(self, ctx:schemeParser.Expr_SContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#params.
    def visitParams(self, ctx:schemeParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#number.
    def visitNumber(self, ctx:schemeParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#boolean.
    def visitBoolean(self, ctx:schemeParser.BooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#var.
    def visitVar(self, ctx:schemeParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#string.
    def visitString(self, ctx:schemeParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#listElements.
    def visitListElements(self, ctx:schemeParser.ListElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by schemeParser#expr_param.
    def visitExpr_param(self, ctx:schemeParser.Expr_paramContext):
        return self.visitChildren(ctx)



del schemeParser