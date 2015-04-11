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
	la $sp, -64($sp)
L2:
	li $t0, 1
	sw $t0, 0($sp)
L3:
	li $t0, 1
	sw $t0, 4($sp)
L4:
	li $t0, 1
	sw $t0, 8($sp)
L5:
	j Proc_endLabel_add
L6:
ProcLabel_add:
	sw $fp, -4($sp)
	sw $ra, -8($sp)
	la $fp, 0($sp)
	la $sp, -52($sp)
L7:
	lw $t0, 4($sp)
	li $t1, 2
	mul $t2, $t0, $t1
	sw $t2, 12($sp)
L8:
	lw $t0, 0($sp)
	lw $t1, 12($sp)
	add $t2, $t0, $t1
	sw $t2, 16($sp)
L9:
	lw $t0, 16($sp)
	sw $t0, 8($sp)
L10:
	lw $v0, 8($sp)
	la $sp, 0($fp)
	lw $ra, -8($fp)
	lw $fp, -4($sp)
	jr $ra
L11:
Proc_endLabel_add:
L12:
	lw $t0, 4($sp)
	sw $t0, -52($sp)
	lw $t0, 8($sp)
	sw $t0, -48($sp)
	jal ProcLabel_add
L13:
	sw $v0, 0($sp)
L14:
	li $v0, 1
	lw $a0, 0($sp)
	syscall
L15:
	li $v0, 4
	la $a0, newline
	syscall
L16:
	la $sp, 0($fp)
	lw $ra, -8($fp)
	lw $fp, -4($sp)
	jr $ra
L17:
Proc_endLabel_test7:

exit:
	li $v0, 10
	syscall
