def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            shifted_char = chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
            result += shifted_char
        else:
            result += char
    return result


# Example usage
plain_text = input("Enter the text to encrypt: ")
shift_value = int(input("Enter the shift value: "))
encrypted_text = caesar_cipher(plain_text, shift_value)
print("Encrypted text:", encrypted_text)
