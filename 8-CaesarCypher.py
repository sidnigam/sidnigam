import random
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(direction, text, shift):
    result = list(text)
    if direction == 'encrypt':
        for i in range(len(result)):
            result[i] = alphabet[alphabet.index(text[i])+shift]
        output = "".join(result)
        print (f"The encoded text is {output}")
    else:
        for i in range(len(result)):
            result[i] = alphabet[alphabet.index(text[i])-shift]
        output = "".join(result)
        print (f"The decoded text is {output}")

caesar(direction, text, shift)
