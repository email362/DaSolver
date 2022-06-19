from abc import abstractmethod
from token import Token
from typing import Optional, Sequence

class AST:
    @abstractmethod
    def token_literal(self) -> str:
        pass
    @abstractmethod
    def __str__(self) -> str:
        pass

class Expression(AST):
    @abstractmethod
    def token_literal(self) -> str:
        pass
    @abstractmethod
    def __str__(self) -> str:
        pass

class Statement(AST):
    def statement_node(self) -> None:
        pass
    @abstractmethod
    def token_literal(self) -> str:
        pass
    @abstractmethod
    def __str__(self) -> str:
        pass

class Program:
    def __init__(self, statements: Sequence[Statement]) -> None:
        self.statements = statements
    def __str__(self) -> str:
        stmt_str = ""
        for stmt in self.statements:
            if not stmt is None:
                stmt_str += str(stmt) + "\n"
        return stmt_str

class Constant(AST):
    def __init__(self, token: Token, value : int) -> None:
        self.token = token
        self.value = value
    def token_literal(self) -> str:
        return self.value
    def __str__(self) -> str:
        return str(self.value)

class Variable(AST):
    def __init__(self, token: Token) -> None:
        self.token = token
    def token_literal(self) -> str:
        return self.token.lexeme
    def __str__(self) -> str:
        return self.token.lexeme

class ExpressionStatement(Statement):
    def __init__(self, token: Token, left : Expression, right: Expression) -> None:
        self.token = token
        self.left = left
        self.right = right
    def token_literal(self) -> str:
        return self.token.lexeme
    def __str__(self) -> str:
        return f'{self.left} = {self.right}'

class ErrorStatement(Statement):
    def __init__(self, token: Token, msg: str) -> None:
        self.token = token
        self.msg = msg
    def token_literal(self) -> str:
        return self.token.lexeme
    def __str__(self) -> str:
        return self.msg

class PrefixExpression(Expression):
    def __init__(self, token: Token, op: str, right : Expression) -> None:
        self.token = token
        self.op = op
        self.right = right
    def token_literal(self) -> str:
        return self.token.lexeme
    def __str__(self) -> str:
        return f'{self.op}{self.right}'

class InfixExpression(Expression):
    def __init__(self, token: Token, op: str, left: Expression, right: Expression) -> None:
        self.token = token
        self.op = op
        self.left = left
        self.right = right
    def token_literal(self) -> str:
        return self.token.lexeme
    def __str__(self) -> str:
        return f'({self.left} {self.op} {self.right})'

        