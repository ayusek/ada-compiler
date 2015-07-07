.data
	newline : .asciiz "\n"

.text
main:
	jal ProcLabel_test2
	la $sp, 0($sp)
	j exit
L0:
	j Proc_endLabel_test2
L1:
ProcLabel_test2:
	sw $fp, -4($sp)
	sw $ra, -8($sp)
	la $fp, 0($sp)
	la $sp, -104($sp)
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
	lw $t0, 0($sp)
	li $t1, 1
	sge $t2, $t0, $t1
	sw $t2, 12($sp)
L6:
	lw $t1, 12($sp)
	beq $t1, 1, L8
L7:
	j L10
L8:
	li $t0, 2
	sw $t0, 4($sp)
L9:
	j L16
L10:
	lw $t0, 0($sp)
	li $t1, 0
	sge $t2, $t0, $t1
	sw $t2, 16($sp)
L11:
	lw $t1, 16($sp)
	beq $t1, 1, L13
L12:
	j L15
L13:
	li $t0, 1
	sw $t0, 4($sp)
L14:
	j L16
L15:
	li $t0, 4
	sw $t0, 4($sp)
L16:
	lw $t0, 8($sp)
	li $t1, 1
	seq $t2, $t0, $t1
	sw $t2, 20($sp)
L17:
	lw $t1, 20($sp)
	beq $t1, 1, L19
L18:
	j L23
L19:
	lw $t0, 4($sp)
	li $t1, 2
	seq $t2, $t0, $t1
	sw $t2, 24($sp)
L20:
	lw $t1, 24($sp)
	beq $t1, 1, L27
L21:
	j L23
L22:
	lw $t0, 20($sp)
	lw $t1, 24($sp)
	and $t2, $t0, $t1
	sw $t2, 28($sp)
L23:
	lw $t0, 8($sp)
	li $t1, 1
	sne $t2, $t0, $t1
	sw $t2, 32($sp)
L24:
	lw $t1, 32($sp)
	beq $t1, 1, L27
L25:
	j L34
L26:
	lw $t0, 28($sp)
	lw $t1, 32($sp)
	or $t2, $t0, $t1
	sw $t2, 36($sp)
L27:
	li $t0, 1
	sw $t0, 0($sp)
L28:
	lw $t0, 0($sp)
	li $t1, 1
	sge $t2, $t0, $t1
	sw $t2, 40($sp)
L29:
	lw $t1, 40($sp)
	beq $t1, 1, L31
L30:
	j L33
L31:
	li $t0, 10
	sw $t0, 0($sp)
L32:
	j L35
L33:
	j L35
L34:
	li $t0, 2
	sw $t0, 0($sp)
L35:
	lw $t0, 0($sp)
	li $t1, 5
	sle $t2, $t0, $t1
	sw $t2, 44($sp)
L36:
	lw $t1, 44($sp)
	beq $t1, 1, L38
L37:
	j L46
L38:
	lw $t0, 8($sp)
	li $t1, 1
	seq $t2, $t0, $t1
	sw $t2, 48($sp)
L39:
	lw $t1, 48($sp)
	beq $t1, 1, L41
L40:
	j L43
L41:
	li $t0, 1
	sw $t0, 0($sp)
L42:
	j L44
L43:
	li $t0, 2
	sw $t0, 0($sp)
L44:
	li $t0, 1
	sw $t0, 0($sp)
L45:
	j L35
L46:
	lw $t0, 8($sp)
	li $t1, 1
	seq $t2, $t0, $t1
	sw $t2, 52($sp)
L47:
	lw $t1, 52($sp)
	beq $t1, 1, L49
L48:
	j L51
L49:
	li $t0, 1
	sw $t0, 0($sp)
L50:
	j L52
L51:
	li $t0, 2
	sw $t0, 0($sp)
L52:
	li $t0, 1
	sw $t0, 4($sp)
L53:
	j L46
L54:
	li $t0, 1
	sw $t0, 56($sp)
L55:
	j L57
L56:
	lw $t0, 56($sp)
	li $t1, 1
	add $t2, $t0, $t1
	sw $t2, 56($sp)
L57:
	lw $t0, 56($sp)
	li $t1, 10
	ble $t0, $t1, L59
L58:
	j L67
L59:
	lw $t0, 8($sp)
	li $t1, 1
	seq $t2, $t0, $t1
	sw $t2, 60($sp)
L60:
	lw $t1, 60($sp)
	beq $t1, 1, L62
L61:
	j L64
L62:
	li $t0, 1
	sw $t0, 0($sp)
L63:
	j L65
L64:
	li $t0, 2
	sw $t0, 0($sp)
L65:
	li $t0, 1
	sw $t0, 8($sp)
L66:
	j L56
L67:
	li $t0, 1
	sw $t0, 64($sp)
L68:
	j L70
L69:
	lw $t0, 64($sp)
	li $t1, 1
	sub $t2, $t0, $t1
	sw $t2, 64($sp)
L70:
	lw $t0, 64($sp)
	li $t1, 10
	bge $t0, $t1, L72
L71:
	j L80
L72:
	lw $t0, 8($sp)
	li $t1, 1
	seq $t2, $t0, $t1
	sw $t2, 68($sp)
L73:
	lw $t1, 68($sp)
	beq $t1, 1, L75
L74:
	j L77
L75:
	li $t0, 1
	sw $t0, 0($sp)
L76:
	j L78
L77:
	li $t0, 2
	sw $t0, 0($sp)
L78:
	li $t0, 1
	sw $t0, 8($sp)
L79:
	j L69
L80:
	la $sp, 0($fp)
	lw $ra, -8($fp)
	lw $fp, -4($sp)
	jr $ra
L81:
Proc_endLabel_test2:

exit:
	li $v0, 10
	syscall
