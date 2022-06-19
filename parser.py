from ast import Constant, ErrorStatement, Expression, ExpressionStatement, InfixExpression, PrefixExpression, Program, Statement, Variable
from operator import truediv
from lexer import Lexer
from token import TokenType, Token

LOWEST = 0
EQUALS = 0
SUM = 1
PRODUCT = 2
PREFIX = 3

precedences = {
    TokenType.EQUAL: EQUALS,
    TokenType.PLUS: SUM,
    TokenType.MINUS: SUM,
    TokenType.MULT: PRODUCT,
    TokenType.DIV: PRODUCT,
}

class Parser:
    def __init__(self, lexer : Lexer) -> None:
        self.lexer = lexer
        self.current = Token(TokenType.EOF, "")
        self.peek = Token(TokenType.EOF, "")
        self.next_token()
        self.next_token()
        self.program = Program([])
        self.prefixFn = {}
        self.prefixFn.update({TokenType.VARIABLE: self.parse_variable})
        self.prefixFn.update({TokenType.NUMBER: self.parse_constant})
        self.prefixFn.update({TokenType.MINUS: self.parse_prefix_expression})
        self.prefixFn.update({TokenType.LPAREN: self.parse_grouped_expression})
        self.infixFn = dict()
        self.infixFn.update({TokenType.PLUS: self.parse_infix_expression})
        self.infixFn.update({TokenType.MINUS: self.parse_infix_expression})
        self.infixFn.update({TokenType.DIV: self.parse_infix_expression})
        self.infixFn.update({TokenType.MULT: self.parse_infix_expression})
    def next_token(self) -> None:
        self.current = self.peek
        self.peek = self.lexer.next_token()
    def current_is(self, ttype: TokenType) -> bool:
        return self.current.ttype is ttype
    def peek_is(self, ttype: TokenType) -> bool:
        return self.peek.ttype is ttype
    def parse(self) -> Program:
        while not self.current_is(TokenType.EOF):
            stmt = self.parse_statement()
            if not stmt is None:
                self.program.statements.append(stmt)
            self.next_token()
        return self.program
    def parse_statement(self) -> Statement:
        return self.parse_expr_statement()
    def parse_expr_statement(self) -> Statement:
        expr_stmt = ExpressionStatement(self.current, None, None)
        expr_stmt.left = self.parse_expression(LOWEST)
        if (self.expect_peek(TokenType.EQUAL)):
            self.next_token()
            expr_stmt.right = self.parse_expression(LOWEST)
        else:
            return ErrorStatement(self.current, "Expected '=' after expression!")
        return expr_stmt
    def peek_precedence(self) -> int:
        precedence = precedences.get(self.peek.ttype, None)
        if precedence is None:
            return LOWEST
        else:
            return precedence
    def current_precedence(self) -> int:
        precedence = precedences.get(self.current.ttype, None)
        if precedence is None:
            return LOWEST
        else:
            return precedence
    def parse_expression(self, precedence: int):
        prefix = self.prefixFn.get(self.current.ttype, None)
        if prefix is None:
            return None
        left = prefix()
        while not self.peek_is(TokenType.EQUAL) and precedence < self.peek_precedence():
            infix = self.infixFn.get(self.peek.ttype, None)
            if infix is None:
                return left
            self.next_token()
            left = infix(left) 
        return left
    def parse_prefix_expression(self):
        expr = PrefixExpression(self.current.ttype, self.current.lexeme, None)
        self.next_token()
        expr.right = self.parse_expression(PREFIX)
        return expr
    
    def expect_peek(self, ttype : TokenType) -> bool:
        if self.peek_is(ttype):
            self.next_token()
            return True
        else:
            return False

    def parse_infix_expression(self, left : Expression):
        expr = InfixExpression(self.current, self.current.lexeme, left, None)
        precedence = self.current_precedence()
        self.next_token()
        expr.right = self.parse_expression(precedence)
        return expr

    def parse_variable(self):
        return Variable(self.current)
    def parse_constant(self):
        return Constant(self.current, int(self.current.lexeme))
    def parse_grouped_expression(self):
        self.next_token()
        expr = self.parse_expression(LOWEST)
        if not self.expect_peek(TokenType.RPAREN):
            return None
        return expr