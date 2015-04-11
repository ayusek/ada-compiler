.data
	newline : .asciiz "\n"

.text
main:
	jal ProcLabel_test7
	la $sp, 0($sp)
	j exit
L0:
ProcLabel_test7:
	sw $fp, -4($sp)
	sw $ra, -8($sp)
	la $fp, 0($sp)
	la $sp, -60($sp)
L1:
	li $t0, 1
	sw $t0, 0($sp)
L2:
	li $t0, 1
	sw $t0, 4($sp)
L3:
	li $t0, 1
	sw $t0, 8($sp)
L4:
	lw $t0, 8($sp)
	lw $t1, 0($sp)
	add $t2, $t0, $t1
	sw $t2, 12($sp)
L5:
	lw $t0, 12($sp)
	li $t1, 10
	mul $t2, $t0, $t1
	sw $t2, 16($sp)
L6:
	lw $t0, 4($sp)
	lw $t1, 16($sp)
	add $t2, $t0, $t1
	sw $t2, 20($sp)
L7:
	lw $t0, 20($sp)
	li $t1, 10
	div $t2, $t0, $t1
	sw $t2, 24($sp)
L8:
	lw $t0, 24($sp)
	sw $t0, 4($sp)
L9:
	li $v0, 1
	lw $a0, 4($sp)
	syscall
L10:
	li $v0, 4
	la $a0, newline
	syscall
L11:
	la $sp, 0($fp)
	lw $ra, -8($fp)
	lw $fp, -4($sp)
	jr $ra

exit:
	li $v0, 10
	syscall
