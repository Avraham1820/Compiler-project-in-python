//push ARG 1 
@1 
D=A 
@ARG 
A=M+D 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 
//pop_pointer 1
@SP
AM=M-1
D=M
@4
M=D
//push_const 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop_THAT 0
@0
D=A
@THAT
D=M+D
@SP
A=M
M=D
A=A-1
D=M 
A=A+1
A=M
M=D
@SP
M=M-1
//push_const 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop_THAT 1
@1
D=A
@THAT
D=M+D
@SP
A=M
M=D
A=A-1
D=M 
A=A+1
A=M
M=D
@SP
M=M-1
//push ARG 0 
@0 
D=A 
@ARG 
A=M+D 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 
//push_const 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
//sub 
@SP 
A=M-1 
D=M 
A=A-1 
M=M-D 
@SP 
M=M-1 
//pop_ARG 0
@0
D=A
@ARG
D=M+D
@SP
A=M
M=D
A=A-1
D=M 
A=A+1
A=M
M=D
@SP
M=M-1
// label MAIN_LOOP_START
(SimpleFunction.test.MAIN_LOOP_START)
//push ARG 0 
@0 
D=A 
@ARG 
A=M+D 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 
// if go to COMPUTE_ELEMENT
@SP
M=M-1
A=M
D=M
@SimpleFunction.test.COMPUTE_ELEMENT
D;JNE
// go to END_PROGRAM
@SimpleFunction.test.END_PROGRAM
0;JMP 
// label COMPUTE_ELEMENT
(SimpleFunction.test.COMPUTE_ELEMENT)
//push THAT 0 
@0 
D=A 
@THAT 
A=M+D 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 
//push THAT 1 
@1 
D=A 
@THAT 
A=M+D 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 
//add 
@SP 
A=M-1 
D=M 
A=A-1 
M=M+D 
@SP 
M=M-1 
//pop_THAT 2
@2
D=A
@THAT
D=M+D
@SP
A=M
M=D
A=A-1
D=M 
A=A+1
A=M
M=D
@SP
M=M-1
//push_ptr 1
@4

D=M
@SP
A=M
M=D
@SP
M=M+1
//push_const 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
//add 
@SP 
A=M-1 
D=M 
A=A-1 
M=M+D 
@SP 
M=M-1 
//pop_pointer 1
@SP
AM=M-1
D=M
@4
M=D
//push ARG 0 
@0 
D=A 
@ARG 
A=M+D 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 
//push_const 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
//sub 
@SP 
A=M-1 
D=M 
A=A-1 
M=M-D 
@SP 
M=M-1 
//pop_ARG 0
@0
D=A
@ARG
D=M+D
@SP
A=M
M=D
A=A-1
D=M 
A=A+1
A=M
M=D
@SP
M=M-1
// go to MAIN_LOOP_START
@SimpleFunction.test.MAIN_LOOP_START
0;JMP 
// label END_PROGRAM
(SimpleFunction.test.END_PROGRAM)
