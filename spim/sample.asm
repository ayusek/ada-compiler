.data
	newline : .asciiz "\n"

.text
main:
	jal ProcLabel_test7
	la $sp, 0($sp)
	j exit
L0:
	j Proc_endLabel_test7
L1:
ProcLabel_test7:
	sw $fp, -4($sp)
	sw $ra, -8($sp)
	la $fp, 0($sp)
	la $sp, -44($sp)
L2:
	li $t0, 'a'
	sw $t0, 0($sp)
L3:
	li $t0, 'a'
	sw $t0, 4($sp)
L4:
	li $t0, 'a'
	sw $t0, 8($sp)
L5:
	li $v0, 11
	lw $a0, 0($sp)
	syscall
L6:
	la $sp, 0($fp)
	lw $ra, -8($fp)
	lw $fp, -4($sp)
	jr $ra
L7:
Proc_endLabel_test7:

exit:
	li $v0, 10
	syscall
