from enum import Enum

class TokenType(Enum):
    ERR         = "ERR"
    EOF         = ""
    PLUS        = "+"
    MINUS       = "-"
    MULT        = "*"
    DIV         = "/"
    EQUAL       = "="
    LPAREN      = "("
    RPAREN      = ")"
    NUMBER      = "NUMBER"
    VARIABLE    = "VARIABLE"

class Token:
    def __init__(self, ttype : TokenType, lexeme : str) -> None:
        self.ttype = ttype
        self.lexeme = lexeme
    def __str__(self) -> str:
        return f"({self.ttype} : {self.lexeme})"