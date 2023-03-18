iterable_alphabet = "abcdefghijklmnopqrstuvwxyz"
rot_alphabet = []
alphabet_key = list(iterable_alphabet)

user_choice = input("Do you wish to encode or decode? ")
user_choice = user_choice.strip().lower()


if user_choice == "encode":

    ROT = int(input("Please enter desired number to ROT: "))
    non_encrypted = input("Please enter the text you wish to encrypt: ")

    x = 0
    y = ROT

    for i in range(ROT):
        iterable_alphabet = iterable_alphabet + iterable_alphabet

    for i in range(0, 26):
        rot_alphabet.append(iterable_alphabet[x + y])
        x = x + 1

    rot_alphabet_key = dict(zip(alphabet_key, rot_alphabet))
    encrypted = "".join(rot_alphabet_key.get(character, character) for character in non_encrypted)

    print(f"{non_encrypted} placed through a ROT {ROT} is: {encrypted}")

elif user_choice == "decode":
    decode_choice = input("Type brute if you do not know the ROT cyphers number, otherwise just press enter: ")
    decode_choice = decode_choice.lower().strip()
    encrypted = input("Please type the text you wish to decrypt: ")

    if decode_choice == "brute":
        min_range_ROT = int(input("Please enter the minimum number for the ROT range: "))
        max_range_ROT = int(input("Please enter the maximum number for the ROT range: "))

        print(f"Attempting to brute force from {min_range_ROT} to {max_range_ROT}, this may take a while...")

        for ranges in range(max_range_ROT):
            iterable_alphabet = iterable_alphabet + iterable_alphabet

        print(iterable_alphabet)
        max_range_ROT = max_range_ROT + 1

        rot_alphabets = {}
        x = 0
        for ranges in range(min_range_ROT, max_range_ROT):
            rot_alphabet = []
            for i in range(0, 26):
                y = ranges
                rot_alphabet.append(iterable_alphabet[x + y])
                x = x + 1
                rot_alphabets[f"rot{ranges}"] = rot_alphabet
        print(rot_alphabets)
        rot_alphabet_keys = {}
        for i in range(min_range_ROT, max_range_ROT):
            rot_alphabet_keys[f"rot{i}"] = dict(zip(rot_alphabets[f"rot{i}"], alphabet_key))

        decrypted_outcomes = {}
        for key in rot_alphabet_keys:
            decrypted = "".join(rot_alphabet_keys[key].get(character, character) for character in encrypted)
            decrypted_outcomes[key] = decrypted

        print("Brute force outcomes: ")
        print(decrypted_outcomes)

    if decode_choice == "":
        decode_ROT = int(input("Please enter the number of the ROT cypher you wish to decode. "))
        x = 0
        y = decode_ROT

        for i in range(decode_ROT):
            iterable_alphabet = iterable_alphabet + iterable_alphabet

        for i in range(0, 26):
            rot_alphabet.append(iterable_alphabet[x + y])
            x = x + 1

        decode_rot_alphabet_key = dict(zip(rot_alphabet, alphabet_key))
        decrypted = "".join(decode_rot_alphabet_key.get(character, character) for character in encrypted)

        print(f" {encrypted} placed through back through a ROT{decode_ROT} cypher is: {decrypted}")
else:
    print("Please enter either encode or decode!")








