#!/usr/bin/env python

import re
from jacktokenizer import JackTokenizer
import File_


class CompilationEngine:
    def __init__(self, infile, XMLResultFilePath):
        self._tokenizer = JackTokenizer(infile)
        self._tokenizer._cleanCode()
        self._XMLResultStr = ''
        self._ident = '' #identation
        comParse = self.CompileClass()
        if comParse == False:
            print "Invalid parse"
        File_.make_File_From_String_(self._XMLResultStr, XMLResultFilePath)

    def inc_ident(self):
        self._ident+='  '

    def dec_ident(self):
        self._ident =self._ident[:-2]

    def CompileClass(self):
        self._tokenizer._getNextTocken()
        # expect class
        if self._tokenizer._current_token != "class":
            return False
        else:
            self._insert("<class>\n")

        self.inc_ident()
        self._insert(self._tokenizer.printToken())
        self._tokenizer._getNextTocken()
        # expect class name
        if not self._tokenizer.identifier():
            return False
        self._insert(self._tokenizer.printToken())
        self._tokenizer._getNextTocken()
        # expect {
        if self._tokenizer.symbol() != "{":
            return False
        self._insert(self._tokenizer.printToken())

        self._tokenizer._getNextTocken()
        # check if there are any field var declarations
        while self._tokenizer.keyWord() in ("static", "field"):
            self.CompileClassVarDec()

        while self._tokenizer.keyWord() in ("constructor", "function", "method"):
            self.CompileSubroutine()

        # expect }
        if self._tokenizer.symbol() != "}":
            return False

        self._insert(self._tokenizer.printToken())
        self.dec_ident()
        self.dec_ident()
        self._insert("</class>\n")

    def CompileClassVarDec(self):
        """Compiles a static declaration or a field declaration."""
        self._insert("<classVarDec>\n")
        self.inc_ident()
        if self._tokenizer.keyWord() not in ("static", "field"):
            return False

        self._insert(self._tokenizer.printToken())

        self._tokenizer._getNextTocken()
        # expect var type
        if not self._tokenizer.identifier() and not self._tokenizer.keyWord() in ("int", "char", "boolean"):
            return False

        self._insert(self._tokenizer.printToken())

        self._tokenizer._getNextTocken()
        # expect var name
        if not self._tokenizer.identifier():
            return False

        self._insert(self._tokenizer.printToken())

        self._tokenizer._getNextTocken()
        # check for ,varname
        while self._tokenizer.symbol() == ",":
            self._insert(self._tokenizer.printToken())

            self._tokenizer._getNextTocken()
            # expect identifier
            if not self._tokenizer.identifier():
                return False

            self._insert(self._tokenizer.printToken())
            self._tokenizer._getNextTocken()

        if not self._tokenizer.symbol() == ";":
            return False

        self._insert(self._tokenizer.printToken())

        self._tokenizer._getNextTocken()
        self.dec_ident()
        self._insert("</classVarDec>\n")

    def CompileSubroutine(self):
        """Compiles a complete method, function, or constructor."""
        self._insert("<subroutineDec>\n")
        self.inc_ident()
        # expecting class ctor, function or method
        if self._tokenizer.keyWord() not in ("constructor", "function", "method"):
            return False
        self._insert(self._tokenizer.printToken())

        self._tokenizer._getNextTocken()
        # expecting func return type
        if not self._tokenizer.identifier() and self._tokenizer.keyWord() not in ("void", "int", "char", "boolean"):
            return False
        self._insert(self._tokenizer.printToken())

        self._tokenizer._getNextTocken()
        # expecting function name
        if not self._tokenizer.identifier():
            return False
        self._insert(self._tokenizer.printToken())

        self._tokenizer._getNextTocken()
        # expecting ( symbol
        if self._tokenizer.symbol() != "(":
            return False

        self._insert(self._tokenizer.printToken())
        self._tokenizer._getNextTocken()
        # check for parameter list

        self._insert("<parameterList>\n")
        self.inc_ident()
        self.CompileParameterList()
        self.dec_ident()
        self._insert("</parameterList>\n")



        # expecting ) symbol
        if self._tokenizer.symbol() != ")":
            return False

        self._insert(self._tokenizer.printToken())
        self._insert("<subroutineBody>\n")
        self.inc_ident()
        self._tokenizer._getNextTocken()
        if self._tokenizer.symbol() != "{":
            return False

        self._insert(self._tokenizer.printToken())

        # checking for var declarations
        self._tokenizer._getNextTocken()
        while self._tokenizer.keyWord() == "var":
            self.CompileVarDec()

        # check for statements
        while self._tokenizer.keyWord() in ("let", "if", "while", "do", "return"):
            self.CompileStatements()

            # expecting } to end subroutine
        if self._tokenizer.symbol() != "}":
            return False

        self._insert(self._tokenizer.printToken())
        self._tokenizer._getNextTocken()
        self.dec_ident()
        self._insert("</subroutineBody>\n")
        self.dec_ident()
        self._insert("</subroutineDec>\n")

    def CompileParameterList(self):

        """Compiles a (possibly empty) parameter list, not including the enclosing '()'."""
        
       
        if self._tokenizer.keyWord() not in ("void", "int", "char", "boolean") and not self._tokenizer.identifier():
            return False

        self._insert(self._tokenizer.printToken())

        self._tokenizer._getNextTocken()
        # expecting var name
        if not self._tokenizer.identifier():
            return False

        self._insert(self._tokenizer.printToken())

        self._tokenizer._getNextTocken()
        while self._tokenizer.symbol() == ",":
            self._insert(self._tokenizer.printToken())

            self._tokenizer._getNextTocken()
            # expect var type
            if self._tokenizer.keyWord() not in ("int", "char", "boolean") and not self._tokenizer.identifier():
                return False

            self._insert(self._tokenizer.printToken())

            self._tokenizer._getNextTocken()
            # expect var name
            if not self._tokenizer.identifier():
                return False

            self._insert(self._tokenizer.printToken())

            self._tokenizer._getNextTocken()


    def CompileVarDec(self):
        """Compiles a var declaration."""
        self._insert("<varDec>\n")
        self.inc_ident()
        # expecting var keyword
        if self._tokenizer.keyWord() != "var":
            return False

        self._insert(self._tokenizer.printToken())

        self._tokenizer._getNextTocken()
        # expect var type
        if self._tokenizer.keyWord() not in ("int", "char", "boolean") and not self._tokenizer.identifier():
            return False

        self._insert(self._tokenizer.printToken())

        self._tokenizer._getNextTocken()
        # expect var name
        if self._tokenizer.tokenType() != JackTokenizer.Identifier:
            return False

        self._insert(self._tokenizer.printToken())

        self._tokenizer._getNextTocken()
        while self._tokenizer.symbol() == ",":
            self._insert(self._tokenizer.printToken())

            self._tokenizer._getNextTocken()
            # expect var name
            if not self._tokenizer.identifier():
                return False
            self._insert(self._tokenizer.printToken())

            self._tokenizer._getNextTocken()

        # expect ;
        if self._tokenizer.symbol() != ";":
            return False

        self._insert(self._tokenizer.printToken())

        self._tokenizer._getNextTocken()
        self.dec_ident()
        self._insert("</varDec>\n")

    def CompileStatements(self):
        """Compiles a sequence of statements, not including the enclosing '{}'."""
        self._insert("<statements>\n")
        self.inc_ident()
        while self._tokenizer.keyWord() in ("let", "if", "while", "do", "return"):
            if self._tokenizer.keyWord() == "let":
                self.CompileLet()
            elif self._tokenizer.keyWord() == "if":
                self.CompileIf()
            elif self._tokenizer.keyWord() == "while":
                self.CompileWhile()
            elif self._tokenizer.keyWord() == "do":
                self.CompileDo()
            elif self._tokenizer.keyWord() == "return":
                self.CompileReturn()
                # TODO is this right?
                break
        self.dec_ident()
        self._insert("</statements>\n")

    def CompileDo(self):
        """Compiles a do statement."""
        self._insert("<doStatement>\n")
        self.inc_ident()
        if self._tokenizer.keyWord() != "do":
            return False

        self._insert(self._tokenizer.printToken())

        self._tokenizer._getNextTocken()
        
        # expecting subroutine call
        self.CompileSubroutineCall()

        # expecting ;
        if self._tokenizer.symbol() != ";":
            return False

        self._insert(self._tokenizer.printToken())

        self._tokenizer._getNextTocken()
        self.dec_ident()
        self._insert("</doStatement>\n")

    def CompileLet(self):
        """Compiles a let statement."""
        self._insert("<letStatement>\n")
        self.inc_ident()
        if self._tokenizer.keyWord() != "let":
            return False

        self._insert(self._tokenizer.printToken())

        self._tokenizer._getNextTocken()
        
        # expect identifier
        if not self._tokenizer.identifier():
            return False

        self._insert(self._tokenizer.printToken())

        self._tokenizer._getNextTocken()


        if self._tokenizer.symbol() == "[":
            # array access
            self._insert(self._tokenizer.printToken())
            self._tokenizer._getNextTocken()
            # expect expresson
            self.CompileExpression()

            # expect closing ]
            if self._tokenizer.symbol() != "]":
                return False

            self._insert(self._tokenizer.printToken())

            self._tokenizer._getNextTocken()
        if self._tokenizer.symbol() != "=":
            # expect =
            return False

        self._insert(self._tokenizer.printToken())

        self._tokenizer._getNextTocken()
        # expecting expression
        self.CompileExpression()

        if self._tokenizer.symbol() != ";":
            return False

        self._insert(self._tokenizer.printToken())

        self._tokenizer._getNextTocken()
        self.dec_ident()
        self._insert("</letStatement>\n")

    def CompileWhile(self):
        """Compiles a while statement."""
        self._insert("<whileStatement>\n")
        self.inc_ident()
        if self._tokenizer.keyWord() != "while":
            return False

        self._insert(self._tokenizer.printToken())

        self._tokenizer._getNextTocken()
        # expext (
        if self._tokenizer.symbol() != "(":
            return False

        self._insert(self._tokenizer.printToken())

        self._tokenizer._getNextTocken()
        self.CompileExpression()

        # expext )
        if self._tokenizer.symbol() != ")":
            return False

        self._insert(self._tokenizer.printToken())

        self._tokenizer._getNextTocken()
        # expext {
        if self._tokenizer.symbol() != "{":
            return False

        self._insert(self._tokenizer.printToken())

        self._tokenizer._getNextTocken()
        self.CompileStatements()

        # expect }
        if self._tokenizer.symbol() != "}":
            return False

        self._insert(self._tokenizer.printToken())

        self._tokenizer._getNextTocken()
        self.dec_ident()
        self._insert("</whileStatement>\n")

    def CompileReturn(self):
        """Compiles a return statement."""
        self._insert("<returnStatement>\n")
        self.inc_ident()
        if self._tokenizer.keyWord() != "return":
            return False

        self._insert(self._tokenizer.printToken())

        self._tokenizer._getNextTocken()

        if self._tokenizer.symbol() != ";":
            # expecting expression
            self.CompileExpression()

        if self._tokenizer.symbol() != ";":
            # expecting ;
            return False

        self._insert(self._tokenizer.printToken())

        self._tokenizer._getNextTocken()
        self.dec_ident()
        self._insert("</returnStatement>\n")

    def CompileIf(self):
        """Compiles an if statement, possible with a trailing else clause."""
        self._insert("<ifStatement>\n")
        self.inc_ident()
        if self._tokenizer.keyWord() != "if":
            return False

        self._insert(self._tokenizer.printToken())

        self._tokenizer._getNextTocken()

        # expect (
        if self._tokenizer.symbol() != "(":
            return False

        self._insert(self._tokenizer.printToken())

        self._tokenizer._getNextTocken()
        self.CompileExpression()

        # expect )
        if self._tokenizer.symbol() != ")":
            return False

        self._insert(self._tokenizer.printToken())

        self._tokenizer._getNextTocken()
        # expect {
        if self._tokenizer.symbol() != "{":
            return False

        self._insert(self._tokenizer.printToken())

        self._tokenizer._getNextTocken()

        self.CompileStatements()

        # expect }
        if self._tokenizer.symbol() != "}":
            return False

        self._insert(self._tokenizer.printToken())

        self._tokenizer._getNextTocken()

        if self._tokenizer.keyWord() == "else":
            self._insert(self._tokenizer.printToken())
            self._tokenizer._getNextTocken()
            if self._tokenizer.symbol() != "{":
                return False
            self._insert(self._tokenizer.printToken())
            self._tokenizer._getNextTocken()
            self.CompileStatements()
            if self._tokenizer.symbol() != "}":
                return False
            self._insert(self._tokenizer.printToken())
            self._tokenizer._getNextTocken()
        self.dec_ident()
        self._insert("</ifStatement>\n")

    def CompileExpression(self):
        """Compiles an expression."""
        self._insert("<expression>\n")
        self.inc_ident()
        self.CompileTerm()
        # (op term)*
        while self._tokenizer.symbol() in ("+", "-", "*", "/", "&", "|", "<", ">", "="):
            self._insert(self._tokenizer.printToken())
            self._tokenizer._getNextTocken()
            self.CompileTerm()
        self.dec_ident()
        self._insert("</expression>\n")

    def CompileTerm(self):
        """Compiles a term."""
        self._insert("<term>\n")
        self.inc_ident()
        thisisterm = False

        if self._tokenizer.intVal():  # integer constant
            thisisterm = True
            self._insert(self._tokenizer.printToken())

        elif self._tokenizer.stringVal():  # string constant
            thisisterm = True
            self._insert(self._tokenizer.printToken())

        elif self._tokenizer.keyWord():  # keyword constant
            keyterm = self._tokenizer.keyWord()

            # can only be true, false, null, this
            if keyterm not in ("true", "false", "null", "this"):
                return False

            thisisterm = True
            self._insert(self._tokenizer.printToken())

        elif self._tokenizer.symbol() == "(":
            # check for (expression)
            self._insert(self._tokenizer.printToken())

            self._tokenizer._getNextTocken()
            self.CompileExpression()

            if self._tokenizer.symbol() != ")":
                return False

            thisisterm = True
            self._insert(self._tokenizer.printToken())

        elif self._tokenizer.symbol() in ("-", "~"):
            # expect term
            self._insert(self._tokenizer.printToken())
            self._tokenizer._getNextTocken()

            self.CompileTerm()

        elif self._tokenizer.identifier():  # variable name
            # lookahead checking for array access signs or subroutine calls sign
            self._insert(self._tokenizer.printToken())
            self._tokenizer._getNextTocken()

            if self._tokenizer.symbol() == "[":
                # array access
                self._insert(self._tokenizer.printToken())
                self._tokenizer._getNextTocken()
                self.CompileExpression()

                if self._tokenizer.symbol() != "]":
                    return False

                thisisterm = True
                self._insert(self._tokenizer.printToken())

            elif self._tokenizer.symbol() == "(":
                # direct subroutine call
                self._insert(self._tokenizer.printToken())

                self._tokenizer._getNextTocken()
                self.CompileExpressionList()
                self._tokenizer._getNextTocken()

                # expect ending )
                if self._tokenizer.symbol() != ")":
                    return False

                thisisterm = True
                self._insert(self._tokenizer.printToken())

            elif self._tokenizer.symbol() == ".":
                # var subroutine call
                self._insert(self._tokenizer.printToken())

                self._tokenizer._getNextTocken()
                # expecting identifier
                if not self._tokenizer.identifier():
                    return False

                self._insert(self._tokenizer.printToken())

                self._tokenizer._getNextTocken()
                # expecting (
                if self._tokenizer.symbol() != "(":
                    return False

                self._insert(self._tokenizer.printToken())
                self._tokenizer._getNextTocken()
                self.CompileExpressionList()

                # expecting closing )
                if self._tokenizer.symbol() != ")":
                    return False

                thisisterm = True
                self._insert(self._tokenizer.printToken())

        if thisisterm == True:
            self._tokenizer._getNextTocken()
        self.dec_ident()
        self._insert("</term>\n")

    def CompileExpressionList(self):
        """Compiles a (possibly empty) comma-separated list of expressions."""
        self._insert("<expressionList>\n")
        self.inc_ident()
        # expression?
        self.CompileExpression()

        # (, expression)*
        while self._tokenizer.symbol() == ",":
            self._insert(self._tokenizer.printToken())

            self._tokenizer._getNextTocken()
            self.CompileExpression()
        self.dec_ident()
        self._insert("</expressionList>\n")

    def CompileSubroutineCall(self):
        """Compile a subroutine call."""
        if not self._tokenizer.identifier():
            return False

        self._insert(self._tokenizer.printToken())

        self._tokenizer._getNextTocken()
        if self._tokenizer.symbol() == "(":
            # direct func call

            self._insert(self._tokenizer.printToken())

            self._tokenizer._getNextTocken()
            self.CompileExpressionList()

            # expect ending )
            if self._tokenizer.symbol() != ")":
                return False

            self._insert(self._tokenizer.printToken())

        elif self._tokenizer.symbol() == ".":
            # method call

            self._insert(self._tokenizer.printToken())

            self._tokenizer._getNextTocken()
            # expecting identifier for method name
            if not self._tokenizer.identifier():
                return False

            self._insert(self._tokenizer.printToken())

            self._tokenizer._getNextTocken()
            # expecting (
            if self._tokenizer.symbol() != "(":
                return False

            self._insert(self._tokenizer.printToken())

            self._tokenizer._getNextTocken()
            self.CompileExpressionList()

            if self._tokenizer.symbol() != ")":
                return False
            self._insert(self._tokenizer.printToken())
        else:
            return False

        self._tokenizer._getNextTocken()

    def _insert(self, strtowrite):
        self._XMLResultStr += self._ident + strtowrite