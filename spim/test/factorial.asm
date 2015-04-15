.data
	newline : .asciiz "\n"

.text
main:
	jal ProcLabel_factorial
	la $sp, 0($sp)
	j exit
L0:
	j Proc_endLabel_factorial
L1:
ProcLabel_factorial:
	sw $fp, -4($sp)
	sw $ra, -8($sp)
	la $fp, 0($sp)
	la $sp, -60($sp)
L2:
	j Proc_endLabel_Fact
L3:
ProcLabel_Fact:
	sw $fp, -4($sp)
	sw $ra, -8($sp)
	la $fp, 0($sp)
	la $sp, -52($sp)
L4:
	lw $t0, 0($sp)
	li $t1, 1
	sgt $t2, $t0, $t1
	sw $t2, 8($sp)
L5:
	lw $t1, 8($sp)
	beq $t1, 1, L7
L6:
	j L13
L7:
	lw $t0, 0($sp)
	li $t1, 1
	sub $t2, $t0, $t1
	sw $t2, 12($sp)
L8:
	lw $t0, 12($sp)
	sw $t0, -52($sp)
	jal ProcLabel_Fact
L9:
	sw $v0, 4($sp)
L10:
	lw $t0, 4($sp)
	lw $t1, 0($sp)
	mul $t2, $t0, $t1
	sw $t2, 16($sp)
L11:
	lw $t0, 16($sp)
	sw $t0, 4($sp)
L12:
	j L14
L13:
	lw $t0, 0($sp)
	sw $t0, 4($sp)
L14:
	lw $v0, 4($sp)
	la $sp, 0($fp)
	lw $ra, -8($fp)
	lw $fp, -4($sp)
	jr $ra
L15:
Proc_endLabel_Fact:
L16:
	li $v0, 5
	syscall
	sw $v0, 0($sp)
L17:
	li $v0, 1
	lw $a0, 0($sp)
	syscall
L18:
	li $t0, 1
newline0:
	ble $t0, $0, newline1
	li $v0, 4
	la $a0, newline
	syscall
	sub $t0, $t0, 1
	j newline0
newline1:
L19:
	lw $t0, 0($sp)
	sw $t0, -52($sp)
	jal ProcLabel_Fact
L20:
	sw $v0, 4($sp)
L21:
	li $v0, 1
	lw $a0, 4($sp)
	syscall
L22:
	la $sp, 0($fp)
	lw $ra, -8($fp)
	lw $fp, -4($sp)
	jr $ra
L23:
Proc_endLabel_factorial:

exit:
	li $v0, 10
	syscall
