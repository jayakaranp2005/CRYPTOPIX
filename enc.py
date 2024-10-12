from PIL import Image
from cryptography.fernet import Fernet
import io

def generate_and_save_key():
   
    key = Fernet.generate_key()
    
    key_path='fernet_key.key'
    with open(key_path, 'wb') as key_file:
        key_file.write(key)
    
    print(f"Fernet Key saved to '{key_path}'.")

def load_key(key_path='fernet_key.key'):
    # Read the key from the file
    with open(key_path, 'rb') as key_file:
        key = key_file.read()
    return key

def encrypt_data(data, key):
    # Create a Fernet object with the key
    fernet = Fernet(key)
    
    # Encrypt the data
    encrypted_data = fernet.encrypt(data)
    return encrypted_data

def main():
    # Uncomment the line below to generate a new key (run this once)
    generate_and_save_key()  

    # Load the Fernet key
    key = load_key()

    # Open the image file
    with Image.open('img2.jpg') as img:
        # Convert image to bytes
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format=img.format)
        img_bytes = img_byte_arr.getvalue()

    # Encrypt the image bytes
    encrypted_data = encrypt_data(img_bytes, key)

    # Save the encrypted data to a file
    with open('encrypted_image.enc', 'wb') as enc_file:
        enc_file.write(encrypted_data)

    print("Image encrypted and saved to 'encrypted_image.enc'.")

if __name__ == "__main__":
    main()


