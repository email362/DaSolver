from token import TokenType, Token

class Lexer:
    def __init__(self, input : str) -> None:
        self.input = input
        self.start = 0
        self.forward = 0
        self.clean_input()
        self.ch = ' '
        self.read_char()
        self.err_msg = ""
    def clean_input(self):
        fix = False
        i = 0
        while not fix:
            fix = True
            for i, x in enumerate(self.input):
                if x.isdigit() and i+1 < len(self.input) and (self.input[i+1].isalpha() or self.input[i+1] == '('):
                    self.input = self.input[:i+1] + '*' + self.input[i+1:]
                    fix = False
                    break
    def read_char(self):
        if self.forward >= len(self.input):
            self.ch = '\0'
        else:
            self.ch = self.input[self.forward]
        self.start = self.forward
        self.forward += 1
    def skip_whitespace(self):
        while self.ch == ' ' or self.ch == '\t' or self.ch == '\n' or self.ch == '\r':
            self.read_char()
    def make_simple_token(self,ttype : TokenType, lexeme : str) -> Token:
        return Token(ttype, lexeme)
    def peek_char(self) -> chr:
        if self.forward >= len(self.input):
            return '\0'
        return self.input[self.forward]
    def read_number(self) -> str:
        start = self.start
        while self.ch.isdigit():
            self.read_char()
        return self.input[start:self.start]
    def match(self, ch : chr) -> bool:
        if ch == self.peek_char():
            self.read_char()
            return True
        return False
    def next_token(self) -> Token:
        token = Token(TokenType.ERR, "err")
        self.skip_whitespace()
        if self.ch == '+':
            token = self.make_simple_token(TokenType.PLUS, '+')
        elif self.ch == '-':
            token = self.make_simple_token(TokenType.MINUS, '-')
        elif self.ch == '*':
            token = self.make_simple_token(TokenType.MULT, '*')
        elif self.ch == '/':
            token = self.make_simple_token(TokenType.DIV, '/')
        elif self.ch == '(':
            token = self.make_simple_token(TokenType.LPAREN, '(')
        elif self.ch == ')':
            token = self.make_simple_token(TokenType.RPAREN, ')')
        elif self.ch == '=':
            token = self.make_simple_token(TokenType.EQUAL, '=')
        elif self.ch == '\0':
            token = self.make_simple_token(TokenType.EOF, self.ch)
        elif self.ch.isalpha():
            token = self.make_simple_token(TokenType.VARIABLE, self.ch)    
        else:
            if self.ch.isdigit():
                num = self.read_number()
                return self.make_simple_token(TokenType.NUMBER, num)
            token = self.make_simple_token(TokenType.ERR, self.ch)
            self.err_msg = "Unrecognized Character"
            if self.ch == '.' and self.start > 0 and self.input[self.start-1].isdigit():
                self.err_msg = " Real numbers are not supported!"
        if token.ttype is TokenType.ERR:
            err_prompt : str = f"Error on [1:{self.start+1}]: "
            print(f'{err_prompt}{self.input}')
            print("^".rjust(len(err_prompt) + self.start+1))
            print("|-".rjust(len(err_prompt) + self.start+2), end="")
            print(self.err_msg)
        self.read_char()
        return token