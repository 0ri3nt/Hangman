import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def autokey_cipher(text, key):
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            key_char = key[key_index % len(key)]
            key_index += 1
            result += chr((ord(char) - base + ord(key_char) - ord('A')) % 26 + base)
        else:
            result += char
    return result

def encrypt_file(file_path, encryption_method, key_entry):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        key = key_entry.get()

        if encryption_method == "Caesar":
            shift = 3  # You can change the shift value as needed
            result = caesar_cipher(content, shift)
        elif encryption_method == "Autokey":
            result = autokey_cipher(content, key)
        else:
            raise ValueError("Invalid encryption method")

        with open(file_path + '_encrypted.txt', 'w') as encrypted_file:
            encrypted_file.write(result)

        result_label.config(text="Encryption successful! Output file: " + file_path + '_encrypted.txt')

    except Exception as e:
        result_label.config(text="Error: " + str(e))

def decrypt_file(file_path, encryption_method, key_entry):
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        key = key_entry.get()

        if encryption_method == "Caesar":
            shift = 3  # You can change the shift value as needed
            result = caesar_cipher(content, -shift)  # Decrypt using the reverse shift
        elif encryption_method == "Autokey":
            result = autokey_cipher(content, key)
        else:
            raise ValueError("Invalid encryption method")

        with open(file_path + '_decrypted.txt', 'w') as decrypted_file:
            decrypted_file.write(result)

        result_label.config(text="Decryption successful! Output file: " + file_path + '_decrypted.txt')

    except Exception as e:
        result_label.config(text="Error: " + str(e))

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    file_path_entry.delete(0, tk.END)
    file_path_entry.insert(tk.END, file_path)

# Tkinter setup
root = tk.Tk()
root.title("Text File Encryption/Decryption")

# File selection
file_label = tk.Label(root, text="Select a text file:")
file_label.pack()

file_path_entry = tk.Entry(root)
file_path_entry.pack()

browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack()

# Encryption method selection
encryption_label = tk.Label(root, text="Select encryption/decryption method:")
encryption_label.pack()

encryption_method_var = tk.StringVar()
encryption_method_var.set("Caesar")  # Default encryption method
encryption_menu = ttk.Combobox(root, textvariable=encryption_method_var, values=["Caesar", "Autokey"])
encryption_menu.pack()

# Key entry
key_label = tk.Label(root, text="Enter key:")
key_label.pack()

key_entry = tk.Entry(root)
key_entry.pack()

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

# Encrypt button
encrypt_button = tk.Button(root, text="Encrypt", command=lambda: encrypt_file(file_path_entry.get(),
                                                                             encryption_method_var.get(),
                                                                             key_entry))
encrypt_button.pack()

# Decrypt button
decrypt_button = tk.Button(root, text="Decrypt", command=lambda: decrypt_file(file_path_entry.get(),
                                                                             encryption_method_var.get(),
                                                                             key_entry))
decrypt_button.pack()

# Run the Tkinter main loop
root.mainloop()
