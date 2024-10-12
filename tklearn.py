from tkinter import Tk, Label, Button, Entry, StringVar, messagebox
from PIL import Image, ImageTk
from enc import generate_and_save_key, load_key, main as m1
from denc import decrypt_data, main as m2

# Initialize the Tkinter window
root = Tk()
root.title("Image Encryption App")
root.geometry("400x500")
root.configure(bg="#f0f0f0")

# Load and display the logo image
image = Image.open("img1.png")
image = image.resize((100, 100))
logo = ImageTk.PhotoImage(image)

logo_label = Label(root, image=logo, bg="#f0f0f0")
logo_label.pack(pady=10)

# Display the heading
heading_label = Label(root, text="Image Encryption App", font=("Arial", 20, "bold"), fg="#003366", bg="#f0f0f0")
heading_label.pack(pady=10)

# Encryption button
encrypt_button = Button(root, text="Encrypt Image", command=m1, font=("Arial", 14), bg="#0066cc", fg="white", width=20, height=2)
encrypt_button.pack(pady=10)

# Fernet key entry for decryption
key_var = StringVar()  # Variable to hold the Fernet key

key_label = Label(root, text="Enter Fernet Key for Decryption:", font=("Arial", 12), fg="#333333", bg="#f0f0f0")
key_label.pack(pady=5)

key_entry = Entry(root, textvariable=key_var, font=("Arial", 12), width=35)
key_entry.pack(pady=5)

# Decryption button
def decrypt_via_gui():
    key_input = key_var.get()  # Get the key from the entry field
    if not key_input:
        messagebox.showerror("Error", "Please enter the Fernet key.")
        return

    try:
        m2(key_input)  # Pass the Fernet key to the decryption script
        messagebox.showinfo("Success", "Image decrypted successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed: {e}")

decrypt_button = Button(root, text="Decrypt Image", command=decrypt_via_gui, font=("Arial", 14), bg="#cc3300", fg="white", width=20, height=2)
decrypt_button.pack(pady=10)

status_label = Label(root, text="", font=("Arial", 12), fg="#333333", bg="#f0f0f0")
status_label.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
