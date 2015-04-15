.data
	newline : .asciiz "\n"

.text
main:
	jal ProcLabel_arrays
	la $sp, 0($sp)
	j exit
L0:
	j Proc_endLabel_arrays
L1:
ProcLabel_arrays:
	sw $fp, -4($sp)
	sw $ra, -8($sp)
	la $fp, 0($sp)
	la $sp, -1340($sp)
L2:
	li $t0, 1
	sw $t0, 0($sp)
L3:
	li $t0, 1
	sw $t0, 4($sp)
L4:
	li $t0, 1
	sw $t0, 1304($sp)
L5:
	li $t0, 3
	sw $t0, 0($sp)
L6:
	lw $t0, 0($sp)
	sw $t0, 4($sp)
L7:
	lw $t0, 4($sp)
	sw $t0, 1304($sp)
L8:
	li $v0, 1
	lw $a0, 1304($sp)
	syscall
L9:
	la $sp, 0($fp)
	lw $ra, -8($fp)
	lw $fp, -4($sp)
	jr $ra
L10:
Proc_endLabel_arrays:

exit:
	li $v0, 10
	syscall
