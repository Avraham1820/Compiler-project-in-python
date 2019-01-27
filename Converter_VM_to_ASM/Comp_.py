



def push_const_(offset):
    content = ''
    content += '//push_const %s\n' % offset
    content += '@%s\n'% offset
    content += 'D=A\n'
    content += '@SP\n'
    content += 'A=M\n'
    content += 'M=D\n'
    content += '@SP\n'
    content += 'M=M+1\n'
    return content

def push_tmp_(offset):
    content = ''
    content += '//push_tmp %s\n' % offset
    content += '@%s\n' % str(int(offset) + 5)
    content += 'D=M\n'
    content += '@SP\n'
    content += 'A=M\n'
    content += 'M=D\n'
    content += '@SP\n'
    content += 'M=M+1\n'
    return content

def push_ptr_(offset):
    content = ''
    content += '//push_ptr %s\n' % offset
    content += '@%s\n\n' % str(int(offset) + 3)
    content += 'D=M\n'
    content += '@SP\n'
    content += 'A=M\n'
    content += 'M=D\n'
    content += '@SP\n'
    content += 'M=M+1\n'
    return content

def push_seg_(seg, offset):
    content = ''
    content += '//push %s %s \n' % (seg ,offset)
    content += '@%s \n' % (offset)
    content += 'D=A \n'
    content += '@%s \n' % (seg)
    content += 'A=M+D \n'
    content += 'D=M \n'
    content += '@SP \n'
    content += 'A=M \n'
    content += 'M=D \n'
    content += '@SP \n'
    content += 'M=M+1 \n'
    return content



def push_static_(className, offset):
    content =  ''
    content += '//push_static %s\n' % ( offset)
    content += '@%s.%s\n'%(className, offset)
    content += 'D=M\n'
    content += '@SP\n'
    content += 'A=M\n'
    content += 'M=D\n'
    content += '@SP\n'
    content += 'M=M+1\n'
    return content

def pop_const_(offset):
    content = ''
    content += '//pop constant %s \n' % (offset)
    content += '@SP \n'
    content += 'M=M-1 \n'
    return content


def pop_static_(className, offset):
    content =  ''
    content += '//pop_static %s\n' % offset
    content += '@SP\n'
    content += 'M=M-1\n'
    content += 'A=M\n'
    content += 'D=M\n'
    content += '@%s.%s\n'%(className, offset)
    content += 'M=D\n'
    return content

def pop_ptr_(offset):
    content =  ''
    content += '//pop_pointer %s\n' % offset
    content += '@SP\n'
    content += 'AM=M-1\n'
    content += 'D=M\n'
    content += '@%s\n'%(int(offset) + 3)
    content += 'M=D\n'
    return content


def pop_temp_(offset):
    content =  ''
    content += '//pop_temp %s\n' % offset
    content += '@%s\n'%offset
    content += 'D=A\n'
    content += '@5\n'
    content += 'D=A+D\n'
    content += '@SP\n'
    content += 'A=M\n'
    content += 'M=D\n'
    content += '@SP\n'
    content += 'AM=M-1\n'
    content += 'D=M\n'
    content += 'A=A+1\n'
    content += 'A=M\n'
    content += 'M=D\n'
    return content

def pop_seg_(seg, offset):
    content =  ''
    content += '//pop_%s %s\n' % (seg, offset)
    content += '@%s\n'% offset
    content += 'D=A\n'
    content += '@%s\n'% seg
    content += 'D=M+D\n'
    content += '@SP\n'
    content += 'A=M\n'
    content += 'M=D\n'
    content += 'A=A-1\n'
    content += 'D=M \n'
    content += 'A=A+1\n'
    content += 'A=M\n'
    content += 'M=D\n'
    content += '@SP\n'
    content += 'M=M-1\n'
    return content
def or_():
    content = ''
    content += '//or \n' # push a, push b, compute a|b ,
    content +='@SP \n'  # A = SP
    content +='M=M-1 \n'  # M[SP] = M[SP-1]  like SP--
    content +='@SP \n'  # A=0
    content +='A=M \n'  # A=M[0]   to set address of SP in A
    content +='D=M \n'  # pop b to register D
    content +='@SP \n'  #
    content +='A=M-1 \n' # SP--
    content +='M=M|D \n'  # compute a|b and push to M[SP] withno inc SP++
    return content        # Why we relate the result of compute like junk so the
                          # next push value will override the compute of A|b


def not_():
    content = ''
    content += '//not \n'
    content += '@SP \n'
    content += 'A=M-1 \n'
    content += 'D=M \n'
    content += 'M=!D \n'
    return content

def and_():
    content = ''
    content += '//and \n'
    content += '@SP \n'
    content += 'M=M-1 \n'
    content += '@SP \n'
    content += 'A=M \n'
    content += 'D=M \n'
    content += '@SP \n'
    content += 'A=M-1 \n'
    content += 'M=M&D \n'
    return content


def add_sub_(OP):
    content = ''
    if OP == 'add':
        content += '//add \n'
    else:
        content += '//sub \n'
    content += '@SP \n'
    content += 'A=M-1 \n'
    content += 'D=M \n'
    content += 'A=A-1 \n'
    if OP == 'add':
        content += 'M=M+D \n'
    else:
        content += 'M=M-D \n'
    content += '@SP \n'
    content += 'M=M-1 \n'
    return content

def neg_():
    content = ''
    content += '//neg\n'
    content += '@SP\n'
    content += 'A=M-1\n'
    content += 'D=M\n'
    content += 'M=-D\n'
    return content



def eq_(labelCounter):
    # create labels
    labelNotEQ =  '.NotEQ_'  + str(labelCounter)
    labelEQ =  '.EQ_' +  str(labelCounter)
    #compare and push true or false
    content = ''
    content += '//Eq \n'
    # pop the first to D
    content += '@SP \n'
    content += 'A=M-1 \n'
    content += 'D=M \n'
    # take the second number on stack and compute to D
    content += 'A=A-1 \n'
    content += 'D=M-D \n'  # push a, push b -> compute a-b
    # if D is 0 so EQ, if D!=0 so NotEQ
    content += '@%s \n' %(labelEQ)
    content += 'D;JEQ \n'
    # so push 0 , 0 means False
    content += 'D=0 \n'
    content += '@SP \n'
    content += 'A=M-1 \n'
    content += 'A=A-1 \n'
    content += 'M=D \n'
    content += '@%s \n' % (labelNotEQ)
    content += '0,JMP \n'
    content += '(%s) \n' %  (labelEQ)
    content += 'D=-1 \n' # we insert 0 to D
    content += '@SP \n'
    content += 'A=M-1 \n'
    content += 'A=A-1 \n'
    content += 'M=D \n'
    content += '(%s) \n' % (labelNotEQ)
    content += '@SP \n'
    content += 'M=M-1 \n'
    return content



def gt_( labelCounter): # push a, push b, Is (a>b)?
    # create labels
    label_a_GT_b = '.a_GT_b' + '_' + str(labelCounter)
    label_a_Not_GT_b =  '.a_Not_GT_b' + '_' + str(labelCounter)
    # compare and push true or false
    content = ''
    content += '//GT \n'
    # pop the first to D
    content += '@SP \n'
    content += 'A=M-1 \n'
    content += 'D=M \n'
    # take the second number on stack and compute to D
    content += 'A=A-1 \n'
    content += 'D=M-D \n'  # push a, push b -> compute a-b
    # if D>0 so (a-b)>0 so it is True so we jmp
    content += '@%s \n' % (label_a_GT_b)
    content += 'D;JGT \n'
    # so push 0 , 0 means False
    content += 'D=0 \n'   # 0 means False
    content += '@SP \n'
    content += 'A=M-1 \n'
    content += 'A=A-1 \n'
    content += 'M=D \n'
    content += '@%s \n' % (label_a_Not_GT_b)
    content += '0,JMP \n'
    content += '(%s) \n' % (label_a_GT_b)
    content += 'D=-1 \n'  # we insert -1 to D , -1 means True
    content += '@SP \n'
    content += 'A=M-1 \n'
    content += 'A=A-1 \n'
    content += 'M=D \n'
    content += '(%s) \n' % (label_a_Not_GT_b)
    content += '@SP \n'
    content += 'M=M-1 \n'
    return content



def lt_( labelCounter):
    # create labels
    label_a_LT_b =  '.a_LT_b' + '_' + str(labelCounter)
    label_a_Not_LT_b =  '.a_Not_LT_b' + '_' + str(labelCounter)
    # compare and push true or false
    content = ''
    content += '//LT \n'
    # pop the first to D
    content += '@SP \n'
    content += 'A=M-1 \n'
    content += 'D=M \n'
    # take the second number on stack and compute to D
    content += 'A=A-1 \n'
    content += 'D=M-D \n'  # push a, push b -> compute a-b
    # if D<0 so (a-b)<0 so it is True that a<b so we jmp
    content += '@%s \n' % (label_a_LT_b)
    content += 'D;JLT \n'
    # so push 0 , 0 means False
    content += 'D=0 \n'  # 0 means False
    content += '@SP \n'
    content += 'A=M-1 \n'
    content += 'A=A-1 \n'
    content += 'M=D \n'
    content += '@%s \n' % (label_a_Not_LT_b)
    content += '0,JMP \n'
    content += '(%s) \n' % (label_a_LT_b)
    content += 'D=-1 \n'  # we insert -1 to D , -1 means True
    content += '@SP \n'
    content += 'A=M-1 \n'
    content += 'A=A-1 \n'
    content += 'M=D \n'
    content += '(%s) \n' % (label_a_Not_LT_b)
    content += '@SP \n'
    content += 'M=M-1 \n'
    return content



