.data
prompt:     .asciiz "Enter your full name (first and last name): "
buffer:     .space 100          # Buffer to store the input name
max_msg:    .asciiz "Maximum ASCII value: "
min_msg:    .asciiz "Minimum ASCII value: "
newline:    .asciiz "\n"

.text
.globl main

main:
    # Prompt for input
    li $v0, 4                  # syscall for print_string
    la $a0, prompt             # Load address of the prompt message
    syscall

    # Read input (full name)
    li $v0, 8                  # syscall for read_string
    la $a0, buffer             # Load address of the buffer
    li $a1, 100                # Maximum number of characters to read
    syscall

    # Initialize max and min
    li $t0, 0                  # Initialize max to 0
    li $t1, 127                 # Initialize min to 127 (highest ASCII value for comparison)

    # Pointer to buffer
    la $t2, buffer             # Load address of the buffer into $t2

process_loop:
    lb $t3, 0($t2)             # Load byte from buffer into $t3
    beqz $t3, done             # If null terminator (end of string), exit loop

    # Check if character is space
    li $t4, ' '                # Load ASCII value of space into $t4
    beq $t3, $t4, skip_space   # If character is space, skip it

    # Compare for max
    bgt $t3, $t0, set_max      # If current character > max, update max
    j check_min                # Else, check for min

set_max:
    move $t0, $t3              # Update max to current character
    j check_min                # Jump to check for min

check_min:
    blt $t3, $t1, set_min      # If current character < min, update min
    j next_char                # Else, move to next character

set_min:
    move $t1, $t3              # Update min to current character

next_char:
    addi $t2, $t2, 1           # Move to the next character in the buffer
    j process_loop             # Repeat the loop

skip_space:
    addi $t2, $t2, 1           # Skip the space character
    j process_loop             # Repeat the loop

done:
    # Print max message
    li $v0, 4                  # syscall for print_string
    la $a0, max_msg            # Load address of the max message
    syscall

    # Print max value
    li $v0, 1                  # syscall for print_int
    move $a0, $t0              # Move max value to $a0
    syscall

    # Print newline
    li $v0, 4                  # syscall for print_string
    la $a0, newline            # Load address of the newline
    syscall

    # Print min message
    li $v0, 4                  # syscall for print_string
    la $a0, min_msg            # Load address of the min message
    syscall

    # Print min value
    li $v0, 1                  # syscall for print_int
    move $a0, $t1              # Move min value to $a0
    syscall

    # Exit program
    li $v0, 10                 # syscall for exit
    syscall