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

/* Ex1 */ // Done
// program: list_declared EOF;

// list_declared: declared list_declared | declared;
// declared:  funcdecl | vardecl;

// /* variables declaration */
// vardecl: 'vardecl' ;    

// /* function declaration */
// funcdecl: 'funcdecl' ;

// WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

// ERROR_CHAR: . {raise ErrorToken(self.text)};
/////////////////////////////////////////////////////////////////////////////

/* Ex2 */ //Done
// program: list_declared EOF;

// list_declared: declared list_declared | declared;
// declared:  funcdecl | vardecl SEMICLON;

// /* variables declaration */
// vardecl: prim_type list_ID;
// list_ID: ID COMMA list_ID | ID;

// /* function declaration */
// funcdecl: prim_type ID LPARENT parameter_list? RPARENT body;
// parameter_list: vardecl SEMICLON parameter_list | vardecl;
// body: 'body';

// /* keywords */
// INT: 'int';
// FLOAT: 'float';
// SEMICLON: ';';
// COMMA: ',';
// LPARENT: '(';
// RPARENT: ')';

// /* Identifier */
// ID: [a-zA-Z]+;
// prim_type: INT | FLOAT;

// WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

// ERROR_CHAR: . {raise ErrorToken(self.text)};
/////////////////////////////////////////////////////////////////////////////

/* Ex3 */ //Done
// program: list_declared EOF;

// list_declared: declared list_declared | declared;
// declared:  funcdecl | vardecl SEMICLON;

// /* variables declaration */
// vardecl: prim_type list_ID;
// list_ID: ID COMMA list_ID | ID;

// /* function declaration */
// funcdecl: prim_type ID LPARENT parameter_list? RPARENT body;
// parameter_list: vardecl SEMICLON parameter_list | vardecl;
// body: LCURL statement_list? RCURL;

// /* statement */
// statement_list: statement statement_list | statement;
// statement: (declaration_statement | assignment_statement 
// 			| call_statement | return_statement
// ) SEMICLON;

// declaration_statement: vardecl;
// assignment_statement: ID ASSIGN expression;
// call_statement: ID LPARENT expression_list? RPARENT;
// return_statement: RETURN expression;

// /* expression */
// expression_list: expression COMMA expression_list | expression;
// expression: 'expr';

// /* keywords */
// INT: 'int';
// FLOAT: 'float';
// SEMICLON: ';';
// COMMA: ',';
// LPARENT: '(';
// RPARENT: ')';
// ASSIGN: '=';
// RETURN: 'return';
// LCURL: '{';
// RCURL: '}';

// /* Identifier */
// ID: [a-zA-Z]+;
// prim_type: INT | FLOAT;

// WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

// ERROR_CHAR: . {raise ErrorToken(self.text)};
/////////////////////////////////////////////////////////////////////////////

/* Ex4 */ //Done
// program: list_declared EOF;

// list_declared: declared list_declared | declared;
// declared:  funcdecl | vardecl SEMICLON;

// /* variables declaration */
// vardecl: prim_type list_ID;
// list_ID: ID COMMA list_ID | ID;

// /* function declaration */
// funcdecl: prim_type ID LPARENT parameter_list? RPARENT body;
// parameter_list: vardecl SEMICLON parameter_list | vardecl;
// body: LCURL statement_list? RCURL;

// /* statement */
// statement_list: statement statement_list | statement;
// statement: (declaration_statement | assignment_statement 
// 			| call_statement | return_statement
// ) SEMICLON;

// declaration_statement: vardecl;
// assignment_statement: ID ASSIGN expression;
// call_statement: ID LPARENT expression_list? RPARENT;
// return_statement: RETURN expression;

// /* expression */
// expression_list: expression COMMA expression_list | expression;
// expression: expression1 ADD expression | expression1;
// expression1: expression1 SUB expression1 | expression2;
// expression2: expression2 (MUL | DIV) operands | operands;
// operands: literal | ID | call_statement | LPARENT expression RPARENT;
// literal: NUMBER_LIT;

// /* keywords */
// INT: 'int';
// FLOAT: 'float';
// SEMICLON: ';';
// COMMA: ',';
// LPARENT: '(';
// RPARENT: ')';
// ASSIGN: '=';
// RETURN: 'return';
// LCURL: '{';
// RCURL: '}';
// ADD: '+';
// SUB: '-';
// MUL: '*';
// DIV: '/';

// /* Identifier */
// ID: [a-zA-Z]+;
// prim_type: INT | FLOAT;

// /* Number */
// NUMBER_LIT: INT_LIT | FLOAT_LIT;
// fragment INT_LIT: '0' | [1-9] [0-9]*;
// fragment FRACT_LIT: [0-9]+;
// fragment FLOAT_LIT: INT_LIT '.' FRACT_LIT;

// WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

// ERROR_CHAR: . {raise ErrorToken(self.text)};
/////////////////////////////////////////////////////////////////////////////

/* Ex5 */ //Done
/*
	Change grammar BKOOL to BKIT
	Change fileName BKOOL.g4 to BKIT.g4 (change the name path in run.py too!)
	Rename checkversion in BKITLexer.py, BKITParser.py from "4.9.2" -> "4.8" 
 */
// program: list_declared EOF;

// list_declared: declared list_declared | declared;
// declared: statement SEMICLON;

// /* statement */
// statement: ID ASSIGN expression;

// /* expression */
// expression_list: expression COMMA expression_list | expression;
// expression: expression1 DQUES expression | expression1;
// expression1: expression2 (ADD | SUB) expression1 | expression2;
// expression2: expression2 (MUL | DIV | MOD) expression3 | expression3;
// expression3: expression3 DOT expression4 | expression4;
// expression4: operands DSTAR expression4 | operands;
// operands: literal | ID | LPARENT expression RPARENT;
// literal: NUMBER_LIT | STRING_LIT | array_literal;

// /* keywords */
// INT: 'int';
// FLOAT: 'float';
// SEMICLON: ';';
// COMMA: ',';
// LPARENT: '(';
// RPARENT: ')';
// ASSIGN: '=';
// ADD: '+';
// SUB: '-';
// MUL: '*';
// DIV: '/';
// MOD: '%';
// ARRAY: 'array';
// ARROW: '=>';
// DSTAR: '**';
// DQUES: '??';
// DOT: '.';

// /* Identifier */
// ID: [a-zA-Z] [a-zA-Z0-9]*;

// /* array */
// array_literal: index_array | assoc_array;
// index_array: ARRAY LPARENT expression_list? RPARENT;
// assoc_array: ARRAY LPARENT pair_name_list? RPARENT;
// pair_name_list: pair_name COMMA pair_name_list | pair_name;
// pair_name: ID ARROW expression;

// /* string */
// STRING_LIT: ["] [.]*? ["];

// /* Number */
// NUMBER_LIT: INT_LIT | FLOAT_LIT;
// fragment INT_LIT: '0' | [1-9] [0-9]*;
// fragment FRACT_LIT: [0-9]+;
// fragment FLOAT_LIT: INT_LIT '.' FRACT_LIT;

// WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

// ERROR_CHAR: . {raise ErrorToken(self.text)};