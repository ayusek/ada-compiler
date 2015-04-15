.data
	newline : .asciiz "\n"

.text
main:
	jal ProcLabel_towers
	la $sp, 0($sp)
	j exit
L0:
	j Proc_endLabel_towers
L1:
ProcLabel_towers:
	sw $fp, -4($sp)
	sw $ra, -8($sp)
	la $fp, 0($sp)
	la $sp, -64($sp)
L2:
	j Proc_endLabel_Hanoi
L3:
ProcLabel_Hanoi:
	sw $fp, -4($sp)
	sw $ra, -8($sp)
	la $fp, 0($sp)
	la $sp, -60($sp)
L4:
	lw $t0, 0($sp)
	li $t1, 0
	sgt $t2, $t0, $t1
	sw $t2, 16($sp)
L5:
	lw $t1, 16($sp)
	beq $t1, 1, L7
L6:
	j L23
L7:
	lw $t0, 0($sp)
	li $t1, 1
	sub $t2, $t0, $t1
	sw $t2, 20($sp)
L8:
	lw $t0, 20($sp)
	sw $t0, -60($sp)
	lw $t0, 4($sp)
	sw $t0, -56($sp)
	lw $t0, 12($sp)
	sw $t0, -52($sp)
	lw $t0, 8($sp)
	sw $t0, -48($sp)
	jal ProcLabel_Hanoi
L9:
	li $v0, 1
	lw $a0, 0($sp)
	syscall
L10:
	li $v0, 11
	li $a0, ' '
	syscall
L11:
	li $v0, 11
	li $a0, ':'
	syscall
L12:
	li $v0, 11
	li $a0, ' '
	syscall
L13:
	li $v0, 1
	lw $a0, 4($sp)
	syscall
L14:
	li $v0, 11
	li $a0, ' '
	syscall
L15:
	li $v0, 11
	li $a0, '-'
	syscall
L16:
	li $v0, 11
	li $a0, '>'
	syscall
L17:
	li $v0, 11
	li $a0, ' '
	syscall
L18:
	li $v0, 1
	lw $a0, 8($sp)
	syscall
L19:
	li $t0, 1
newline0:
	ble $t0, $0, newline1
	li $v0, 4
	la $a0, newline
	syscall
	sub $t0, $t0, 1
	j newline0
newline1:
L20:
	lw $t0, 0($sp)
	li $t1, 1
	sub $t2, $t0, $t1
	sw $t2, 24($sp)
L21:
	lw $t0, 24($sp)
	sw $t0, -60($sp)
	lw $t0, 12($sp)
	sw $t0, -56($sp)
	lw $t0, 8($sp)
	sw $t0, -52($sp)
	lw $t0, 4($sp)
	sw $t0, -48($sp)
	jal ProcLabel_Hanoi
L22:
	j L23
L23:
	la $sp, 0($fp)
	lw $ra, -8($fp)
	lw $fp, -4($sp)
	jr $ra
L24:
Proc_endLabel_Hanoi:
L25:
	li $v0, 5
	syscall
	sw $v0, 0($sp)
L26:
	lw $t0, 0($sp)
	sw $t0, -60($sp)
	li $t0, 0
	sw $t0, -56($sp)
	li $t0, 2
	sw $t0, -52($sp)
	li $t0, 1
	sw $t0, -48($sp)
	jal ProcLabel_Hanoi
L27:
	la $sp, 0($fp)
	lw $ra, -8($fp)
	lw $fp, -4($sp)
	jr $ra
L28:
Proc_endLabel_towers:

exit:
	li $v0, 10
	syscall
