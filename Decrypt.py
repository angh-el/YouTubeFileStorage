from cryptography.fernet import Fernet

class Decrypt:
    def __init__(self, key_file_path):
        #file where they key is saved
        self.key_file_path = key_file_path

    def decrypt_contents(self, encrypted_text):
        with open(self.key_file_path, 'rb') as filekey:
            key = filekey.read()

        #create a cipher using the key
        cipher_suite = Fernet(key)

        #decrypt contens
        decrypted_contents = cipher_suite.decrypt(encrypted_text.encode('utf-8')).decode('utf-8')

        return decrypted_contents
