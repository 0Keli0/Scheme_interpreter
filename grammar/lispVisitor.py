# Generated from ./grammar/scheme.g4 by ANTLR 4.13.2
from antlr4 import *

if "." in __name__:
    from .lispParser import lispParser
else:
    from lispParser import lispParser

# This class defines a complete generic visitor for a parse tree produced by lispParser.


class lispVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by lispParser#root.
    def visitRoot(self, ctx: lispParser.RootContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by lispParser#exprs.
    def visitExprs(self, ctx: lispParser.ExprsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by lispParser#expr_S.
    def visitExpr_S(self, ctx: lispParser.Expr_SContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by lispParser#params.
    def visitParams(self, ctx: lispParser.ParamsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by lispParser#number.
    def visitNumber(self, ctx: lispParser.NumberContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by lispParser#float.
    def visitFloat(self, ctx: lispParser.FloatContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by lispParser#boolean.
    def visitBoolean(self, ctx: lispParser.BooleanContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by lispParser#var.
    def visitVar(self, ctx: lispParser.VarContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by lispParser#string.
    def visitString(self, ctx: lispParser.StringContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by lispParser#listElements.
    def visitListElements(self, ctx: lispParser.ListElementsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by lispParser#expr_param.
    def visitExpr_param(self, ctx: lispParser.Expr_paramContext):
        return self.visitChildren(ctx)


del lispParser
