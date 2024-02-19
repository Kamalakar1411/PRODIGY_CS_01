def caesar_cipher(text, shift, mode="encrypt"):
    """Encrypts or decrypts text using the Caesar Cipher algorithm.

    Args:
        text: The text to encrypt or decrypt.
        shift: The number of positions to shift each letter.
        mode: "encrypt" or "decrypt" (default: "encrypt").

    Returns:
        The encrypted or decrypted text.
    """

    result = ""
    for char in text:
        if char.isalpha():
            lowercase_char = char.lower()
            new_position = (ord(lowercase_char) - ord('a') + shift) % 26
            new_char = chr(ord('a') + new_position)
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char

    return result

while True:
    mode = input("Enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ").lower()
    if mode == 'q':
        break

    text = input("Enter the text: ")
    shift = int(input("Enter the shift value: "))

    if mode == 'e':
        encrypted_text = caesar_cipher(text, shift)
        print("Encrypted text:", encrypted_text)
    elif mode == 'd':
        decrypted_text = caesar_cipher(text, -shift) 
        print("Decrypted text:", decrypted_text)
    else:
        print("Invalid mode. Please enter 'e', 'd', or 'q'.")
