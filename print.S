.intel_syntax noprefix
.globl _start
.section .text
_start:
	// create some stack memory
	sub rsp, 1024 // 1KB
	// stack 
	// char buffer[256] = [rsp:rsp+256]
	// open the file in O_RDONLY
	mov rax, 2 // open
	lea rdi, [rip+FILE_NAME] // FILE_NAME = "找找自己問題.txt"
	mov rsi, 0 // O_RDONLY
	mov rdx, 0 // NULL
	syscall

	mov r12, rax // store the fd

getline_loop:
	// read the line
	mov rax, 0 // read
	mov rdi, r12 // fd
	lea rsi, [rsp]  // buffer
	mov rdx, 256 // read_size = 256
	syscall

	mov r13, rax // store the read content's size

	// output the file content
	mov rax, 1 // write
	mov rdi, 1 // write to std output
	lea rsi, [rsp] // buffer
	mov rdx, r13 // write the r13 bytes
	syscall

	cmp r13, 256 // the size of read content == 256
	je getline_loop // repeat if true

 	// exit(0)
	mov rax, 60
	mov rdi, 0
	syscall

.section .data
FILE_NAME:
	.string "找找自己問題.txt"
