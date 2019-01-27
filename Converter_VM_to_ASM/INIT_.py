import os

def segments_(SP, LCL, ARG, THIS, THAT):
    content = ''
    content += '//SP_Init_To %d \n' % (SP)
    content += '@%d \n' % (SP)
    content += 'D=A \n'
    content += '@SP \n'
    content += 'M=D \n'

    content += '//LCL_Init_To %d \n' % (LCL)
    content += '@%d \n' % (LCL)
    content += 'D=A \n'
    content += '@LCL \n'
    content += 'M=D \n'

    content += '//ARG_Init_To %d \n' % (ARG)
    content += '@%d \n' % (ARG)
    content += 'D=A \n'
    content += '@ARG \n'
    content += 'M=D \n'

    content += '//THIS_Init_To %d \n' % (THIS)
    content += '@%d \n' % (THIS)
    content += 'D=A \n'
    content += '@THIS \n'
    content += 'M=D \n'

    content += '//THAT_Init_To %d \n' % (THAT)
    content += '@%d \n' % (THAT)
    content += 'D=A \n'
    content += '@THAT \n'
    content += 'M=D \n'
    content += '///////////////////////// \n'
    return content


def sys_():
    content = ''
    content += '//SP_Init_To %d \n' % (256)
    content += '@%d \n' % (256)
    content += 'D=A \n'
    content += '@SP \n'
    content += 'M=D \n'
    return content

