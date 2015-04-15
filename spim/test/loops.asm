.data
	newline : .asciiz "\n"

.text
main:
	jal ProcLabel_loops
	la $sp, 0($sp)
	j exit
L0:
	j Proc_endLabel_loops
L1:
ProcLabel_loops:
	sw $fp, -4($sp)
	sw $ra, -8($sp)
	la $fp, 0($sp)
	la $sp, -68($sp)
L2:
	li.s $f0, 1.0
	neg.s $f2, $f0
	s.s $f2, 0($sp)
L3:
	l.s $f0, 0($sp)
	s.s $f0, 4($sp)
L4:
	li $t0, 2
	sw $t0, 8($sp)
L5:
	j L7
L6:
	lw $t0, 8($sp)
	li $t1, 1
	add $t2, $t0, $t1
	sw $t2, 8($sp)
L7:
	lw $t0, 8($sp)
	li $t1, 8
	ble $t0, $t1, L9
L8:
	j L12
L9:
	li $v0, 1
	lw $a0, 8($sp)
	syscall
L10:
	li $t0, 1
newline0:
	ble $t0, $0, newline1
	li $v0, 4
	la $a0, newline
	syscall
	sub $t0, $t0, 1
	j newline0
newline1:
L11:
	j L6
L12:
	li $t0, 2
newline2:
	ble $t0, $0, newline3
	li $v0, 4
	la $a0, newline
	syscall
	sub $t0, $t0, 1
	j newline2
newline3:
L13:
	li $t0, 8
	sw $t0, 12($sp)
L14:
	j L16
L15:
	lw $t0, 12($sp)
	li $t1, 1
	sub $t2, $t0, $t1
	sw $t2, 12($sp)
L16:
	lw $t0, 12($sp)
	li $t1, 2
	bge $t0, $t1, L18
L17:
	j L21
L18:
	li $v0, 1
	lw $a0, 12($sp)
	syscall
L19:
	li $t0, 1
newline4:
	ble $t0, $0, newline5
	li $v0, 4
	la $a0, newline
	syscall
	sub $t0, $t0, 1
	j newline4
newline5:
L20:
	j L15
L21:
	l.s $f0, 4($sp)
	li.s $f1, 0.0
	c.lt.s $f0, $f1
	bc1t float0
	nop
	bc1f float1
	nop
float0:
	li $t2, 1
	j float2
float1:
	li $t2, 0
	j float2
float2:
	sw $t2, 16($sp)
L22:
	lw $t1, 16($sp)
	beq $t1, 1, L24
L23:
	j L33
L24:
	l.s $f0, 4($sp)
	neg.s $f2, $f0
	s.s $f2, 20($sp)
L25:
	l.s $f0, 20($sp)
	s.s $f0, 4($sp)
L26:
	l.s $f0, 4($sp)
	li.s $f1, 0.0
	c.le.s $f1, $f0
	bc1t float3
	nop
	bc1f float4
	nop
float3:
	li $t2, 1
	j float5
float4:
	li $t2, 0
	j float5
float5:
	sw $t2, 24($sp)
L27:
	lw $t1, 24($sp)
	beq $t1, 1, L29
L28:
	j L31
L29:
	li $v0, 2
	l.s $f12, 4($sp)
	syscall
L30:
	j L31
L31:
	li.s $f0, 1.0
	s.s $f0, 4($sp)
L32:
	j L33
L33:
	li $t0, 2
newline6:
	ble $t0, $0, newline7
	li $v0, 4
	la $a0, newline
	syscall
	sub $t0, $t0, 1
	j newline6
newline7:
L34:
	l.s $f0, 4($sp)
	li.s $f1, 10.0
	c.lt.s $f0, $f1
	bc1t float6
	nop
	bc1f float7
	nop
float6:
	li $t2, 1
	j float8
float7:
	li $t2, 0
	j float8
float8:
	sw $t2, 28($sp)
L35:
	lw $t1, 28($sp)
	beq $t1, 1, L37
L36:
	j L42
L37:
	l.s $f0, 4($sp)
	li.s $f1, 0.5
	add.s $f2, $f0, $f1
	s.s $f2, 32($sp)
L38:
	l.s $f0, 32($sp)
	s.s $f0, 4($sp)
L39:
	li $v0, 2
	l.s $f12, 4($sp)
	syscall
L40:
	li $t0, 1
newline8:
	ble $t0, $0, newline9
	li $v0, 4
	la $a0, newline
	syscall
	sub $t0, $t0, 1
	j newline8
newline9:
L41:
	j L34
L42:
	la $sp, 0($fp)
	lw $ra, -8($fp)
	lw $fp, -4($sp)
	jr $ra
L43:
Proc_endLabel_loops:

exit:
	li $v0, 10
	syscall
