import Comp_

def label_ (label, currentFunction):
    content = ''
    content += "// label %s\n"% label
    content += "(%s.%s)\n"%(currentFunction,label)
    return content

def goto_(label,currentFunction):
    content = ''
    content += '// go to %s\n'% label
    content += '@%s.%s\n'%(currentFunction,label)
    content += '0;JMP \n'
    return content




def if_goto_(label,currentFunction):
    content = ''
    content += '// if go to %s\n'%label
    content += '@SP\n'
    content += 'M=M-1\n'
    content += 'A=M\n'
    content += 'D=M\n'
    content += '@%s.%s\n'% (currentFunction,label)
    content += 'D;JNE\n'
    return content

def function_ (name, numLCL):
    content = ''
    content += '//Function %s %s \n' % (name, numLCL)
    content += '(%s) \n' % (name)
    a = int(numLCL)
    while(a>0):
        content += Comp_.push_const_(0)
        a -= 1
    return content

def store_callers_(segment):
    content = ''
    content += "//store_caller's %s\n" % segment
    content += '@%s\n' % segment
    content += 'D=M\n'
    content += '@SP\n'
    content += 'A=M\n'
    content += 'M=D\n'
    content += '@SP\n'
    content += 'M=M+1\n'
    return content

def call_(fooName, numOfArgs,counter):
    content = ''
    content += '// call %s %s\n'%(fooName, numOfArgs)
    returnAddress = '%s.ReturnAdress%s'%(fooName,counter)
    content += Comp_.push_const_(returnAddress)
    content += store_callers_('LCL')
    content += store_callers_('ARG')
    content += store_callers_('THIS')
    content += store_callers_('THAT')
    content += "//change arg to callee's arg\n"
    content += '@SP \n'
    content += 'D=M\n'#D=264
    content += '@%s\n'%numOfArgs#A=3
    content += 'D=D-A\n'#D=261
    content += '@5\n'
    content += 'D=D-A\n'#D=256
    content += '@ARG\n'#A=2
    content += 'M=D\n'#
    content += "//change lcl to callee's lcl\n"
    content += '@SP  \n'
    content += 'D=M\n'
    content += '@LCL\n'
    content += 'M=D\n'
    content += "//goto - function call\n"
    content += '@%s\n' % fooName
    content += '0;JMP\n'
    content += '(%s)\n' % returnAddress
    return content


def restore_callers_(segment,offset):
    content = ''
    content += "//restor_caller's %s \n" %segment
    content += '@LCL\n'
    content += 'D=M\n'
    content += '@%s\n'% offset
    content += 'A=D-A \n'
    content += 'D=M\n'
    content += '@%s\n'% segment
    content += 'M=D\n'
    return  content

def return_():
    content = ''
    content += '//Return \n'
    content += "//save return address in R14\n"
    content += '@LCL \n'#A=1
    content += 'D=M \n'#D=264
    content += '@5 \n'#A=5
    content += 'A=D-A \n'#A=259
    content += 'D=M \n'#D=R.A=4
    content += '@R14 \n'
    content += 'M=D \n'#M[14]=4
    content += "//save function computation result to the top of the stack that the caller will see\n"
    content += '@SP \n'
    content += 'M=M-1 \n'#SP->266
    content += '@0 \n'#A=0
    content += 'D=A \n'#D=0
    content += '@ARG \n'#A=2
    content += 'D=M+D \n'#D=256+0=256
    content += '@R13 \n'#A=13
    content += 'M=D \n'#M[13]<-256
    content += '@SP \n'#A=0
    content += 'A=M \n'#A=266
    content += 'D=M \n'#D=*[266]=2
    content += '@R13 \n'#A=13
    content += 'A=M \n'#A=M[13], A=256
    content += 'M=D \n'#M[256]=2
    content += "//restore caller's sp\n"
    content += '@ARG \n'
    content += 'D=M+1 \n'
    content += '@SP \n'
    content += 'M=D \n'
    content+= restore_callers_('THAT','1')
    content += restore_callers_('THIS', '2')
    content += restore_callers_('ARG', '3')
    content += restore_callers_('LCL', '4')
    content += "//jump to return address that was stored in R14\n"
    content += '@R14 \n'
    content += 'A=M \n'
    content += '1;JMP \n'
    content += '\n'
    return content