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
	la $sp, -52($sp)
L2:
	li $t0, 1
	sw $t0, 0($sp)
L3:
	li $t0, 1
	sw $t0, 4($sp)
L4:
	j Proc_endLabel_Triple
L5:
ProcLabel_Triple:
	sw $fp, -4($sp)
	sw $ra, -8($sp)
	la $fp, 0($sp)
	la $sp, -44($sp)
L6:
	j Proc_endLabel_Second_Layer
L7:
ProcLabel_Second_Layer:
	sw $fp, -4($sp)
	sw $ra, -8($sp)
	la $fp, 0($sp)
	la $sp, -40($sp)
L8:
	j Proc_endLabel_Bottom_Layer
L9:
ProcLabel_Bottom_Layer:
	sw $fp, -4($sp)
	sw $ra, -8($sp)
	la $fp, 0($sp)
	la $sp, -36($sp)
L10:
	li $v0, 11
	li $a0, 'b'
	syscall
L11:
	li $t0, 5
	sw $t0, 0($sp)
L12:
	li $v0, 11
	li $a0, 'b'
	syscall
L13:
	la $sp, 0($fp)
	lw $ra, -8($fp)
	lw $fp, -4($sp)
	jr $ra
L14:
Proc_endLabel_Bottom_Layer:
L15:
	li $v0, 11
	li $a0, 's'
	syscall
L16:
	li $t0, 2
	sw $t0, 0($sp)
L17:
	lw $t0, 0($sp)
	sw $t0, -36($sp)
	jal ProcLabel_Bottom_Layer
L18:
	li $v0, 11
	li $a0, 's'
	syscall
L19:
	la $sp, 0($fp)
	lw $ra, -8($fp)
	lw $fp, -4($sp)
	jr $ra
L20:
Proc_endLabel_Second_Layer:
L21:
	li $v0, 11
	li $a0, 't'
	syscall
L22:
	li $t0, 3
	sw $t0, 0($sp)
L23:
	li $t0, 1
	sw $t0, 4($sp)
L24:
	lw $t0, 4($sp)
	sw $t0, -40($sp)
	jal ProcLabel_Second_Layer
L25:
	li $v0, 1
	lw $a0, 4($sp)
	syscall
L26:
	li $v0, 1
	lw $a0, 0($sp)
	syscall
L27:
	li $v0, 11
	li $a0, 't'
	syscall
L28:
	la $sp, 0($fp)
	lw $ra, -8($fp)
	lw $fp, -4($sp)
	jr $ra
L29:
Proc_endLabel_Triple:
L30:
	lw $t0, 0($sp)
	sw $t0, -44($sp)
	jal ProcLabel_Triple
L31:
	la $sp, 0($fp)
	lw $ra, -8($fp)
	lw $fp, -4($sp)
	jr $ra
L32:
Proc_endLabel_nesting:

exit:
	li $v0, 10
	syscall
