from PIL import Image
from cryptography.fernet import Fernet
import io

def decrypt_data(encrypted_data, key):
    # Create a Fernet object with the key
    fernet = Fernet(key)
    
    # Decrypt the data
    decrypted_data = fernet.decrypt(encrypted_data)
    return decrypted_data

def main(key_input):
    # Convert the key input to bytes
    key = key_input.encode()  

    # Read the encrypted data from the file
    with open('encrypted_image.enc', 'rb') as enc_file:
        encrypted_data = enc_file.read()

    # Decrypt the image data
    decrypted_data = decrypt_data(encrypted_data, key)

    # Save the decrypted data to an image file
    decrypted_img = Image.open(io.BytesIO(decrypted_data))
    decrypted_img.save('decrypted_image.png')

    print("Image decrypted and saved to 'decrypted_image.png'.")

if __name__ == "__main__":
 
    pass  

