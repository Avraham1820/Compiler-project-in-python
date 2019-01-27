#Avraham Shaharabani 032472664
#Daniel Lictenshtat  302026059

import os
import File_



class JackTokenizer:
    _keywords = ["class", "constructor", "function", "method", "field", "static", "var", "int", "char", "boolean",
                 "void", "true", "false", "null", "this", "let", "do", "if", "else", "while", "return"]
    _symbol = ["{", "}", "(", ")", "[", "]", ".", ",", ";", "+", "-", "*", "/", "&", "|", "<", ">", "=", "~"]

    _space = ['\n','\t',' ']

    Keyword = 1
    Symbol = 2
    IntegerConstant = 3
    StringConstant = 4
    Identifier = 5

    def __init__(self, jack_file_path):
        self._jack_str = self.convertFileToString(jack_file_path)
        self._current_token = ''
        self._next_char = ''
        self._i=-1
        self._j=0
        self._numOfChars=0
        self.XML=''


    def convertFileToString(self,filePath):
        file = open(filePath, 'r')  # Open a stream to read the file
        content = file.read()  # Read from the file all the text to a var
        file.close()  # Close the stream
        return content


    def _getCurrentChar(self):
        if self._i>=0:
            return ''.join(self._jack_str[self._i: self._j])

    def _getNextChar(self):
        if (self._j  <= self._numOfChars):
            self._i += 1
            self._j += 1
            return ''.join(self._jack_str[self._i: self._j])
        else: return ''

    def _peeknextchar(self):
        self._next_char = self._getNextChar()
        self._i -= 1
        self._j -= 1
        return self._next_char

    def hasMoreTokens(self):
        #Do we have more tokens in the input?
        peekchar = self._peeknextchar()
        if peekchar == "" or peekchar == '':
            return False
        else:
            return True


    def tokenType(self):
        #Returns the type of the current token.
        if self._current_token in self._keywords:
            return self.Keyword

        if self._current_token in self._symbol:
            return self.Symbol

        if  self._current_token.isdigit():
            return self.IntegerConstant


        if self._current_token.startswith('"') and self._current_token.endswith('"'):
            return self.StringConstant


        if self._current_token!=''  and self._current_token[0].isalpha():
            return self.Identifier


    def printToken(self):
        #print self._current_token
        if self.tokenType() == JackTokenizer.Keyword:
            return "<keyword> %s </keyword>\n" % self._current_token
        elif self.tokenType() == JackTokenizer.Symbol:
            if self._current_token == "<":
                return "<symbol> &lt; </symbol>\n"
            elif self._current_token == ">":
                return "<symbol> &gt; </symbol>\n"
            elif self._current_token == "&":
                return "<symbol> &amp; </symbol>\n"
            else:
                return "<symbol> %s </symbol>\n" % self._current_token
        elif self.tokenType() == JackTokenizer.Identifier:
            return "<identifier> %s </identifier>\n" % self._current_token
        elif self.tokenType() == JackTokenizer.IntegerConstant:
            return "<integerConstant> %s </integerConstant>\n" % self._current_token
        elif self.tokenType() == JackTokenizer.StringConstant:
            return "<stringConstant> %s </stringConstant>\n" % self._current_token[1:-1]
        else:
            return "Token: %s\n" % self._current_token

    def keyWord(self):
        """Returns the keyword which is the current token."""
        if self.tokenType() == JackTokenizer.Keyword:
            return self._current_token

    def symbol(self):
        """Returns the character which is the current token."""
        if self.tokenType() == JackTokenizer.Symbol:
            return self._current_token

    def identifier(self):
        """Returns the identifier which is the current token."""
        if self.tokenType() == JackTokenizer.Identifier:
            return self._current_token

    def intVal(self):
        """Returns the integer value of the current token."""
        if self.tokenType() == JackTokenizer.IntegerConstant:
            return self._current_token

    def stringVal(self):
        """Returns the string value of the current token, without the double quotes."""
        if self.tokenType() == JackTokenizer.StringConstant:
            # skip quotes in constant
            return self._current_token[1:-1]

    def _cleanCode(self):

       n=len(self._jack_str)
       i=0
       clean=''
       while(i<n):

          while self._jack_str[i]=='/':
              if self._jack_str[i+1]=='/':
                  i=self._jack_str.find('\n',i)+1
                  clean += ' '
              elif  self._jack_str[i+1]=='*':
                  i=self._jack_str.find('*/',i)+2
              else: break
          if i<n and self._jack_str[i]=='\n':
              clean +=' '

              #clean=clean[:-1]
          if i<n and self._jack_str[i]!='\n' :
             clean+= self._jack_str[i]

          i+=1

       clean=clean.split()


       str=''
       k=0
       while(k<len(clean)):
         str+=''.join(clean[k:k+1])
         str+=' '
         k+=1
       clean =str
       self._jack_str=clean
       self._numOfChars=len(self._jack_str)
       #print self._numOfChars


    def _getNextTocken(self):
        #Gets the next token from the input and makes it the current token.
        if not self.hasMoreTokens():
            return

        self._current_token = ""
        currentchar = self._getNextChar()

        while currentchar in self._space:
            currentchar = self._getNextChar()

        while True:
            if not self.hasMoreTokens():
                return

            self._current_token += currentchar

            if self._current_token.startswith("\""):
                # matching a quoted string
                if self._peeknextchar() == "\"":
                    # matching closing quote
                    self._current_token = self._current_token + self._getNextChar()
                    return

            elif self._peeknextchar() in self._space:
                # next char is a symbol, so current is token
                return

            elif self._peeknextchar() in self._symbol:
                # next char is a symbol, so current is token
                return
            elif self._current_token in self._symbol:
                # current char is a symbol, special case, so token
                return

            currentchar = self._getNextChar()




def main_of_tockenizer(filePath):
    (jackFileName, jackFileExtension) = os.path.splitext(filePath)
    XMLPath = jackFileName + "T.xml"
    jackT = JackTokenizer(filePath)
    jackT._cleanCode()
    #print jackT._jack_str
    jackT.XML+="<tokens>\n"
    jackT._getNextTocken()
    while jackT.hasMoreTokens():
        jackT.XML += jackT.printToken()
        jackT._getNextTocken()

    jackT.XML+="</tokens>\n"
    #print jackT.XML
    File_.make_File_From_String_(jackT.XML,XMLPath)

def mainf_(fileName):
    if os.path.isfile(fileName):
        main_of_tockenizer(fileName)
    else:
        print 'The file : %s is not exsist' % fileName


    #print jtok.XML
f1='C:\XXX_Python\Jack_Parser_4.0\Jack_code\Main.jack'
f2='C:\XXX_Python\Jack_Parser_4.0\Jack_code\SquareGame.jack'
f3='C:\XXX_Python\Jack_Parser_4.0\Jack_code\Square.jack'
f4='C:\XXX_Python\Jack_Parser_4.0\Jack_code\Dictionary.jack'
f5='C:\XXX_Python\Jack_Parser_4.0\Jack_code\MainArray.jack'
#mainf_(f1)
#mainf_(f2)
#mainf_(f3)
#mainf_(f4)
#mainf_(f5)
#a =Tokenizer(x)
#a.cleanCode()
#print a._jack_str





#print a.hasMoreTokens()
#print a._getNextChar()
#print a.hasMoreTokens()
#print a._getNextChar()
#print a.hasMoreTokens()
#print a._getNextChar()
#print a.hasMoreTokens()
#print a._getNextChar()
#print a.hasMoreTokens()
#
#print a._getNextChar()
#print a._getNextChar()
#
#a._skipwholeline()
#print a._i
#
#print a._getNextChar()
#print a._getNextChar()
#print a._getNextChar()
#print a._getNextChar()
#print a._getNextChar()
#print a._getNextChar()
