from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as Tk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"../img")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class VigenerePage(Tk.Frame):
    def __init__(self, master, pageManager):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.pack()
        self.Vigenere()

    def Vigenere(self):
        self.canvas = Canvas(
            self.master,
            bg = "#F4F3F9",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            339.5,
            589.5,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=88.0,
            y=537.0,
            width=503.0,
            height=103.0
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("encrypt_button.png"))
        self.encrypt_button = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.encrypt(),
            relief="flat"
        )
        self.encrypt_button.place(
            x=88.0,
            y=682.0,
            width=241.0,
            height=55.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("reset_button.png"))
        self.reset_button = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("reset_button clicked"),
            relief="flat"
        )
        self.reset_button.place(
            x=697.0,
            y=682.0,
            width=503.0,
            height=55.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("decrypt_button.png"))
        self.decrypt_button = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("decrypt_button clicked"),
            relief="flat"
        )
        self.decrypt_button.place(
            x=350.0,
            y=682.0,
            width=241.0,
            height=55.0
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            339.5,
            412.5,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=88.0,
            y=360.0,
            width=503.0,
            height=103.0
        )

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            948.5,
            589.5,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_3.place(
            x=697.0,
            y=537.0,
            width=503.0,
            height=103.0
        )

        self.entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            948.5,
            412.5,
            image=self.entry_image_4
        )
        self.entry_4 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_4.place(
            x=697.0,
            y=360.0,
            width=503.0,
            height=103.0
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("download_button.png"))
        self.download_button = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("download_button clicked"),
            relief="flat"
        )
        self.download_button.place(
            x=697.0,
            y=226.0,
            width=262.0,
            height=75.0
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("upload_button.png"))
        self.upload_button = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("upload_button clicked"),
            relief="flat"
        )
        self.upload_button.place(
            x=88.0,
            y=226.0,
            width=262.0,
            height=75.0
        )

        self.button_image_6 = PhotoImage(
            file=relative_to_assets("back_button.png"))
        self.back_button = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.click_backHome(),
            relief="flat"
        )
        self.back_button.place(
            x=88.0,
            y=104.0,
            width=97.0,
            height=55.0
        )

        self.canvas.create_text(
            697.0,
            505.0,
            anchor="nw",
            text="Ciphertext (5-word):",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            697.0,
            331.0,
            anchor="nw",
            text="Ciphertext (no space):",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            88.0,
            505.0,
            anchor="nw",
            text="Enter secret key for encryption and decryption:",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            88.0,
            331.0,
            anchor="nw",
            text="Enter text for encryption and decryption:",
            fill="#000000",
            font=("Inter", 20 * -1)
        )

        self.canvas.create_text(
            310.0,
            97.0,
            anchor="nw",
            text="Vigenere Cipher Standard",
            fill="#000000",
            font=("Inter Bold", 64 * -1)
        )

    def startPage(self):
        self.mainloop()
    
    def click_backHome(self):
        self.origin.Home()
    
    def remove_not_alphabet(text):
        remove = "".join(i for i in text if i.isalpha())
        return remove
    
    def length_key(plaintext,key):
        while len(key) < len(plaintext):
            key += key
        return key[:len(plaintext)]
    
    def uppercase_text(text):
        return text.upper()
    
    def text_with_space(text):
        group_text = []
        for i in range (0, len(text), 5):
            space_text = text[i:i+5]
            group_text.append(space_text)
        result = " ".join(group_text)
        return result

    def encrypt(self):
        self.origin.Vigenere()
        plaintext = self.entry_image_1.get()
        key = self.entry_image_2.get()
        
        non_alphabet_plaintext = self.remove_not_alphabet(plaintext)
        non_alphabet_key = self.remove_not_alphabet(key)
        check_length_key = self.length_key(non_alphabet_plaintext,non_alphabet_key)
        uppercase_plaintext = self.uppercase_text(non_alphabet_plaintext)
        uppercase_key = self.uppercase_text(check_length_key)

        ciphertext = []
        for i in range (len(uppercase_plaintext)):
            plaintext_to_int = ord(uppercase_plaintext[i]) - ord('A')
            key_to_int = ord(uppercase_key[i]) - ord('A')
            encrypt_formula = (plaintext_to_int + key_to_int) % 26
            ciphertext.append(chr(encrypt_formula + ord('A')))
        result_no_space = "".join(ciphertext)
        self.entry_image_3.set(result_no_space)

        result_with_space = self.text_with_space(result_no_space)
        self.entry_image_4.set(result_with_space)
