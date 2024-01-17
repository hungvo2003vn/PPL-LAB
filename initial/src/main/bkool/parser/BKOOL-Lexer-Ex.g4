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

//EX1 Done
// BKNETID: LETTER '.' LETTER ChuoiTuChon;

// fragment LETTER: [a-z]+;
// fragment DIGIT: [0-9]+;
// fragment ChuoiTuChon: [a-z0-9._]? [a-z0-9._]? [a-z0-9._]? [a-z0-9._]? [a-z0-9_] ;

//EX2 Done
// Ipv4_address: '0' | (DHEAD '.' DIGIT '.' DIGIT'.' DIGIT);
// fragment DIGIT: '0' | ([1-9] [0-9]? [0-9]?);
// fragment DHEAD: [1-9] [0-9]? [0-9]?;

//Ex3 Done
// PHP_INT: '0' | [1-9] [0-9]* ('_'[0-9]+)* {self.text = self.text.replace("_", "")};

//Ex4 Done
// SHEXA: [02468] | [1-9] [0-9A-Fa-f]* [02468aceACE] ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;