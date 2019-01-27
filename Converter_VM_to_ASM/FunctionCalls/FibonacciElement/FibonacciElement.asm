//SP_Init_To 256 
@256 
D=A 
@SP 
M=D 
// call Sys.init 0
//push_const Sys.init.ReturnAdress0
@Sys.init.ReturnAdress0
D=A
@SP
A=M
M=D
@SP
M=M+1
//store_caller's LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
//store_caller's ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
//store_caller's THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
//store_caller's THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
//change arg to callee's arg
@SP 
D=M
@0
D=D-A
@5
D=D-A
@ARG
M=D
//change lcl to callee's lcl
@SP  
D=M
@LCL
M=D
//goto - function call
@Sys.init
0;JMP
(Sys.init.ReturnAdress0)
//Function Main.fibonacci 0 
(Main.fibonacci) 
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
//LT 
@SP 
A=M-1 
D=M 
A=A-1 
D=M-D 
@.a_LT_b_1 
D;JLT 
D=0 
@SP 
A=M-1 
A=A-1 
M=D 
@.a_Not_LT_b_1 
0,JMP 
(.a_LT_b_1) 
D=-1 
@SP 
A=M-1 
A=A-1 
M=D 
(.a_Not_LT_b_1) 
@SP 
M=M-1 
// if go to IF_TRUE
@SP
M=M-1
A=M
D=M
@Main.fibonacci.IF_TRUE
D;JNE
// go to IF_FALSE
@Main.fibonacci.IF_FALSE
0;JMP 
// label IF_TRUE
(Main.fibonacci.IF_TRUE)
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

// label IF_FALSE
(Main.fibonacci.IF_FALSE)
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
// call Main.fibonacci 1
//push_const Main.fibonacci.ReturnAdress2
@Main.fibonacci.ReturnAdress2
D=A
@SP
A=M
M=D
@SP
M=M+1
//store_caller's LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
//store_caller's ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
//store_caller's THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
//store_caller's THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
//change arg to callee's arg
@SP 
D=M
@1
D=D-A
@5
D=D-A
@ARG
M=D
//change lcl to callee's lcl
@SP  
D=M
@LCL
M=D
//goto - function call
@Main.fibonacci
0;JMP
(Main.fibonacci.ReturnAdress2)
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
// call Main.fibonacci 1
//push_const Main.fibonacci.ReturnAdress3
@Main.fibonacci.ReturnAdress3
D=A
@SP
A=M
M=D
@SP
M=M+1
//store_caller's LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
//store_caller's ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
//store_caller's THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
//store_caller's THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
//change arg to callee's arg
@SP 
D=M
@1
D=D-A
@5
D=D-A
@ARG
M=D
//change lcl to callee's lcl
@SP  
D=M
@LCL
M=D
//goto - function call
@Main.fibonacci
0;JMP
(Main.fibonacci.ReturnAdress3)
//add 
@SP 
A=M-1 
D=M 
A=A-1 
M=M+D 
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

//Function Sys.init 0 
(Sys.init) 
//push_const 4
@4
D=A
@SP
A=M
M=D
@SP
M=M+1
// call Main.fibonacci 1
//push_const Main.fibonacci.ReturnAdress4
@Main.fibonacci.ReturnAdress4
D=A
@SP
A=M
M=D
@SP
M=M+1
//store_caller's LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
//store_caller's ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
//store_caller's THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
//store_caller's THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
//change arg to callee's arg
@SP 
D=M
@1
D=D-A
@5
D=D-A
@ARG
M=D
//change lcl to callee's lcl
@SP  
D=M
@LCL
M=D
//goto - function call
@Main.fibonacci
0;JMP
(Main.fibonacci.ReturnAdress4)
// label WHILE
(Sys.init.WHILE)
// go to WHILE
@Sys.init.WHILE
0;JMP 
