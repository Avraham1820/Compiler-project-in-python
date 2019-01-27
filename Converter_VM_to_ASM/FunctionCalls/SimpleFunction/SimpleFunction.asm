//Function SimpleFunction.test 2 
(SimpleFunction.test) 
//push_const 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//push_const 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//push LCL 0 
@0 
D=A 
@LCL 
A=M+D 
D=M 
@SP 
A=M 
M=D 
@SP 
M=M+1 
//push LCL 1 
@1 
D=A 
@LCL 
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
//not 
@SP 
A=M-1 
D=M 
M=!D 
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
//add 
@SP 
A=M-1 
D=M 
A=A-1 
M=M+D 
@SP 
M=M-1 
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
//sub 
@SP 
A=M-1 
D=M 
A=A-1 
M=M-D 
@SP 
M=M-1 
//Return 
//save return address in R14
@LCL 
D=M 
@5 
A=D-A 
D=M 
@R14 
M=D 
//save function computation result to the top of the stack that the caller will see
@SP 
M=M-1 
@0 
D=A 
@ARG 
D=M+D 
@R13 
M=D 
@SP 
A=M 
D=M 
@R13 
A=M 
M=D 
//restore caller's sp
@ARG 
D=M+1 
@SP 
M=D 
//restor_caller's THAT 
@LCL
D=M
@1
A=D-A 
D=M
@THAT
M=D
//restor_caller's THIS 
@LCL
D=M
@2
A=D-A 
D=M
@THIS
M=D
//restor_caller's ARG 
@LCL
D=M
@3
A=D-A 
D=M
@ARG
M=D
//restor_caller's LCL 
@LCL
D=M
@4
A=D-A 
D=M
@LCL
M=D
//jump to return address that was stored in R14
@R14 
A=M 
1;JMP 

