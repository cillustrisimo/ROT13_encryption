iterable_alphabet = "abcdefghijklmnopqrstuvwxyz"
rot_alphabet = []
alphabet_key = list(iterable_alphabet)

ROT = int(input("Please enter desired number to ROT: "))
non_encrypted = input("Please enter the text you wish to encrypt: ")

x = 0
y = ROT

for i in range(ROT):
    iterable_alphabet = iterable_alphabet + iterable_alphabet

for i in range(0, 26):
    rot_alphabet.append(iterable_alphabet[x + y])
    x = x + 1
    y = ROT

rot_alphabet_key = dict(zip(alphabet_key, rot_alphabet))

encrypted = "".join(rot_alphabet_key.get(character, character) for character in non_encrypted)

print(encrypted)







