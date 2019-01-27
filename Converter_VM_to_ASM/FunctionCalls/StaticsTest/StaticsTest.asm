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
//Function Class1.set 0 
(Class1.set) 
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
//pop_static 0
@SP
M=M-1
A=M
D=M
@Class1.0
M=D
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
//pop_static 1
@SP
M=M-1
A=M
D=M
@Class1.1
M=D
//push_const 0
@0
D=A
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

//Function Class1.get 0 
(Class1.get) 
//push_static 0
@Class1.0
D=M
@SP
A=M
M=D
@SP
M=M+1
//push_static 1
@Class1.1
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

//Function Class2.set 0 
(Class2.set) 
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
//pop_static 0
@SP
M=M-1
A=M
D=M
@Class2.0
M=D
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
//pop_static 1
@SP
M=M-1
A=M
D=M
@Class2.1
M=D
//push_const 0
@0
D=A
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

//Function Class2.get 0 
(Class2.get) 
//push_static 0
@Class2.0
D=M
@SP
A=M
M=D
@SP
M=M+1
//push_static 1
@Class2.1
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

//Function Sys.init 0 
(Sys.init) 
//push_const 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1
//push_const 8
@8
D=A
@SP
A=M
M=D
@SP
M=M+1
// call Class1.set 2
//push_const Class1.set.ReturnAdress1
@Class1.set.ReturnAdress1
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
@2
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
@Class1.set
0;JMP
(Class1.set.ReturnAdress1)
//pop_temp 0
@0
D=A
@5
D=A+D
@SP
A=M
M=D
@SP
AM=M-1
D=M
A=A+1
A=M
M=D
//push_const 23
@23
D=A
@SP
A=M
M=D
@SP
M=M+1
//push_const 15
@15
D=A
@SP
A=M
M=D
@SP
M=M+1
// call Class2.set 2
//push_const Class2.set.ReturnAdress2
@Class2.set.ReturnAdress2
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
@2
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
@Class2.set
0;JMP
(Class2.set.ReturnAdress2)
//pop_temp 0
@0
D=A
@5
D=A+D
@SP
A=M
M=D
@SP
AM=M-1
D=M
A=A+1
A=M
M=D
// call Class1.get 0
//push_const Class1.get.ReturnAdress3
@Class1.get.ReturnAdress3
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
@Class1.get
0;JMP
(Class1.get.ReturnAdress3)
// call Class2.get 0
//push_const Class2.get.ReturnAdress4
@Class2.get.ReturnAdress4
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
@Class2.get
0;JMP
(Class2.get.ReturnAdress4)
// label WHILE
(Sys.init.WHILE)
// go to WHILE
@Sys.init.WHILE
0;JMP 
