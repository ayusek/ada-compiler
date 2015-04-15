.data
	newline : .asciiz "\n"

.text
main:
	jal ProcLabel_nesting
	la $sp, 0($sp)
	j exit
L0:
	j Proc_endLabel_nesting
L1:
ProcLabel_nesting:
	sw $fp, -4($sp)
	sw $ra, -8($sp)
	la $fp, 0($sp)
	la $sp, -48($sp)
L2:
	j Proc_endLabel_Triple
L3:
ProcLabel_Triple:
	sw $fp, -4($sp)
	sw $ra, -8($sp)
	la $fp, 0($sp)
	la $sp, -44($sp)
L4:
	j Proc_endLabel_Second_Layer
L5:
ProcLabel_Second_Layer:
	sw $fp, -4($sp)
	sw $ra, -8($sp)
	la $fp, 0($sp)
	la $sp, -40($sp)
L6:
	j Proc_endLabel_Bottom_Layer
L7:
ProcLabel_Bottom_Layer:
	sw $fp, -4($sp)
	sw $ra, -8($sp)
	la $fp, 0($sp)
	la $sp, -36($sp)
L8:
	li $v0, 11
	li $a0, 'b'
	syscall
L9:
	li $t0, 1
	sw $t0, 0($sp)
L10:
	li $v0, 11
	li $a0, 'b'
	syscall
L11:
	lw $v0, 0($sp)
	la $sp, 0($fp)
	lw $ra, -8($fp)
	lw $fp, -4($sp)
	jr $ra
L12:
Proc_endLabel_Bottom_Layer:
L13:
	li $v0, 11
	li $a0, 's'
	syscall
L14:
	li $t0, 2
	sw $t0, 0($sp)
L15:
	jal ProcLabel_Bottom_Layer
L16:
	sw $v0, 0($sp)
L17:
	li $v0, 11
	li $a0, 's'
	syscall
L18:
	lw $v0, 0($sp)
	la $sp, 0($fp)
	lw $ra, -8($fp)
	lw $fp, -4($sp)
	jr $ra
L19:
Proc_endLabel_Second_Layer:
L20:
	li $v0, 11
	li $a0, 't'
	syscall
L21:
	li $t0, 3
	sw $t0, 0($sp)
L22:
	jal ProcLabel_Second_Layer
L23:
	sw $v0, 0($sp)
L24:
	li $v0, 11
	li $a0, 't'
	syscall
L25:
	lw $v0, 0($sp)
	la $sp, 0($fp)
	lw $ra, -8($fp)
	lw $fp, -4($sp)
	jr $ra
L26:
Proc_endLabel_Triple:
L27:
	jal ProcLabel_Triple
L28:
	sw $v0, 0($sp)
L29:
	la $sp, 0($fp)
	lw $ra, -8($fp)
	lw $fp, -4($sp)
	jr $ra
L30:
Proc_endLabel_nesting:

exit:
	li $v0, 10
	syscall
