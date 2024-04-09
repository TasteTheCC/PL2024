import ply.lex as lex

# Tokens e expressoes reservadas
tokens = (
    'SELECT',
    'FROM',
    'WHERE',
    'VAR',
    'VALUE',
    'COMMA',
    'GREATER_EQ',
    'GREATER',
    'EQUALS',
    'LOWER_EQ',
    'LOWER',
)

# Definição das REGEX dos tokens
t_SELECT = r'SELECT'
t_FROM = r'FROM'
t_WHERE = r'WHERE'
t_VAR = r'\w+'
t_VALUE = r'\d+'
t_COMMA = r','
t_GREATER_EQ = r'>='
t_GREATER = r'>'
t_EQUALS = r'='
t_LOWER_EQ = r'<='
t_LOWER = r'<'


#whitespaces
t_ignore = ' \t\n'

def t_error(t):
    print(f"Wrong char {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

#TESTE
test = "SELECT id, nome, salario FROM empregados WHERE salario >= 820"
lexer.input(test)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)