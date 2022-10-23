def decode_morse(morse_code):
    morse_code = morse_code.strip(" ")
    morse_code = morse_code.replace("  ", " * ")
    morse_code = morse_code.split()
    human_code = []
    for item in morse_code:
        if item == "*":
            human_code.append(" ")
        else:
            human_code.append(MORSE_CODE[item])
    return "".join(human_code)