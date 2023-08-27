import tkinter as tk
import random
import string

class PasswordGenerator:
    def __init__(self, r):
        self.r = r
        self.r.title("Password Generator")
        self.r.geometry("500x250")

        self.label = tk.Label(r, text="Password Length:")
        self.label.pack(pady=10)

        self.length_entry = tk.Entry(r)
        self.length_entry.pack(pady=10)

        self.generate_button = tk.Button(r, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)

        self.result_label = tk.Label(r, text="")
        self.result_label.pack(pady=10)

    def generate_password(self):
        password_length = int(self.length_entry.get())
        if password_length < 6:
            self.result_label.config(text="Password length should be at least 6 characters")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(password_length))
        self.result_label.config(text="Generated Password: " + password)

if __name__ == "__main__":
    r = tk.Tk()
    app = PasswordGenerator(r)
    r.mainloop()