# Caesar Cipher, message encrypting

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z'
            ]


# Defining encrypting/decrypting function
def caesar(direction, text, shift):

    # creating empty list to shift letters
    output_text = []
    # Encoding message
    if direction.lower() == "encode":

        if shift >= 26:
            shift = shift % 26
        # Finding index of the letter in alphabet
        for char in text:
            if char not in alphabet:
                output_text.append(char)
            else:
                i_char = alphabet.index(char) + shift
                if i_char >= 26:
                    i_char = abs(26-i_char)
                output_text.append(alphabet[i_char])
        # Printing encrypted message
        print(f"Encrypted text is: {''.join(output_text)}")
    # In case of decoding we just deduct shift from letter index in alphabet
    elif direction.lower() == "decode":
        if shift > 26:
            shift = shift % 26

        for char in text:
            # If character is not in alphabet, we just leave it as it is
            if char not in alphabet:
                output_text.append(char)
            else:
                i_char = alphabet.index(char) - shift
                output_text.append(alphabet[i_char])
        print(f"Decrypted text is: {''.join(output_text)}")

    else:
        print("Invalid input")


decoding = True
while decoding:

    n_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    plain_text = input("Type your message:\n").lower()

    # In case user input is not int
    while True:
        try:
            n_shift = int(input("Type the shift number:\n"))
            break

        except ValueError:
            print("This is not a number, try again")

    # calling caesar with user input as arguments
    caesar(n_direction, plain_text, n_shift)

    # asking user if he wants to do it again
    again = input("Do you want to do it again?(y/n)\n").lower()

    if again == "n" or again == "no":
        decoding = False

print("Good Bye!")

# ps. if we want to encode numbers, we just add them to the "alphabet" list
