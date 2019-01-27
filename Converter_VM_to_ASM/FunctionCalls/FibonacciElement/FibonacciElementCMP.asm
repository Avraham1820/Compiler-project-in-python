// init
@256
D=A
@SP
M=D
// call Sys.init 0
@Sys.init.ReturnAdress2000
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL  // push locals of calling function
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG  // push arguments of calling function
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS  // push this of calling function
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT  // push that of calling function
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP  // ADR = SP - num_args - 5
D=M
@0
D=D-A
@5
D=D-A
@ARG
M=D
@SP  // reposition of locals
D=M
@LCL
M=D
@Sys.init
0;JMP
(Sys.init.ReturnAdress2000)
// function Main.fibonacci 0
(Main.fibonacci)
@0
D=A
@R15
M=D
(Main.fibonacci.loop) // reset the function locals to zero
@R15
D=M
@Main.fibonacci.end
D;JEQ
@R15
M=M-1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@Main.fibonacci.loop
0;JMP
(Main.fibonacci.end)
// push segment 0
@0
D=A
@2
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
// lt 
@SP
A=M-1
D=M
A=A-1
D=M-D
@IF_TRUE0
D;JLT
D=0
@SP
A=M-1
A=A-1
M=D
@IF_FALSE0
0;JMP
(IF_TRUE0)
D=-1
@SP
A=M-1
A=A-1
M=D
(IF_FALSE0)
@SP
M=M-1
// if go to IF_TRUE
@SP
M=M-1
A=M
D=M
@Main.IF_TRUE
D;JNE
// go to IF_FALSE
@Main.IF_FALSE
0;JMP
// label IF_TRUE
(Main.IF_TRUE)
// push segment 0
@0
D=A
@2
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// return
@5
D=A
@LCL
A=M-D
D=M
@R15
M=D
@SP
A=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@LCL
A=M-1
D=M
@THAT
M=D
@2
D=A
@LCL
A=M-D
D=M
@THIS
M=D
@3
D=A
@LCL
A=M-D
D=M
@ARG
M=D
@4
D=A
@LCL
A=M-D
D=M
@LCL
M=D
@R15
A=M
0;JMP
// label IF_FALSE
(Main.IF_FALSE)
// push segment 0
@0
D=A
@2
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
// sub 
@SP
A=M-1
D=M
A=A-1
M=M-D
@SP
M=M-1
// call Main.fibonacci 1
@Main.fibonacci.ReturnAdress1
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL  // push locals of calling function
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG  // push arguments of calling function
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS  // push this of calling function
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT  // push that of calling function
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP  // ADR = SP - num_args - 5
D=M
@1
D=D-A
@5
D=D-A
@ARG
M=D
@SP  // reposition of locals
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci.ReturnAdress1)
// push segment 0
@0
D=A
@2
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
// sub 
@SP
A=M-1
D=M
A=A-1
M=M-D
@SP
M=M-1
// call Main.fibonacci 1
@Main.fibonacci.ReturnAdress2
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL  // push locals of calling function
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG  // push arguments of calling function
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS  // push this of calling function
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT  // push that of calling function
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP  // ADR = SP - num_args - 5
D=M
@1
D=D-A
@5
D=D-A
@ARG
M=D
@SP  // reposition of locals
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci.ReturnAdress2)
// add 
@SP
A=M-1
D=M
A=A-1
M=D+M
@SP
M=M-1
// return
@5
D=A
@LCL
A=M-D
D=M
@R15
M=D
@SP
A=M-1
D=M
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@LCL
A=M-1
D=M
@THAT
M=D
@2
D=A
@LCL
A=M-D
D=M
@THIS
M=D
@3
D=A
@LCL
A=M-D
D=M
@ARG
M=D
@4
D=A
@LCL
A=M-D
D=M
@LCL
M=D
@R15
A=M
0;JMP
// function Sys.init 0
(Sys.init)
@0
D=A
@R15
M=D
(Sys.init.loop) // reset the function locals to zero
@R15
D=M
@Sys.init.end
D;JEQ
@R15
M=M-1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@Sys.init.loop
0;JMP
(Sys.init.end)
// push constant 4
@4
D=A
@SP
A=M
M=D
@SP
M=M+1
// call Main.fibonacci 1
@Main.fibonacci.ReturnAdress3
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL  // push locals of calling function
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG  // push arguments of calling function
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS  // push this of calling function
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT  // push that of calling function
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP  // ADR = SP - num_args - 5
D=M
@1
D=D-A
@5
D=D-A
@ARG
M=D
@SP  // reposition of locals
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci.ReturnAdress3)
// label WHILE
(Sys.WHILE)
// go to WHILE
@Sys.WHILE
0;JMP
