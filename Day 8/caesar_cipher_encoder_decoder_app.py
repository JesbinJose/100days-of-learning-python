import assets as a

def caeser(text,shift,direction):
    result = ""
    for char in text:
        if char not in a.alphabet:
            result = result + char
            continue
        position = a.alphabet.index(char)
        res_char_pos = position 
        if direction =="en":
            res_char_pos += shift
        else :
            res_char_pos -= shift
        res_char =  a.alphabet[res_char_pos % 26]
        result = result + res_char
    print(f"{direction}cypted data : {result}")

can_continue = True

print(a.logo)

while can_continue:
    direction = input("Type 'en' to encrypt, type 'de' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(text,shift,direction)
    would_continue = input("Do you want to continue the type y or n for exiting: \n")
    if would_continue == "n":
        can_continue = False


