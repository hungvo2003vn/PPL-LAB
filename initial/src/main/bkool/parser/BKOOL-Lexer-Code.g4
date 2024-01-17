grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}
// Use ANTLR to write regular expressions describing 
// Pascal strings are made up of a sequence of characters between single quotes: 'string'. 
// The single quote itself can appear as two single quotes back to back in a string: 'isn''t'.


program:  EOF;

//Ex1
// IDENTIFIER: [a-z] [a-z0-9]*; 

//Ex2
// NUMBER: (NUMBER1 | NUMBER2); 
// fragment NUMBER1: [0-9]+ '.' ([0-9]'e''-')* [0-9]+;
// fragment NUMBER2: [0-9]+ 'e' ('-')* [0-9]+;

//Ex3
STRING: '\'' (~'\'' | '\'\'')* '\'';
// // STRING: [SQUOTE] (~[SQUOTE] | [DQUOTE])* [SQUOTE];
// fragment SQUOTE: '\'';
// fragment DQUOTE: '\'\'';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;