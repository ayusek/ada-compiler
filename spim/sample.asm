.data
	newline : .asciiz "\n"

.text
main:
	jal ProcLabel_test5
	la $sp, 0($sp)
	j exit
L0:
	j Proc_endLabel_test5
L1:
ProcLabel_test5:
	sw $fp, -4($sp)
	sw $ra, -8($sp)
	la $fp, 0($sp)
	la $sp, -580($sp)
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
	li $t0, 1
	sw $t0, 0($sp)
L6:
	li $t0, 1
	sw $t0, 460($sp)
L7:
	j L9
L8:
	lw $t0, 460($sp)
	li $t1, 1
	add $t2, $t0, $t1
	sw $t2, 460($sp)
L9:
	lw $t0, 460($sp)
	li $t1, 7
	ble $t0, $t1, L11
L10:
	j L24
L11:
	lw $t0, 460($sp)
	li $t1, 1
	sub $t2, $t0, $t1
	sw $t2, 464($sp)
L12:
	li $t0, 7
	lw $t1, 464($sp)
	mul $t2, $t0, $t1
	sw $t2, 468($sp)
L13:
	lw $t0, 460($sp)
	li $t1, 1
	sub $t2, $t0, $t1
	sw $t2, 472($sp)
L14:
	lw $t0, 468($sp)
	lw $t1, 472($sp)
	add $t2, $t0, $t1
	sw $t2, 476($sp)
L15:
	li $t0, 4
	lw $t1, 476($sp)
	mul $t2, $t0, $t1
	sw $t2, 480($sp)
L16:
	lw $t0, 460($sp)
	li $t4, 68
	add $t4, $sp, $t4
	lw $t3, 480($sp)
	add $t3, $t3, $t4
	sw $t0, ($t3)
L17:
	lw $t0, 460($sp)
	li $t1, 1
	sub $t2, $t0, $t1
	sw $t2, 484($sp)
L18:
	li $t0, 7
	lw $t1, 484($sp)
	mul $t2, $t0, $t1
	sw $t2, 488($sp)
L19:
	lw $t0, 460($sp)
	li $t1, 1
	sub $t2, $t0, $t1
	sw $t2, 492($sp)
L20:
	lw $t0, 488($sp)
	lw $t1, 492($sp)
	add $t2, $t0, $t1
	sw $t2, 496($sp)
L21:
	li $t0, 4
	lw $t1, 496($sp)
	mul $t2, $t0, $t1
	sw $t2, 500($sp)
L22:
	lw $t0, 460($sp)
	li $t4, 264
	add $t4, $sp, $t4
	lw $t3, 500($sp)
	add $t3, $t3, $t4
	sw $t0, ($t3)
L23:
	j L8
L24:
	li $t0, 7
	sw $t0, 504($sp)
L25:
	j L27
L26:
	lw $t0, 504($sp)
	li $t1, 1
	sub $t2, $t0, $t1
	sw $t2, 504($sp)
L27:
	lw $t0, 504($sp)
	li $t1, 1
	bge $t0, $t1, L29
L28:
	j L43
L29:
	lw $t0, 504($sp)
	li $t1, 1
	sub $t2, $t0, $t1
	sw $t2, 508($sp)
L30:
	li $t0, 7
	lw $t1, 508($sp)
	mul $t2, $t0, $t1
	sw $t2, 512($sp)
L31:
	lw $t0, 504($sp)
	li $t1, 1
	sub $t2, $t0, $t1
	sw $t2, 516($sp)
L32:
	lw $t0, 512($sp)
	lw $t1, 516($sp)
	add $t2, $t0, $t1
	sw $t2, 520($sp)
L33:
	li $t0, 4
	lw $t1, 520($sp)
	mul $t2, $t0, $t1
	sw $t2, 524($sp)
L34:
	li $v0, 1
	li $t4, 68
	add $t4, $sp, $t4
	lw $t5, 524($sp)
	add $t4, $t4, $t5
	lw $a0, ($t4)
	syscall
L35:
	lw $t0, 504($sp)
	li $t1, 1
	sub $t2, $t0, $t1
	sw $t2, 528($sp)
L36:
	li $t0, 7
	lw $t1, 528($sp)
	mul $t2, $t0, $t1
	sw $t2, 532($sp)
L37:
	lw $t0, 504($sp)
	li $t1, 1
	sub $t2, $t0, $t1
	sw $t2, 536($sp)
L38:
	lw $t0, 532($sp)
	lw $t1, 536($sp)
	add $t2, $t0, $t1
	sw $t2, 540($sp)
L39:
	li $t0, 4
	lw $t1, 540($sp)
	mul $t2, $t0, $t1
	sw $t2, 544($sp)
L40:
	li $v0, 1
	li $t4, 264
	add $t4, $sp, $t4
	lw $t5, 544($sp)
	add $t4, $t4, $t5
	lw $a0, ($t4)
	syscall
L41:
	li $t0, 1
newline0:
	ble $t0, $0, newline1
	li $v0, 4
	la $a0, newline
	syscall
	sub $t0, $t0, 1
	j newline0
newline1:
L42:
	j L26
L43:
	la $sp, 0($fp)
	lw $ra, -8($fp)
	lw $fp, -4($sp)
	jr $ra
L44:
Proc_endLabel_test5:

exit:
	li $v0, 10
	syscall
