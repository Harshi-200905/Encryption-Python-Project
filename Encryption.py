
# Layer 1: Caesar Encryption
def caesar_encryption(text, shift = 3):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result =""
    for letter in text.upper():
        if letter in letters:
            place = letters.index(letter)
            new_place = place + shift
            while new_place>=len(letters):
                new_place = new_place - len(letters)
            result += letters[new_place]
        else:
            result += letter
    return result

# Layer 2: Substitution Encryption
def substitution_encryption(text):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mixup = "QWERTYUIOPASDFGHJKLZXCVBNM"
    result = ""
    for letter in text.upper():
        if letter in letters:
            place = letters.index(letter)
            result = result + mixup[place]
        else:
            result = result +letter
    return result

# Layer 3: Transposition Encryption
def transposition_encryption(text):
    result = ""
    mid = len(text)//2
    if len(text)%2==0:
        result = text[mid:] + text[: mid]
    else:
        result = text[mid+1:]+text[mid]+text[:mid]
    return result

# Layer 4: Custom Encryption (custom choice)
def custom_encryption(text, key):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    key = key.upper()
    key_index = 0
    for char in text.upper():
        if char in letters:
            shift = letters.index(key[key_index%len(key)])
            place = letters.index(char)
            new_place = (place + shift)% len(letters)
            result += letters[new_place]
            key_index += 1
        else:
            result += char
    return result


# Layer 1: Caesar Decryption
def caesar_decryption(text, shift = 3):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    result = ""
    for letter in text.upper():
        if letter in letters:
            place = letters.index(letter)
            new_place = place-shift
            while new_place<0:
                new_place = new_place+len(letters)
            result = result + letters[new_place]
        else:
            result = result +letter
    return result

# Layer 2: Substitution Decryption
def substitution_decryption(text):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mixup = "QWERTYUIOPASDFGHJKLZXCVBNM"
    result = ""
    for letter in text.upper():
        if letter in mixup:
            place = mixup.index(letter)
            result = result + letters[place]
        else:
           result = result + letter
    return result

# Layer 3: Transposition Decryption
def transposition_decryption(text):
    mid = len(text)//2
    if len(text) %2 ==0:
        return text[mid:] + text[:mid]
    else:
        first_part = text[:-mid-1]
        middle_char =text[-mid-1]
        last_part = text[-mid:]
        return last_part + middle_char + first_part

# Layer 4: Custom Decryption (custom choice)
def custom_decryption(text, key):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result= ""
    key = key.upper()
    key_index = 0
    for char in text.upper():
        if char in letters:
            shift = letters.index(key[key_index % len(key)])
            place = letters.index(char)
            new_place = (place-shift)%len(letters)
            result += letters[new_place]
            key_index += 1
        else:
            result += char

    return result


# --- Pipeline functions ---

def encrypt_all_four(text, shift, key):
    # write caesar_encryption here
    result = caesar_encryption(text, shift)
    print("After Caesar Encryption:", result)

    # write substitution_encryption here
    result = substitution_encryption(result)
    print("After Substitution Encryption:", result)

    # write transposition_encryption here
    result = transposition_encryption(result)
    print("After Transposition Encryption:", result)

    # write custom_encryption here
    result = custom_encryption(result, key)
    print("After Custom Encryption:", result)

    return result


def decrypt_all_four(text, shift, key):
    # write custom_decryption here
    result =custom_decryption(text, key)
    print("After Custom Decryption:", result)

    # write transposition_decryption here
    result = transposition_decryption(result)
    print("After Transposition Decryption:",result)

    # write substitution_decryption here
    result = substitution_decryption(result)
    print("After Substitution Decryption:", result)

    # write caesar_decryption here
    result = caesar_decryption(result, shift)
    print("After Caesar Decryption:",result)

    return result


# --- Example test ---
message = input("Enter a message ")
encrypted = encrypt_all_four(message, shift=3, key="KEY")
print()
decrypted = decrypt_all_four(encrypted, shift=3, key="KEY")

print("\nOriginal:", message)
print("Final Encrypted Message:", encrypted)
print("Final Decrypted Message:", decrypted)