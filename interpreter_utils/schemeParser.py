# Generated from ./interpreter_utils/scheme.g4 by ANTLR 4.13.2
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
        4,1,13,41,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,1,5,
        1,14,8,1,10,1,12,1,17,9,1,1,2,1,2,1,2,1,2,1,3,5,3,24,8,3,10,3,12,
        3,27,9,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,39,8,4,1,4,
        0,0,5,0,2,4,6,8,0,0,42,0,10,1,0,0,0,2,15,1,0,0,0,4,18,1,0,0,0,6,
        25,1,0,0,0,8,38,1,0,0,0,10,11,3,2,1,0,11,1,1,0,0,0,12,14,3,4,2,0,
        13,12,1,0,0,0,14,17,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,3,1,0,
        0,0,17,15,1,0,0,0,18,19,5,1,0,0,19,20,3,6,3,0,20,21,5,2,0,0,21,5,
        1,0,0,0,22,24,3,8,4,0,23,22,1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,
        25,26,1,0,0,0,26,7,1,0,0,0,27,25,1,0,0,0,28,39,5,10,0,0,29,39,5,
        7,0,0,30,39,5,4,0,0,31,39,5,8,0,0,32,33,5,3,0,0,33,34,5,1,0,0,34,
        35,3,6,3,0,35,36,5,2,0,0,36,39,1,0,0,0,37,39,3,4,2,0,38,28,1,0,0,
        0,38,29,1,0,0,0,38,30,1,0,0,0,38,31,1,0,0,0,38,32,1,0,0,0,38,37,
        1,0,0,0,39,9,1,0,0,0,3,15,25,38
    ]

class schemeParser ( Parser ):

    grammarFileName = "scheme.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'''" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "OPERATORS", "CONDITIONAL", "TRUE_FALSE", "STRING", 
                      "WORD", "NUM", "WS", "LINE_COMMENT", "MULTI_COMMNET" ]

    RULE_root = 0
    RULE_exprs = 1
    RULE_expr = 2
    RULE_params = 3
    RULE_param = 4

    ruleNames =  [ "root", "exprs", "expr", "params", "param" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    ID=4
    OPERATORS=5
    CONDITIONAL=6
    TRUE_FALSE=7
    STRING=8
    WORD=9
    NUM=10
    WS=11
    LINE_COMMENT=12
    MULTI_COMMNET=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprs(self):
            return self.getTypedRuleContext(schemeParser.ExprsContext,0)


        def getRuleIndex(self):
            return schemeParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = schemeParser.RootContext(self, self._ctx, self.state)
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(schemeParser.ExprContext)
            else:
                return self.getTypedRuleContext(schemeParser.ExprContext,i)


        def getRuleIndex(self):
            return schemeParser.RULE_exprs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprs" ):
                return visitor.visitExprs(self)
            else:
                return visitor.visitChildren(self)




    def exprs(self):

        localctx = schemeParser.ExprsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_exprs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return schemeParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Expr_SContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a schemeParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def params(self):
            return self.getTypedRuleContext(schemeParser.ParamsContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_S" ):
                return visitor.visitExpr_S(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = schemeParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr)
        try:
            localctx = schemeParser.Expr_SContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(schemeParser.T__0)
            self.state = 19
            self.params()
            self.state = 20
            self.match(schemeParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(schemeParser.ParamContext)
            else:
                return self.getTypedRuleContext(schemeParser.ParamContext,i)


        def getRuleIndex(self):
            return schemeParser.RULE_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParams" ):
                return visitor.visitParams(self)
            else:
                return visitor.visitChildren(self)




    def params(self):

        localctx = schemeParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1434) != 0):
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return schemeParser.RULE_param

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NumberContext(ParamContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a schemeParser.ParamContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(schemeParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)


    class BooleanContext(ParamContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a schemeParser.ParamContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE_FALSE(self):
            return self.getToken(schemeParser.TRUE_FALSE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean" ):
                return visitor.visitBoolean(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(ParamContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a schemeParser.ParamContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(schemeParser.STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class VarContext(ParamContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a schemeParser.ParamContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(schemeParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)


    class ListElementsContext(ParamContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a schemeParser.ParamContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def params(self):
            return self.getTypedRuleContext(schemeParser.ParamsContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListElements" ):
                return visitor.visitListElements(self)
            else:
                return visitor.visitChildren(self)


    class Expr_paramContext(ParamContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a schemeParser.ParamContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(schemeParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_param" ):
                return visitor.visitExpr_param(self)
            else:
                return visitor.visitChildren(self)



    def param(self):

        localctx = schemeParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_param)
        try:
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                localctx = schemeParser.NumberContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.match(schemeParser.NUM)
                pass
            elif token in [7]:
                localctx = schemeParser.BooleanContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.match(schemeParser.TRUE_FALSE)
                pass
            elif token in [4]:
                localctx = schemeParser.VarContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                self.match(schemeParser.ID)
                pass
            elif token in [8]:
                localctx = schemeParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 31
                self.match(schemeParser.STRING)
                pass
            elif token in [3]:
                localctx = schemeParser.ListElementsContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 32
                self.match(schemeParser.T__2)
                self.state = 33
                self.match(schemeParser.T__0)
                self.state = 34
                self.params()
                self.state = 35
                self.match(schemeParser.T__1)
                pass
            elif token in [1]:
                localctx = schemeParser.Expr_paramContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 37
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





