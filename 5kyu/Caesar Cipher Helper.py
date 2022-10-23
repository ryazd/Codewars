class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = shift
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def encode(self, str):
        upper_str = str.upper()
        encoded_str = ''
        for letter in upper_str:
            if letter.isalpha():
                index = self.alphabet.index(letter) + self.shift
                modified_idx = index - 26 if index >= 26 else index
                encoded_str += self.alphabet[modified_idx]
            else:
                encoded_str += letter
        return encoded_str

    def decode(self, str):
        upper_str = str.upper()
        decoded_str = ''
        for letter in upper_str:
            if letter.isalpha():
                index = self.alphabet.index(letter) - self.shift
                modified_idx = 26 + index if index < 0 else index
                decoded_str += self.alphabet[modified_idx]
            else:
                decoded_str += letter
        return decoded_str