# ROT13_Encryption Script

---
At this point, I should probably just rename this to a ceasar cipher script. In anycase, this is a simple script that can encode or decode any given text to the ROT(X) of your choice.

It works by creating a small key that matches a letter in the alphabet to its positional equivalent in a ROT(x) alphabet. Each run creates a new key.

- When encoding, you simply input your text and then the number of times you wish to rotate over the alphabet.

- When decoding, you can choose to either "brute-force" or decode with a certain number of rotations.
  - If decoding under the brute force option, it creates a large key of each alphabet character to its positional equivalent in various ROT positions.
  - The output is then every single possibility of decoding from your inputted text.

You should, of course, not actually use this for encoding anything important.
