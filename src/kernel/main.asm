ORG 0x7E00
BITS 16

jmp start

; Placeholder function for Python script execution
execute_python_script:
    ; Save the current register state
    pusha

    ; Set up the registers and flags for invoking the external Python interpreter
    mov ah, 0x4B                 ; AH = 0x4B: Load and execute a program
    mov al, 0x00                 ; AL = 0x00: Use the default drive
    mov dx, python_script_path   ; DX = address of the null-terminated Python script path
    int 0x21                     ; Invoke the MS-DOS interrupt to launch the Python interpreter

    ; Restore the register state
    popa

    ret


start:
    mov ax, 0
    mov ds, ax
    mov es, ax

    mov ss, ax
    mov sp, 0x7C00

    python_script_path db 'main.py', 0

    ; Call the placeholder function for Python script execution
    call execute_python_script

    cli
    hlt

puts:
    pusha

.loop:
    lodsb
    or al, al
    jz .done

    mov ah, 0x0E
    mov bh, 0x00
    int 0x10

    jmp .loop

.done:
    popa
    ret

.msg_hello: db 'Hello, World!', 0

times 510 - ($-$$) db 0
dw 0xAA55
