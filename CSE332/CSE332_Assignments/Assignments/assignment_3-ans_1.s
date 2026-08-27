.data
    prompt:    .asciiz "Enter three integers: "
    valid_msg: .asciiz "The perimeter is: "
    invalid_msg: .asciiz "The input is invalid\n"

.text
.globl main

main:
    # Print prompt
    li $v0, 4
    la $a0, prompt
    syscall

    # Read three integers
    li $v0, 5
    syscall
    move $s0, $v0  # Store first input in $s0

    li $v0, 5
    syscall
    move $s1, $v0  # Store second input in $s1

    li $v0, 5
    syscall
    move $s2, $v0  # Store third input in $s2

    # Call validity function
    move $a0, $s0
    move $a1, $s1
    move $a2, $s2
    jal validity
    move $t0, $v0  # Store result of validity check

    # If validity returned false (0), print "The input is invalid"
    beqz $t0, print_invalid  

    # Otherwise, call perimeter function
    move $a0, $s0
    move $a1, $s1
    move $a2, $s2
    jal perimeter
    move $t1, $v0  # Save the perimeter result in $t1

    # Print valid message
    li $v0, 4
    la $a0, valid_msg
    syscall

    # Print the perimeter
    li $v0, 1
    move $a0, $t1  # Move the saved perimeter result to $a0
    syscall

    j exit

print_invalid:
    li $v0, 4
    la $a0, invalid_msg
    syscall

exit:
    li $v0, 10
    syscall

# Function: perimeter(int x, int y, int z)
# Returns x + y + z
perimeter:
    add $v0, $a0, $a1
    add $v0, $v0, $a2
    jr $ra

# Function: validity(int x, int y, int z)
# Checks triangle inequality rule
validity:
    add $t0, $a0, $a1  # t0 = x + y
    slt $t1, $t0, $a2  # if x + y > z ? t1 = 0
    bnez $t1, return_false 

    add $t0, $a1, $a2  # t0 = y + z
    slt $t1, $t0, $a0  # if y + z > x ? t1 = 0
    bnez $t1, return_false 

    add $t0, $a2, $a0  # t0 = z + x
    slt $t1, $t0, $a1  # if z + x > y ? t1 = 0
    bnez $t1, return_false 

    li $v0, 1  # Return true (1)
    jr $ra

return_false:
    li $v0, 0  # Return false (0)
    jr $ra