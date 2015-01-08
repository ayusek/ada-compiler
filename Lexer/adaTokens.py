#Token Definitions for Ada Language - http://en.wikibooks.org/wiki/Ada_Programming/Lexical_elements#Numbers

from reserved_Tokens import *
from symbol_Tokens import * 

# List of token names.   This is always required
tokens = [
    'IDENTIFIER',
    'ARROW',
    'DOTDOT',
    'STARSTAR',
    'ASSIGNMENT',
    'NOTEQUAL',
    'GREATEREQ',
    'LESSEQ',
    'LESSLESS',
    'MOREMORE',
    'LESSMORE',
    'STRING',
    'CHAR'
] + list(reserved.values())

#Regular Expressions for Compound Delimiters
t_ARROW = r'=>'
t_DOTDOT = r'\.\.'
t_STARSTAR = r'\*\*'
t_ASSIGNMENT = r':='
t_NOTEQUAL = r'/='
t_GREATEREQ = r'>='
t_LESSEQ = r'<='
t_LESSLESS = r'<<'
t_MOREMORE = r'>>'
t_LESSMORE = r'<>'

#Regular expression rules for simple tokens - reference taken from http://en.wikibooks.org/wiki/Ada_Programming/Lexical_elements#Numbers

#Regular Expression Rules for identifiers
def t_IDENTIFIER(t):
    r'[A-Za-z](_?[A-Za-z0-9])*'
    t.type=reserved.get(t.value,'IDENTIFIER') #giving reserved words a higher priority
    return t

def t_CHAR(t):
    r'^\'.\'$'  #Because in python dot matches any character except newline
    return t

def t_STRING(t):
    r'\"((\"\")|[^"])*\"' #Strings start and end with " only
    
    return t

#single character literals used as Operators or Delimiters
literals = "&\'()*+,-./:;<=>"


#The below definitions are not to be added to Tokens list.
# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    #Returns nothing

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

def t_comment(t):
    r'--.*'
    #Returns nothing... Ignores the comment

# Error handling rule
def t_error(t):
    print("Line:" + str( t.lineno) + "Illegal character '%s' found"% t.value[0])
    t.lexer.skip(1)
