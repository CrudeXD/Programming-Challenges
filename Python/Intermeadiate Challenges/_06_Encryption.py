cipher = {"A": "T", "B": "D", "C": "L", "D": "O", "E": "F",
          "F": "A", "G": "G", "H": "J", "I": "K", "J": "R",
          "K": "I", "L": "C", "M": "V", "N": "P", "O": "W",
          "P": "U", "Q": "X", "R": "Y", "S": "B", "T": "E",
          "U": "Z", "V": "Q", "W": "S", "X": "N", "Y": "M",
          "Z": "H"}

x = input("Input any phrase to be incrypted: ").upper()
encrypted = ''


def encrypt(phrase):
    global encrypted
    for letter in phrase:
        if letter in cipher:
            encrypted += cipher[letter]
        else:
            encrypted += letter
    return encrypted


print(encrypt(x))
