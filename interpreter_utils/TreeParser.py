from copy import copy
from antlr4 import *

from interpreter_utils.TreeShow import TreeVisitor
from interpreter_utils.schemeLexer import schemeLexer
from interpreter_utils.schemeParser import schemeParser
from interpreter_utils.schemeVisitor import schemeVisitor


def correctOutputExpression(expr):
    """Print Expected Output Expression"""
    if type(expr) == bool:
        print("#t" if expr else "#f", end="")
    elif type(expr) == list:
        print(
            f"{str(expr).replace("[", "(").replace("]", ")").replace(",", "")}",
            end="",
        )
    elif type(expr) == float:
        print(f"{expr:.2f}", end="")
    else:
        print(expr, end="")


def raiseError(msg):
    """Centralized Error Message"""
    # Try-except block used to properly observe and handle implemented error checkers
    try:
        raise Exception(msg)
    except Exception as e:
        print(f"Error: {e}")
        # raise


def checkCondition(condition, msg):
    """Checks if the condition is correct."""
    if condition:
        raiseError(msg)


def checkArgumentCount(operator, args_num, expected_count):
    """Checks if the number of arguments is correct."""
    checkCondition(
        args_num != expected_count,
        f"Operator {operator}. Expected {expected_count} arguments, got {args_num}",
    )


class EvalVisitor(schemeVisitor):
    def __init__(self):
        self.default_labels = {
            "+": (lambda x, y: x + y),
            "-": (lambda x, y: x - y),
            "*": (lambda x, y: x * y),
            "/": (lambda x, y: x // y),
            "div": (lambda x, y: x / y),
            "=": (lambda x, y: x == y),
            "<>": (lambda x, y: x != y),
            ">": (lambda x, y: x > y),
            "<": (lambda x, y: x < y),
            ">=": (lambda x, y: x >= y),
            "<=": (lambda x, y: x <= y),
            "#t": 1,
            "#f": 0,
            "and": (lambda x, y: x and y),
            "or": (lambda x, y: x or y),
            "not": (lambda x: not x),
            "display": (lambda x: correctOutputExpression(x)),
            "newline": (lambda: print("\n", end="")),
            "mod": (lambda x, y: x % y),
        }
        self.func_lists = {
            "car": (lambda x: x[0]),
            "cdr": (lambda x: x[1:]),
            "null?": (lambda x: len(x) == 0),
            "cons": (lambda x, y: [x] + y),
        }
        self.var_runtime = {}
        self.func_runtime = {}
        self.stack_runtime = []

        # Linker of functions to improve modularity and readability
        self.operator_handlers = {
            **{op: self.handle_default_labels for op in self.default_labels},
            **{op: self.handle_func_lists for op in self.func_lists},
            "define": self.handle_define,
            "read": self.handle_read,
            "let": self.handle_let,
            "if": self.handle_if,
            "cond": self.handle_cond,
        }

    def visitRoot(self, ctx):
        """Visits the root node and evaluates each expression."""
        s_expr = list(ctx.getChildren())

        _ = (correctOutputExpression(self.visit(expr)) for expr in s_expr[:-1])

        if expr_sol := self.visit(s_expr[-1]) is not None:
            correctOutputExpression(expr_sol)

        print(f"{"="*20}End of the execution{"="*20}")

    def visitExpr_S(self, ctx):
        """Evaluates an S-expression."""
        # '(' , *args , ')'
        [_, *args, _] = list(ctx.getChildren())

        # The operator should always be the first parameter
        operator_node = args[0].getChild(0)
        arguments_node = list(args[0].getChildren())[1:]
        operator = operator_node.getText().lower()
        handler = self.operator_handlers.get(operator, self.handle_function_var_call)
        return handler(
            arguments_node,
            operator_node if handler == self.handle_function_var_call else operator,
        )

    def handle_default_labels(self, arguments_node, operator):
        """Default_Identifiers which are already provided by the interpreter"""
        # Visit all arguments (excluding the operator) and give them to the default operator
        lst = [self.visit(arg) for arg in arguments_node]
        return self.default_labels[operator](*lst)

    def handle_func_lists(self, arguments_node, operator):
        """Default_List_Operators to manipulate lists"""
        if operator != "cons":
            lst = self.visit(arguments_node[0])
            return self.func_lists[operator](lst)
        else:
            value = self.visit(arguments_node[0])
            lst = self.visit(arguments_node[1])
            return self.func_lists[operator](value, lst)

    def handle_define(self, arguments_node, operator):
        """DEFINE case to define a function or a Variable"""
        # ( define _ _ )
        checkCondition(
            len(arguments_node) < 2,
            f"Operator `{operator}` has too few arguments.",
        )

        [function_var_header] = list(arguments_node[0].getChildren())

        function_var_body = arguments_node[1:]

        # Function case
        if function_var_header.getText()[0] == "(":
            # ( define ( f_name *params ) ( body ... ) )

            [_, *func_header, _] = list(function_var_header.getChildren())
            func_name_params = list(func_header[0].getChildren())
            func_name = func_name_params[0].getText()
            func_params = func_name_params[1:]

            self.func_runtime[func_name] = {
                "params": [param.getText() for param in func_params],
                "body": function_var_body,
                "env": {},
            }
        # Variable case
        else:
            # ( define var_name _ )
            checkArgumentCount(f"`{operator}` as a variable", len(arguments_node), 2)
            var_name = function_var_header.getText()
            # Save the context, evaluating it when we call it
            body = function_var_body[0]
            self.var_runtime[var_name] = {"body": body, "visited": 0}

        return None

    def handle_read(self, arguments_node, operator):
        """DISPLAY case to read an expression"""
        checkArgumentCount("`read` does not have arguments", len(arguments_node), 0)
        input_taken = input(
            # "Enter expression: "
        )
        try:
            input_taken = eval(input_taken)
            return input_taken

        # Case where input evals a string
        except (SyntaxError, NameError):
            return input_taken

    def handle_let(self, arguments_node, operator):
        """LET case for a local scope"""
        """TODO: CHECK wtf is going on with this checker --> Problem laziness_aware_test_output"""
        """Let local scope case"""
        # (let ((var1 value1)   (var2 value2) ...)  *expr)

        # New variables to add to the let scope
        [var_block_node] = list(arguments_node[0].getChildren())
        [_, *var_block, _] = list(var_block_node.getChildren())

        # Unpacking all generator to have a list of list expressions
        [*let_expr_s] = [[*args_node.getChildren()] for args_node in arguments_node[1:]]

        # To add the new variables given as local variables restricted to let scope
        local_env = {}
        # Creating new local environment
        for expr_var in list(var_block[0].getChildren()):
            [var] = expr_var.getChildren()
            # Extract variable names and their corresponding evaluated values for the let scope
            [*name_body_var] = list(var.getChildren())[1].getChildren()
            # print( f"Let Checker{[v.getText() for v in name_body_var]}. NUMBER OF PARAMS = {len(name_body_var)}")
            # Check var value number of elements

            checkArgumentCount(f"`{operator}` variables", len(name_body_var), 2)

            [var_name, var_body] = name_body_var

            # In a local scope we evaluate the var immediately
            local_env[var_name.getText()] = {
                "body": self.visit(var_body),
                "visited": 1,
            }

        # Copy the actual environment to reset it when let expression is evaluated
        copy_actual_env = copy(self.var_runtime)
        self.var_runtime.update(local_env)
        let_solution = None

        # Len evaluation
        for [expr] in let_expr_s:
            # print(f"Expression len: {expr.getText()}")
            let_solution = self.visit(expr)

        self.var_runtime = copy_actual_env

        return let_solution

    def handle_if(self, arguments_node, operator):
        """Conditional IF case"""
        # Checking if construction, (cond,N1,N2) or (cond,N1)
        count_arg = len(arguments_node)
        checkCondition(
            count_arg < 2 or count_arg > 3,
            f"`{operator}` statement requires at least 2 arguments and less than 3: condition, true branch, else branch. "
            f"Got {len(arguments_node)} arguments.",
        )

        condition = self.visit(arguments_node[0])
        if condition:
            return self.visit(arguments_node[1])
        # Just evaluate if there is an else case
        else:
            return self.visit(arguments_node[2]) if count_arg > 2 else None

    def handle_cond(self, arguments_node, operator):
        """Conditional COND case"""

        # Analyse every possible condition
        for arg in arguments_node:
            # Statement node not counting ( )
            [_, statements, _] = list(list(arg.getChildren())[0].getChildren())

            # Dividing condition and *instructions
            [cond, instructions] = list(statements.getChildren())
            if cond.getText() == "else":
                return self.visit(instructions)

            # Only evaluate instructions if condition is true
            if self.visit(cond):
                return self.visit(instructions)

    def handle_function_var_call(self, arguments_node, operator_node):
        """Function/Var call case"""

        # Operator as a function defined by the program or a param function already defined

        # visitVar gives either a runtime_function, a param_function or an notFind error
        function_context = self.visit(operator_node)
        operator = operator_node.getText().lower()
        # Argument checker
        checkArgumentCount(
            operator, len(arguments_node), len(function_context["params"])
        )
        # Link args with params
        for arg, param in zip(arguments_node, function_context["params"]):
            function_context["env"][param] = self.visit(arg)

        # Add function to the stack
        self.stack_runtime.append(function_context)

        # Evaluate the body
        result = None
        for [instruction_expr] in [
            body_expr.getChildren() for body_expr in function_context["body"]
        ]:
            result = self.visit(instruction_expr)

        # Pop  the function up from the stack
        self.stack_runtime.pop()

        return result

    def visitListElements(self, ctx):
        """Processes a quoted list."""
        [_, _, children, _] = list(ctx.getChildren())
        lst = [
            s
            for child in list(children.getChildren())
            if (s := self.visit(child)) is not None
        ]
        return lst

    def visitNumber(self, ctx):
        """Processes a numeric parameter."""
        [num] = list(ctx.getChildren())
        return eval(num.getText())

    def visitBoolean(self, ctx):
        """Processes a boolean parameter."""
        [bool_label] = list(ctx.getChildren())
        return self.default_labels[bool_label.getText()]

    def visitVar(self, ctx):
        """Processes a variable or function."""
        func_var_text = ctx.getText()

        # Search at the top of the Stack
        if len(self.stack_runtime) > 0:
            if func_var_text in (s := self.stack_runtime[-1]["env"]).keys():
                return s[func_var_text]

        # Search as global var
        if func_var_text in self.var_runtime:
            if not self.var_runtime[func_var_text]["visited"]:
                self.var_runtime[func_var_text]["body"] = self.visit(
                    self.var_runtime[func_var_text]["body"]
                )
                self.var_runtime[func_var_text]["visited"] = 1
            return self.var_runtime[func_var_text]["body"]

        # Search at function definitions
        if func_var_text in self.func_runtime:
            # Copy of the function already defined in function_creation. Shallow copy aware with env compromised data
            function_context = copy(self.func_runtime[func_var_text])
            function_context["env"] = copy(self.func_runtime[func_var_text]["env"])
            return function_context

        # No func_var found
        raiseError(f"Variable/Function `{func_var_text}` not found")

    def visitString(self, ctx):
        """Processes a string parameter."""
        string = ctx.getText().replace('"', "")
        return string


def evalProgram(
    input_program="../scheme_programs/repo_main_features1.scm", show_visit_tree=0
):
    input_stream = FileStream(input_program, encoding="utf-8")

    # Create Lexer and Parser

    lexer = schemeLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = schemeParser(token_stream)

    # Generate tree analysis
    tree = parser.root()
    if parser.getNumberOfSyntaxErrors() != 0:
        print(parser.getNumberOfSyntaxErrors(), "Syntax errors")
        print(tree.toStringTree(recog=parser))
    else:
        if show_visit_tree:
            # Visit Tree
            visitor_tree = TreeVisitor()
            print("Visiting tree...")
            visitor_tree.visit(tree)
        # Evaluate Tree
        visitor_eval = EvalVisitor()
        visitor_eval.visit(tree)


evalProgram("/Users/h.gf/PycharmProjects/LISP_compiler/scheme_programs/test.scm")

# python3 scheme.py ./scheme_programs/repo_main_features1_test.scm < ./inout/input_files/repo_main_features1_test_input.txt > ./inout/output_files/repo_main_features1_test_output.txt
# diff ./inout/output_files/repo_main_features1_test_output.txt ./inout/diff_output_files/repo_main_features1_test_output.txt
# python3 scheme.py ./scheme_programs/repo_main_features2_test.scm < ./inout/input_files/repo_main_features2_test_input.txt > ./inout/output_files/repo_main_features2_test_output.txt
# diff ./inout/output_files/repo_main_features2_test_output.txt ./inout/diff_output_files/repo_main_features2_test_output.txt
# python3 scheme.py ./scheme_programs/laziness_aware_test.scm <./inout/input_files/laziness_aware_test_input.txt > ./inout/output_files/laziness_aware_test_output.txt
# diff ./inout/output_files/laziness_aware_test_output.txt ./inout/diff_output_files/laziness_aware_test_output.txt
# python3 scheme.py ./scheme_programs/scope_test.scm <./inout/input_files/scope_test_input.txt > ./inout/output_files/scope_test_output.txt
# diff ./inout/output_files/scope_test_output.txt ./inout/diff_output_files/scope_test_output.txt
# python3 scheme.py ./scheme_programs/error_checkers_test.scm <./inout/input_files/error_checkers_test_input.txt > ./inout/output_files/error_checkers_test_output.txt
# diff ./inout/output_files/error_checkers_test_output.txt ./inout/diff_output_files/error_checkers_test_output.txt

# Variables are evaluated immediately with let!
# Variables are just evaluated when it is needed with define!
