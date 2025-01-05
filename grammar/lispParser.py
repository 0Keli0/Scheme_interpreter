# Generated from ./grammar/scheme.g4 by ANTLR 4.13.2
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
        4,
        1,
        13,
        42,
        2,
        0,
        7,
        0,
        2,
        1,
        7,
        1,
        2,
        2,
        7,
        2,
        2,
        3,
        7,
        3,
        2,
        4,
        7,
        4,
        1,
        0,
        1,
        0,
        1,
        1,
        5,
        1,
        14,
        8,
        1,
        10,
        1,
        12,
        1,
        17,
        9,
        1,
        1,
        2,
        1,
        2,
        1,
        2,
        1,
        2,
        1,
        3,
        5,
        3,
        24,
        8,
        3,
        10,
        3,
        12,
        3,
        27,
        9,
        3,
        1,
        4,
        1,
        4,
        1,
        4,
        1,
        4,
        1,
        4,
        1,
        4,
        1,
        4,
        1,
        4,
        1,
        4,
        1,
        4,
        1,
        4,
        3,
        4,
        40,
        8,
        4,
        1,
        4,
        0,
        0,
        5,
        0,
        2,
        4,
        6,
        8,
        0,
        0,
        44,
        0,
        10,
        1,
        0,
        0,
        0,
        2,
        15,
        1,
        0,
        0,
        0,
        4,
        18,
        1,
        0,
        0,
        0,
        6,
        25,
        1,
        0,
        0,
        0,
        8,
        39,
        1,
        0,
        0,
        0,
        10,
        11,
        3,
        2,
        1,
        0,
        11,
        1,
        1,
        0,
        0,
        0,
        12,
        14,
        3,
        4,
        2,
        0,
        13,
        12,
        1,
        0,
        0,
        0,
        14,
        17,
        1,
        0,
        0,
        0,
        15,
        13,
        1,
        0,
        0,
        0,
        15,
        16,
        1,
        0,
        0,
        0,
        16,
        3,
        1,
        0,
        0,
        0,
        17,
        15,
        1,
        0,
        0,
        0,
        18,
        19,
        5,
        1,
        0,
        0,
        19,
        20,
        3,
        6,
        3,
        0,
        20,
        21,
        5,
        2,
        0,
        0,
        21,
        5,
        1,
        0,
        0,
        0,
        22,
        24,
        3,
        8,
        4,
        0,
        23,
        22,
        1,
        0,
        0,
        0,
        24,
        27,
        1,
        0,
        0,
        0,
        25,
        23,
        1,
        0,
        0,
        0,
        25,
        26,
        1,
        0,
        0,
        0,
        26,
        7,
        1,
        0,
        0,
        0,
        27,
        25,
        1,
        0,
        0,
        0,
        28,
        40,
        5,
        10,
        0,
        0,
        29,
        40,
        5,
        11,
        0,
        0,
        30,
        40,
        5,
        7,
        0,
        0,
        31,
        40,
        5,
        4,
        0,
        0,
        32,
        40,
        5,
        8,
        0,
        0,
        33,
        34,
        5,
        3,
        0,
        0,
        34,
        35,
        5,
        1,
        0,
        0,
        35,
        36,
        3,
        6,
        3,
        0,
        36,
        37,
        5,
        2,
        0,
        0,
        37,
        40,
        1,
        0,
        0,
        0,
        38,
        40,
        3,
        4,
        2,
        0,
        39,
        28,
        1,
        0,
        0,
        0,
        39,
        29,
        1,
        0,
        0,
        0,
        39,
        30,
        1,
        0,
        0,
        0,
        39,
        31,
        1,
        0,
        0,
        0,
        39,
        32,
        1,
        0,
        0,
        0,
        39,
        33,
        1,
        0,
        0,
        0,
        39,
        38,
        1,
        0,
        0,
        0,
        40,
        9,
        1,
        0,
        0,
        0,
        3,
        15,
        25,
        39,
    ]


class lispParser(Parser):

    grammarFileName = "scheme.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "'('", "')'", "'''"]

    symbolicNames = [
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "ID",
        "OPERATORS",
        "CONDITIONAL",
        "TRUE_FALSE",
        "STRING",
        "WORD",
        "NUM",
        "FLOAT",
        "WS",
        "LINE_COMMENT",
    ]

    RULE_root = 0
    RULE_exprs = 1
    RULE_expr = 2
    RULE_params = 3
    RULE_param = 4

    ruleNames = ["root", "exprs", "expr", "params", "param"]

    EOF = Token.EOF
    T__0 = 1
    T__1 = 2
    T__2 = 3
    ID = 4
    OPERATORS = 5
    CONDITIONAL = 6
    TRUE_FALSE = 7
    STRING = 8
    WORD = 9
    NUM = 10
    FLOAT = 11
    WS = 12
    LINE_COMMENT = 13

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(
            self, self.atn, self.decisionsToDFA, self.sharedContextCache
        )
        self._predicates = None

    class RootContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprs(self):
            return self.getTypedRuleContext(lispParser.ExprsContext, 0)

        def getRuleIndex(self):
            return lispParser.RULE_root

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitRoot"):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)

    def root(self):

        localctx = lispParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.exprs()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprsContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(lispParser.ExprContext)
            else:
                return self.getTypedRuleContext(lispParser.ExprContext, i)

        def getRuleIndex(self):
            return lispParser.RULE_exprs

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitExprs"):
                return visitor.visitExprs(self)
            else:
                return visitor.visitChildren(self)

    def exprs(self):

        localctx = lispParser.ExprsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_exprs)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 1:
                self.state = 12
                self.expr()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return lispParser.RULE_expr

        def copyFrom(self, ctx: ParserRuleContext):
            super().copyFrom(ctx)

    class Expr_SContext(ExprContext):

        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a lispParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def params(self):
            return self.getTypedRuleContext(lispParser.ParamsContext, 0)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitExpr_S"):
                return visitor.visitExpr_S(self)
            else:
                return visitor.visitChildren(self)

    def expr(self):

        localctx = lispParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr)
        try:
            localctx = lispParser.Expr_SContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(lispParser.T__0)
            self.state = 19
            self.params()
            self.state = 20
            self.match(lispParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParamsContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(lispParser.ParamContext)
            else:
                return self.getTypedRuleContext(lispParser.ParamContext, i)

        def getRuleIndex(self):
            return lispParser.RULE_params

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitParams"):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)

    def params(self):

        localctx = lispParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_params)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3F) == 0 and ((1 << _la) & 3482) != 0:
                self.state = 22
                self.param()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParamContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return lispParser.RULE_param

        def copyFrom(self, ctx: ParserRuleContext):
            super().copyFrom(ctx)

    class NumberContext(ParamContext):

        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a lispParser.ParamContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(lispParser.NUM, 0)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitNumber"):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)

    class BooleanContext(ParamContext):

        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a lispParser.ParamContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE_FALSE(self):
            return self.getToken(lispParser.TRUE_FALSE, 0)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitBoolean"):
                return visitor.visitBoolean(self)
            else:
                return visitor.visitChildren(self)

    class StringContext(ParamContext):

        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a lispParser.ParamContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(lispParser.STRING, 0)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitString"):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)

    class VarContext(ParamContext):

        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a lispParser.ParamContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(lispParser.ID, 0)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitVar"):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)

    class FloatContext(ParamContext):

        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a lispParser.ParamContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(lispParser.FLOAT, 0)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitFloat"):
                return visitor.visitFloat(self)
            else:
                return visitor.visitChildren(self)

    class ListElementsContext(ParamContext):

        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a lispParser.ParamContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def params(self):
            return self.getTypedRuleContext(lispParser.ParamsContext, 0)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitListElements"):
                return visitor.visitListElements(self)
            else:
                return visitor.visitChildren(self)

    class Expr_paramContext(ParamContext):

        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a lispParser.ParamContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(lispParser.ExprContext, 0)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitExpr_param"):
                return visitor.visitExpr_param(self)
            else:
                return visitor.visitChildren(self)

    def param(self):

        localctx = lispParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_param)
        try:
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                localctx = lispParser.NumberContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.match(lispParser.NUM)
                pass
            elif token in [11]:
                localctx = lispParser.FloatContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.match(lispParser.FLOAT)
                pass
            elif token in [7]:
                localctx = lispParser.BooleanContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                self.match(lispParser.TRUE_FALSE)
                pass
            elif token in [4]:
                localctx = lispParser.VarContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 31
                self.match(lispParser.ID)
                pass
            elif token in [8]:
                localctx = lispParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 32
                self.match(lispParser.STRING)
                pass
            elif token in [3]:
                localctx = lispParser.ListElementsContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 33
                self.match(lispParser.T__2)
                self.state = 34
                self.match(lispParser.T__0)
                self.state = 35
                self.params()
                self.state = 36
                self.match(lispParser.T__1)
                pass
            elif token in [1]:
                localctx = lispParser.Expr_paramContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 38
                self.expr()
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
