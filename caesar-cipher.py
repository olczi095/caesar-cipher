class CaesarCipher:
    """
    A class to represent a Caesar Cipher.

    Args:
        alphabet (str): The alphabet taken from the user.
        shift (int): The shift chosen by the user to encrypt or decrypt alphabet.
    """

    def __init__(self, alphabet, shift):
        self.alphabet = alphabet
        self.shift = shift

    @property
    def cipher(self):
        """Returns encrypted alphabet."""
        new_alphabet = ''
        for letter in self.alphabet:
            new_idx = (
                              self.alphabet.index(letter) + self.shift
                      ) % len(self.alphabet)
            new_alphabet += self.alphabet[new_idx]
        return new_alphabet

    def encrypt(self, message):
        """Takes normal message and returns encrypted message. """
        encrypted_message = ''
        for letter in message:
            if letter not in self.alphabet:
                encrypted_message += letter
            else:
                encrypted_message += self.cipher[self.alphabet.index(letter)]
        return encrypted_message

    def decrypt(self, message):
        """Takes encrypted message and returns decrypted message."""
        decrypted_message = ''

        for letter in message:
            if letter not in self.cipher:
                decrypted_message += letter
            else:
                decrypted_message += self.alphabet[self.cipher.index(letter)]
        return decrypted_message


if __name__ == "__main__":
    checking = True

    while checking:
        user_alphabet = input("Type the alphabet you want to use (for example - \"ABCDEFGHIJKLMNOPQRSTUVWXYZ\")\n>>> ")
        user_shift = int(input("Type the shift:\n>>> "))
        user_message = input("Type the message:\n>>> ")

        user_cipher = CaesarCipher(user_alphabet, user_shift)
        usage = input("If you want to encrypt the message, please type \"encrypt\".\n"
                      " Otherwise, if you want to decrypt it, type \"decrypt\"\n>>> ")

        if usage.lower() == "encrypt":
            print(f"\nYour encrypted message is: {user_cipher.encrypt(user_message)}")
        elif usage.lower() == "decrypt":
            print(f"\nYour decrypted message is: {user_cipher.decrypt(user_message)}")
        else:
            print("\nYou must have typed a wrong command. Please try again!")
            continue

        play_again = input(f"Do you want to encrypt/decrypt something else? If you want to, type 'yes'.\n>>> ")
        if play_again.lower() != "yes":
            checking = False
