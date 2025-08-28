from interpreter_utils.schemeVisitor import schemeVisitor


class TreeVisitor(schemeVisitor):

    def __init__(self):
        self.level = 0

    def identificationTree(self, text):
        print(" " * self.level + text)

    def visitExpr_S(self, ctx):
        [*params] = ctx.getChildren()

        self.identificationTree("(")
        for param in params:
            self.level += 1
            self.visit(param)
            self.level -= 1
        self.identificationTree(")")

    def visitListElements(self, ctx):
        [_, _, *params, _] = ctx.getChildren()
        self.identificationTree("'(")
        self.level += 1
        for param in params:
            self.level += 1
            self.visit(param)
            self.level -= 1
        self.level -= 1
        self.identificationTree(")")

    def visitString(self, ctx):
        string = ctx.getText().replace('"', "")
        self.identificationTree(string)

    def visitBoolean(self, ctx):
        [bool_label] = list(ctx.getChildren())
        self.identificationTree(f"{bool_label.getText()}")

    def visitNumber(self, ctx):
        [num] = list(ctx.getChildren())
        self.identificationTree(f"{num.getText()}")

    def visitVar(self, ctx):
        [var] = list(ctx.getChildren())
        self.identificationTree(f"{var.getText()}")
