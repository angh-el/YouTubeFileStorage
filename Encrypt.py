from cryptography.fernet import Fernet


class Encrypt:
    def __init__(self, file_path):
        self.file_path = file_path
        self.key = None

    def generate_key(self):
        self.key = Fernet.generate_key()
        with open('filekey.key', 'wb') as filekey:
            filekey.write(self.key)

    def encrypt_contents(self):
        if self.key is None:
            self.generate_key()

        with open(self.file_path, 'r', encoding='utf-8') as file:
            plaintext = file.read()

        cipher_suite = Fernet(self.key)


        encrypted_contents = cipher_suite.encrypt(plaintext.encode('utf-8'))

        return encrypted_contents.decode('utf-8')

    def get_file_contents(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            contents = file.read()
            return repr(contents)

        
