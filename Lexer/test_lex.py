# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
tokens = (
   'NUMBER',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
)

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
#lexer = lex.lex(debug=1)	#for debugging

#if __name__ == '__main__':	#use for command line or file input
#     lex.runmain()

# Test it out
data = '''
13 * 45 / 10
  + -20 *2
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: break      # No more input
    print tok			# Output is of the form LexToken(Token Type,Value of token,Present line number,Start position of 1st character of this token)
#By default, t.type is set to the name following the t_ prefix.The action function can modify the contents of the LexToken object as appropriate. However, when it is done, the resulting token should be returned.
#Internally, lex.py uses the re module to do its patten matching. When building the master regular expression, rules are added in the following order:

#All tokens defined by functions are added in the same order as they appear in the lexer file.
#Tokens defined by strings are added next by sorting them in order of decreasing regular expression length (longer expressions are added first).
#To handle reserved words, you should write a single rule to match an identifier and do a special name lookup in a function like this:

#reserved = {
#   'if' : 'IF',
#   'then' : 'THEN',
#   'else' : 'ELSE',
#   'while' : 'WHILE',
#   ...
#}

#tokens = ['LPAREN','RPAREN',...,'ID'] + list(reserved.values())

#def t_ID(t):
#    r'[a-zA-Z_][a-zA-Z_0-9]*'
#    t.type = reserved.get(t.value,'ID')    # Check for reserved words
#    return t

#Note: You should avoid writing individual rules for reserved words. For example, if you write rules like this,

#t_FOR   = r'for'
#t_PRINT = r'print'
#those rules will be triggered for identifiers that include those words as a prefix such as "forget" or "printed". This is probably not what #you want.

#To discard a token, such as a comment, simply define a token rule that returns no value. For example:
#def t_COMMENT(t):
#    r'\#.*'
#    pass
    # No return value. Token discarded
#Alternatively, you can include the prefix "ignore_" in the token declaration to force a token to be ignored. For example:
#t_ignore_COMMENT = r'\#.*'


