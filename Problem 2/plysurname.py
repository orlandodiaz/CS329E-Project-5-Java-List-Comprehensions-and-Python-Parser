tokens = ('FIRSTLINE','NAME','INTEGER')
literals = [',','.']

# Tokens
t_FIRSTLINE   = r'surname.*$'
t_NAME = r'[a-zA-Z]+'
t_INTEGER = r'\d+'



# Ignored characters
t_ignore = " \r\n"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex   # ply.lex comes from the ply folder in the PLY download.
lexer = lex.lex()
# Parsing rules

global line
line = 1
def p_start(t):
    '''start : FIRSTLINE
             | data
    '''
    global line
    if line == 1:
      print "Top 10000 Popular surnames in United States in 1990"
      line += 1

def p_data(t):
    'data : NAME "," float "," float "," INTEGER'
    print "Saw surname " + str(t[1]) +" with rank " + str(t[7])+" and percent " + str(t[3])

def p_float(t):
    'float : INTEGER "." INTEGER'
    t[0] = str(t[1]) + str(t[2]) + str(t[3])


def p_error(t):
    if t == None:
        print("Syntax error at '%s'" % t)
    else:
        print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc   # ply.yacc comes from the ply folder in the PLY download.
parser = yacc.yacc()

while True:
    try:
        s = raw_input('')
    except EOFError:
        break
    parser.parse(s)

    # To run the parser do the following in a terminal window:cat 1990.out |python plysurname.py