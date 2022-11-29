# https://www.codewars.com//kata/58817056e7a31c2ceb000052

def interpreter(tape):
    memory = {}
    ptr = 0
    output = ''
    index_com = 0

    while True:
        com = tape[index_com]
        if com == ">":
            ptr += 1
        elif com == "<":
            ptr -= 1
        elif com == "+":
            memory[ptr] = (memory.get(ptr, 0) + 1) % 256
        elif com == "-":
            memory[ptr] = (memory.get(ptr, 0) - 1) % 256
        elif com == "*":
            output += chr(memory.get(ptr, 0))
        elif com == "&":
            break
        elif com == "/":
            index_com += memory.get(ptr, 0) == 0
        elif com == "\\":
            index_com += memory.get(ptr, 0) != 0
        index_com = (index_com + 1) % len(tape)
    return output
