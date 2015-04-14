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
	la $sp, -84($sp)
L2:
	li $t0, 0
	sw $t0, 0($sp)
L3:
	j Proc_endLabel_Even
L4:
ProcLabel_Even:
	sw $fp, -4($sp)
	sw $ra, -8($sp)
	la $fp, 0($sp)
	la $sp, -56($sp)
L5:
	lw $t0, 0($sp)
	li $t1, 0
	seq $t2, $t0, $t1
	sw $t2, 16($sp)
L6:
	lw $t1, 16($sp)
	beq $t1, 1, L8
L7:
	j L10
L8:
	li $t0, 1
	sw $t0, 8($sp)
L9:
	j L12
L10:
	lw $t0, 0($sp)
	li $t1, 1
	sub $t2, $t0, $t1
	sw $t2, 20($sp)
L11:
	lw $t0, 20($sp)
	sw $t0, 12($sp)
L12:
	lw $t0, 8($sp)
	sw $t0, 4($sp)
L13:
	lw $v0, 4($sp)
	la $sp, 0($fp)
	lw $ra, -8($fp)
	lw $fp, -4($sp)
	jr $ra
L14:
Proc_endLabel_Even:
L15:
	j Proc_endLabel_Odd
L16:
ProcLabel_Odd:
	sw $fp, -4($sp)
	sw $ra, -8($sp)
	la $fp, 0($sp)
	la $sp, -56($sp)
L17:
	lw $t0, 0($sp)
	li $t1, 0
	seq $t2, $t0, $t1
	sw $t2, 16($sp)
L18:
	lw $t1, 16($sp)
	beq $t1, 1, L20
L19:
	j L22
L20:
	li $t0, 0
	sw $t0, 8($sp)
L21:
	j L26
L22:
	lw $t0, 0($sp)
	li $t1, 1
	sub $t2, $t0, $t1
	sw $t2, 20($sp)
L23:
	lw $t0, 20($sp)
	sw $t0, 12($sp)
L24:
	lw $t0, 12($sp)
	sw $t0, -56($sp)
	jal ProcLabel_Even
L25:
	sw $v0, 8($sp)
L26:
	lw $t0, 8($sp)
	sw $t0, 4($sp)
L27:
	lw $v0, 4($sp)
	la $sp, 0($fp)
	lw $ra, -8($fp)
	lw $fp, -4($sp)
	jr $ra
L28:
Proc_endLabel_Odd:
L29:
	li $t0, 4
	sw $t0, -56($sp)
	jal ProcLabel_Odd
L30:
	sw $v0, 0($sp)
L31:
	li $v0, 1
	lw $a0, 0($sp)
	syscall
L32:
	li $t0, 1
newline0:
	ble $t0, $0, newline1
	li $v0, 4
	la $a0, newline
	syscall
	sub $t0, $t0, 1
	j newline0
newline1:
L33:
	li $t0, 4
	sw $t0, -56($sp)
	jal ProcLabel_Even
L34:
	sw $v0, 0($sp)
L35:
	li $v0, 1
	lw $a0, 0($sp)
	syscall
L36:
	la $sp, 0($fp)
	lw $ra, -8($fp)
	lw $fp, -4($sp)
	jr $ra
L37:
Proc_endLabel_test7:

exit:
	li $v0, 10
	syscall
