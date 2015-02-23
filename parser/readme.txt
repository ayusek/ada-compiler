Changes made to the lexer for making the parser:
1. We have removed the token Ada_Keyword from the lexer, this would be dealt in the semantic analysis stage
2. We have removed tokens for the INTEGER_TYPE and FLOAT_TYPE
3. we have commented out some reserced keywords which we could not understand the meaning of and relate to a grammar
rule. 
